import numpy as np
from time import time,sleep
from random import randint

def f(x,m,b):
	return m*x + b

def cost(a,b):
	'''
	Evaluate mean absolute error between a and b.
	'''
	return np.mean(np.abs(a-b))

def tabu_search(x,y,nm=2,nb=2):
	'''
	Given an x and a y find the underlying function of the form
	y = mx + b via tabu search.
	'''
	tabu = set()
	m = 0
	b = 0
	n = 0
	cur_obj = np.inf

	while True:
		# Evaluate neighborhood around current best hypothesis
		hypos = []
		objs = []
		for i in range(-nm,nm+1):
			for j in range(-nb,nb+1):
				if str([m+i,b+j]) not in tabu:
					hypos.append([m+i,b+j])
					objs.append(cost(y,f(x,m+i,b+j)))
					n += 1

		# choose minimum to transition to
		m,b = hypos[np.argmin(objs)]
		tabu.add(str([m,b]))

		if np.min(objs) == 0:
			print
			print 'SOLUTION FOUND'
			break
	return m,b,n

def main(n):
	'''
	Evaluate n random functions and check that tabu search finds
	underlying functions. It should find in under 10 seconds per function.
	'''
	for example in range(n):
		# generate random function
		m = randint(-10000,10000)
		b = randint(-10000,10000)

		print
		print 'Current function: y = %0.fx + %0.f'%(m,b)

		# evaluate it
		x = np.arange(100)
		y = f(x,m,b)

		t = time()
		m,b,n = tabu_search(x,y)
		t = time()-t
		e = 10000**2/float(n)

		print 'Found slope %s\nFound offset %s\nIn %0.f checks\nIn %.2f seconds\nEfficiency Ratio: %.2f'%(m,b,n,t,e)
		sleep(2.5)

if __name__ == "__main__":
    main(10)