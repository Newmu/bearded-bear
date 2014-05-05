import numpy as np
from matplotlib import pyplot as plt

def LinearRegression(X,Y):
	return np.dot(Y,np.dot(np.linalg.pinv(np.dot(X,X.T)),X))

def f(x,a,b,c,d):
	return a*x**3+b*x**2+c*x+d

def aug(X):
	return np.column_stack((X**3,X**2,X,np.ones(len(X))))

X1 = np.arange(-10,-2)
X2 = np.arange(-2,10)
h1 = np.random.randint(-10000,10000,size=4)
h2 = np.random.randint(-10000,10000,size=4)
Y = np.concatenate((f(X1,*h1),f(X2,*h2)))
X = aug(np.arange(-10,10))
p = LinearRegression(X,Y)
print h1
print h2
print p
# model = LinearRegression()
# model.fit(X,Y)
# print model.coef_
# print model.intercept_

plt.plot(X[:,-2],Y,c='b')
plt.plot(X[:,-2],f(X[:,-2],*p),c='r')
plt.show()