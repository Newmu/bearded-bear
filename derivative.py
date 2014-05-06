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

def derivative(Y):
	s = len(Y)
	toReturn = []
	for j in range(0,s-2):
		val = (Y[j]-Y[j+2])/2
		toReturn.append(val)
	return toReturn

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



	print temp
	Yy = derivative(Y)
	Yyy = derivative (Yy)
	Xxxx = np.arange(-97, 97)
	Yyyy = np.absolute(derivative (Yyy))
	Yyyyguess = np.gradient(Y)
	point = X[np.argmax(Y)]
	print Yyyyguess
	Yfinal = getY (point, Yyyyguess, upperLim, lowerLim)

	print point
	plt.plot(Xxxx, Yyyy, c = 'r')
	plt.plot(X[:,-2],Y,c='b')
	#plt.plot(X[:,-2],Yfinal,c='r')
	plt.show()

if __name__ == "__main__":
	main()