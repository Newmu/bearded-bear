import numpy as np
import math as m
from random import choice,randint
from copy import deepcopy
from time import time,sleep

def init(n_in):
	vs = [chr(ord('a')+i) for i in range(n_in)]
	rep = {'ins':vs,'vars':deepcopy(vs),'code':[]}
	return rep

def cost(X,Y,rep):
	exec(render(rep))
	h = np.array([f(*x) for x in X])
	err = np.mean(np.abs(Y-h))
	return err

def gen_code(rep):
	op = choice(ops)
	new_var = chr(ord(max(rep['vars']))+1)
	if op[0] == 'm':
		code = [new_var,op,choice(rep['vars'])]
	else:
		v1,v2 = choice(rep['vars']),choice(rep['vars'])
		# v1,v2 = np.random.choice(rep['vars'],size=2)
		code = [new_var,op,v1,v2]
	rep['code'].append(code)
	rep['vars'].append(new_var)
	return rep

def valid_var_swap_idxs(code):
	valid = []
	for i,c in enumerate(code):
		if len(c) != 3 and c[1] not in ['+','*']:
			valid.append(i)
	return valid

def var_swap(rep):
	idxs = [i for i in range(len(rep['code'])) if len(rep['code'][i]) != 3]
	idx = choice(idxs)
	max_var_idx = idx+len(rep['ins'])
	vs = rep['vars'][:max_var_idx]
	v_to_swap_idx = randint(0,1)
	v_to_swap = rep['code'][idx][v_to_swap_idx+2]
	vs.remove(rep['code'][idx][v_to_swap_idx+2])
	rep['code'][idx][v_to_swap_idx+2] = choice(vs)
	return rep

def order_swap(rep):
	idxs = valid_var_swap_idxs(rep['code'])
	idx = choice(idxs)
	tmp = rep['code'][idx][2]
	rep['code'][idx][2] = rep['code'][idx][3]
	rep['code'][idx][3] = tmp
	return rep

# def delete_code():

def neighbor(rep):
	return choice(moves)(rep)

def render_code(rep):
	if len(rep) == 3:
		code = '    %s = %s(%s)\n'%tuple(rep)
	else:
		code = '    %s = %s %s %s\n'%(rep[0],rep[2],rep[1],rep[3])
	return code

def render(rep):
	if len(rep['ins']) == 1:
		head = 'def f(%s):\n'%rep['ins'][0]
	else:
		head = 'def f(%s,%s):\n'%(rep['ins'][0],','.join(rep['ins'][1:]))
	body = ''.join([render_code(code) for code in rep['code']])
	end = '    return %s'%max(rep['vars'])
	return head+body+end

def main():
	ops = ['m.sqrt','+','-','*']
	moves = [gen_code,var_swap,order_swap]

	exec("""
def distance(x1, y1, x2, y2):
	dx = x2 - x1
	dy = y2 - y1
	dsquared = dx**2 + dy**2
	result = m.sqrt(dsquared)
	return result
	""")

	exec("""
def squared_error(a, b):
	c = a - b
	d = c ** 2
	return d
	""")

	rep = {'ins':['a','b'],'vars':['a','b','c'],'code':[('c','+','a','b')]}
	rep = {'ins':['a','b','c','d'],
		'vars':['a','b','c','d','e','f','g','h','i','j'],
		'code':[['e','-','c','a'],
		['f','-','d','b'],
		['g','*','e','e'],
		['h','*','f','f'],
		['i','+','g','h'],
		['j','m.sqrt','i']]}

	rep = init(4)
	X = np.random.randint(-10,10,size=(100,4))
	Y = np.array([distance(*x) for x in X])
	print X
	print Y
	cmin = np.inf
	repmin = deepcopy(rep)
	t = time()
	n = 0
	for starts in range(100000):
		if starts % 1000 == 0 and starts != 0: print starts,n/(time()-t)
		rep = init(4)
		for i in range(30):
			try:
				rep = neighbor(rep)
				c = cost(X,Y,rep)
				if c < cmin:
					cmin = deepcopy(c)
					repmin = deepcopy(rep)
				if c == 0:
					if len(rep['code']) < len(repmin['code']):
						repmin = deepcopy(rep)
			except:
				pass
			n += 1
	print cmin
	print repmin
	print render(repmin)

	
if __name__ == "__main__":
	main()

# choices = [delete_line,gen_line]

# rep = {'ins':['a','b'],'vars':['a','b','c'],'code':[('c','+','a','b')]}
# print render(rep)
# print render(neighbor(rep))
# rep = {'ins':['a','b','c','d'],
# 	'vars':['a','b','c','d','e','f','g','h','i','j'],
# 	'code':[('e','-','c','a'),
# 	('f','-','d','b'),
# 	('g','**','e','2'),
# 	('h','**','f','2'),
# 	('i','+','g','h'),
# 	('j','m.sqrt','i')]}

# exec("""
# def f(x):
# 	x = x + 1
# 	return x ** 2""")

# exec("""
# def f(a,b):
# 	c = a + b
# 	return c""")

# exec("""
# def distance(x1, y1, x2, y2):
# 	dx = x2 - x1
# 	dy = y2 - y1
# 	dsquared = dx**2 + dy**2
# 	result = m.sqrt(dsquared)
# 	return result
# 	""")

# print f(1,2)
# print distance(0,0,3,4)
# gen_line(['a','b','c'])
# s = render(rep)
# print s
# exec(s)
# print f(0,0,4,3)