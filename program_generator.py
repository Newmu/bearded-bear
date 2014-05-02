import numpy as np
import math as m
from random import choice,randint

def gen_str_rep(rep):
	print rep

def gen_line(vs):
	op = choice(ops)
	if op[0] == 'm':
		line = [chr(ord(max(vs))+1),op,choice(vs)]
	else:
		v1,v2 = np.random.choice(vs,size=2,replace=False)
		if randint(0,5) == 0:
			v2 = str(randint(-1,10))
		line = [chr(ord(max(vs))+1),op,v1,v2]
	return line

def render_line(rep):
	if len(rep) == 3:
		line = '%s = %s(%s)'%rep
	else:
		line = '%s = %s %s %s'%(rep[0],rep[2],rep[1],rep[3])

def render(rep):
	if len(rep['ins']) == 1:
		head = 'def f(%s):\n'%rep['ins'][0]
	else:
		head = 'def f(%s,%s):\n'%(rep['ins'][0],','.join(rep['ins'][1:]))
	vinit = '\n'.join([v+' = 0' for v in rep['vars']])
	body = '\n'.join([])

ops = ['m.sqrt','+','-','*','**']
rep = {'ins':['a','b'],'vars':['c'],'code':[['c','+','a','b']]}

exec("""def f(x):
	x = x + 1
	return x ** 2""")

exec("""def f(a,b):
	c = a + b
	return c""")

exec("""def distance(x1, y1, x2, y2):
	dx = x2 - x1
	dy = y2 - y1
	dsquared = dx**2 + dy**2
	result = m.sqrt(dsquared)
	return result
	""")

print f(1,2)
print distance(0,0,3,4)
gen_line(['a','b','c'])
render(rep)