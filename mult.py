import numpy as np

def f(x):
	return x * 100

def h(x,n):
	return x * n

def cost(a,b):
	return np.mean(np.square(a-b))

def learn(x,f):
	y = f(x)
	n = 0
	err = 1
	while err != 0:
		err = cost(y,h(x,n))
		if err > 0:
			n += 1
		if err < 0:
			n += 1
	print 'solution',n

x = np.arange(10)
learn(x,f)