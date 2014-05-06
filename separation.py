import numpy as np
from matplotlib import pyplot as plt

def LinearRegression(X,Y):
	return np.dot(Y,np.dot(np.linalg.pinv(np.dot(X,X.T)),X))

def f(x,a,b,c,d):
	return a*x**3+b*x**2+c*x+d

def aug(X):
	return np.column_stack((X**3,X**2,X,np.ones(len(X))))

def error(X,Y):
	return sum(np.sqrt((X-Y)**2))/(len(X))

def getY (start, Y, upLim, lowLim):
	XA = np.arange(lowLim, start)
	XB = np.arange(start, upLim)
	pA = LinearRegression(aug(XA), Y[0:(start + (lowLim * -1))])
	pB = LinearRegression(aug(XB), Y[(start + (lowLim * -1)):(upLim + (lowLim * -1))])
	YAll = np.concatenate((f(XA, *pA), f(XB, *pB)))
	return YAll

def main():
	upperLim = 100
	lowerLim = -100

	#initial function
	temp = np.random.randint(lowerLim + 2, upperLim - 2)
	X1 = np.arange(lowerLim,temp)
	X2 = np.arange(temp,upperLim)
	h1 = np.random.randint(-1000,1000,size=4)
	h2 = np.random.randint(-1000,1000,size=4)
	Y = np.concatenate((f(X1,*h1),f(X2,*h2)))
	X = aug(np.arange(lowerLim,upperLim))
	p = LinearRegression(X,Y)


	#initialize min
	start = 0
	minstart = 0
	minerror = 0

	while True:
		Yvalues1 = getY(start, Y, upperLim, lowerLim)
		Yvalues2 = getY((0-start), Y, upperLim, lowerLim)
		error1 = error(Y, Yvalues1)
		error2 = error(Y, Yvalues2)
		if error1<error2:
			if minerror==0 or error1<minerror:
				minstart = start
				minerror = error1
		elif error2<error1:
			if minerror==0 or error2<minerror:
				minstart = 0-start
				minerror = error2

		start = start + 1
		if start == upperLim - 1:
			break


	print temp
	print minstart
	#final function
	Yfinal = getY (minstart, Y, upperLim, lowerLim)

	plt.plot(X[:,-2],Y,c='b')
	plt.plot(X[:,-2],Yfinal,c='r')
	plt.show()

if __name__ == "__main__":
	main()