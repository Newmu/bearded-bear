import numpy as np
import math
from random import choice,randint,random,seed
from copy import copy,deepcopy
from time import time,sleep

np.random.seed(42)
seed(42)

def init(n_in):
	ins = [chr(ord('a')+i) for i in range(n_in)]
	vs = [chr(ord('a')+i) for i in range(n_in+13)]
	v_inits = [choice(ins) for _ in range(13)]
	rep = {'v_inits':v_inits,'ins':ins,'vars':vs,'code':[['NOP'] for i in range(13)]}
	return rep

def cost(X,Y,rep):
	exec(render(rep))
	h = np.array(f(X[:,0],X[:,1],X[:,2],X[:,3])).T
	errs = np.abs(Y-h).mean(axis=0)
	err = np.min(errs)
	var_best = rep['vars'][np.argmin(errs)]
	return err,var_best

def gen_code(rep):
	idx = choice(range(len(rep['code'])))
	op = choice(ops)
	target = choice(rep['vars'][len(rep['ins']):])
	v1 = choice(rep['vars'])
	if op[0] == 'm' or op[0] == 'n':
		code = [target,op,v1]
	else:
		v2 = choice(rep['vars'])
		code = [target,op,v1,v2]
	rep['code'][idx] = code 
	return rep

def valid_order_swap_idxs(code):
	valid = []
	for i,c in enumerate(code):
		if len(c) != 3 and c != ['NOP']:
			if c[1] not in ['+','*']:
				valid.append(i)
	return valid

def var_swap(rep):
	idxs = [i for i in range(len(rep['code'])) if len(rep['code'][i]) != 3 and rep['code'][i] != ['NOP']]
	if len(idxs) > 0:
		idx = choice(idxs)
		vs = copy(rep['vars'])
		v_to_swap_idx = randint(0,1)
		v_to_swap = rep['code'][idx][v_to_swap_idx+2]
		vs.remove(rep['code'][idx][v_to_swap_idx+2])
		rep['code'][idx][v_to_swap_idx+2] = choice(vs)
	return rep

def order_swap(rep):
	idxs = valid_order_swap_idxs(rep['code'])
	if len(idxs) > 0:
		idx = choice(idxs)
		tmp = rep['code'][idx][2]
		rep['code'][idx][2] = rep['code'][idx][3]
		rep['code'][idx][3] = tmp
	return rep

def op_swap(rep):
	idxs = [i for i in range(len(rep['code'])) if len(rep['code'][i]) != 3 and rep['code'][i] != ['NOP']]
	if len(idxs) > 0:
		idx = choice(idxs)
		rep['code'][idx][1] = choice(ops[2:])
	return rep

def delete_code(rep):
	idxs = range(len(rep['code']))
	idx = choice(idxs)
	rep['code'][idx] = ['NOP']
	return rep

def code_order_swap(rep):
	idxs = range(len(rep['code']))
	idx1 = choice(idxs)
	idxs.remove(idx1)
	idx2 = choice(idxs)
	tmp = rep['code'][idx1]
	rep['code'][idx1] = rep['code'][idx2]
	rep['code'][idx2] = tmp
	return rep

def neighbor(rep,n=1):
	rep = deepcopy(rep)
	for move in range(n):
		rep = choice(moves)(rep)
	return rep

def render_code(rep):
	if rep == ['NOP']:
		return '\n'
	if len(rep) == 3:
		code = '    %s = %s(%s)\n'%tuple(rep)
	else:
		code = '    %s = %s %s %s\n'%(rep[0],rep[2],rep[1],rep[3])
	return code

def render(rep,vreturn=None):
	if len(rep['ins']) == 1:
		head = 'def f(%s):\n'%rep['ins'][0]
	else:
		head = 'def f(%s,%s):\n'%(rep['ins'][0],','.join(rep['ins'][1:]))
	vs = ','.join(rep['vars'][len(rep['ins']):])
	vals = ','.join(['%s'%v for v in rep['v_inits']])
	vinit = '    %s = %s\n'%(vs,vals)
	body = ''.join([render_code(code) for code in rep['code']])
	if vreturn != None:
		end = '    return %s'%vreturn
	else:
		end = '    return %s'%','.join(rep['vars'])
	return head+vinit+body+end

def hcwr_pg(X,Y):
	Y = Y.reshape(-1,1)
	rep = init(X.shape[1])
	c = np.inf
	c_min = np.inf
	rep_min = deepcopy(rep)
	i = 0
	t = time()
	while c_min != 0:
		n = neighbor(rep_min,n=5)
		cn,v = cost(X,Y,n)
		if cn < c_min:
			print '%0.f evals, new min mean error %0.4f'%(i,cn)
			program_str = render(n,vreturn=v)
			c_min = deepcopy(cn)
			rep_min = deepcopy(n)
		i += 1

		if i % 10000 == 0:
			print '%0.f evals %0.f per second %0.4f best mean error'%(i,i/(time()-t),c_min)
	
	print
	print 'Learned program in %0.f evaluations taking %0.f seconds'%(i,time()-t)
	return program_str

ops = ['np.square','np.sqrt','+','-','*']
moves = [gen_code,var_swap,order_swap,op_swap,delete_code]

exec("""
def distance(x1, y1, x2, y2):
	dx = x2 - x1
	dy = y2 - y1
	dsquared = dx**2 + dy**2
	result = math.sqrt(dsquared)
	return result
	""")

exec("""
def quadratic(a,b,c,d):
	return (a**2)*b + a*c + d
	""")

rep = init(4)
X = np.random.randint(-10,10,size=(100,4))
Y = np.array([quadratic(*x) for x in X])

print "Learning quadratic function"

learned_quadratic_function = hcwr_pg(X,Y)

print
sleep(1)

Y = np.array([distance(*x) for x in X])

print "Learning distance function"

learned_distance_function = hcwr_pg(X,Y)

print
sleep(1)

print "General Quadratic Function:"
print
print learned_quadratic_function
print

print
sleep(5)

print "Euclidean Distance Function:"
print
print learned_distance_function