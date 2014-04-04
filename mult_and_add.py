import numpy as np
from time import time,sleep
from matplotlib import pyplot as plt

def f(x):
	return -1*x*scaler + round(0.1*scaler)

# def f(x):
	# return -10*x + round(0.1*10)

def h(x,m,b):
	return m*x + b

def cost(a,b):
	return np.sign(np.mean(a-b)),np.mean(np.square(a-b))

def learn(x,f):
	y = f(x)
	m = np.random.randint(-2,2)
	b = np.random.randint(-2,2)
	err = 1
	i = 0
	while err != 0:
		sign,err = cost(y,h(x,m,b))
		# if i % 1000 == 0:
		# 	print i,sign,err,m,b,np.sqrt(err)
		adj = np.sqrt(err)/50.
		adj = np.clip(adj,2,10000)
		# if adj < 2:
			# adj = 2
		# print h(x,m,b)
		# print y
		if sign == 1:
			m += np.random.randint(0,adj)
			b += np.random.randint(0,adj)
		elif sign == -1:
			m -= np.random.randint(0,adj)
			b -= np.random.randint(0,adj)
		elif err != 0:
			m += np.random.randint(-adj,adj)
			b += np.random.randint(-adj,adj)
		i += 1
		# sleep(0.01)			
	return i

def steps_to_converge(x,n):
	global scaler
	scalers = []
	steps = []
	for s in range(1,n):
		print s
		scaler = s
		step = np.mean([learn(x,f) for _ in range(10)])
		scalers.append(s)
		steps.append(step)
	return np.array(scalers),np.array(steps)

# x = np.arange(100)
# learn(x,f)

global scaler
scaler = 1.
x = np.arange(100)
# learn(x,f)
X,Y = steps_to_converge(x,8)
plt.plot(X,Y)
plt.show()