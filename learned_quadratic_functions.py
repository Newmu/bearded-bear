import numpy as np

def quadratic(a,b,c,d):
	return (a**2)*b + c*a + d

def is_valid(true,pred):
	return np.all(true == pred)

def f1(a,b,c,d):
    e,f,g,h,i,j,k,l,m,n,o,p,q = b,a,a,c,a,c,c,a,d,a,d,d,a
    j = np.square(i)

    l = k * a
    m = p - e
    g = j * e
    k = e + a


    p = np.square(l)
    g = o + g
    e = l + g
    k = e - l

    return e

def f2(a,b,c,d):
    e,f,g,h,i,j,k,l,m,n,o,p,q = a,c,c,a,c,d,a,d,c,b,a,d,b
    k = h * h
    l = e * c

    i = b * k
    i = i + p





    o = n - i

    i = i + l
    return i

# Learned in 48018 evaluations taking 21 seconds
def f3(a,b,c,d):
    e,f,g,h,i,j,k,l,m,n,o,p,q = a,c,c,a,c,d,a,d,c,b,a,d,b
    k = h * h
    l = e * c

    i = b * k
    i = i + p





    o = n - i

    i = i + l
    return i

X = np.random.randint(-10,10,size=(100,4))
Y = np.array([quadratic(*x) for x in X])

print 'INPUTS'
print X[:10]
print 'OUTPUTS'
print Y[:10]
Yf1 = np.array([f1(*x) for x in X])
Yf2 = np.array([f2(*x) for x in X])
Yf3 = np.array([f3(*x) for x in X])

print 'f1 is_valid',is_valid(Y,Yf1)
print 'f2 is_valid',is_valid(Y,Yf2)
print 'f3 is_valid',is_valid(Y,Yf3)