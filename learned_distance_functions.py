import numpy as np

def distance(x1,y1,x2,y2):
    dx = x2-x1
    dy = y2-y1
    d = np.sqrt(dx**2+dy**2)
    return d

def is_valid(true,pred):
    return np.all(true == pred)

# Learned in about 660000 evaluations seed = 43
def f1(a,b,c,d):
    e,f,g,h,i,j,k,l,m,n,o,p,q = d,b,a,d,d,b,a,c,b,d,c,c,c
    o = e - b
    o = np.square(o)
    j = e * m
    p = a - q
    f = np.square(b)

    j = np.square(p)
    e = o - o
    q = l - j
    g = j + o

    q = np.sqrt(g)
    h = np.square(c)
    return q

# Learned in about 162478 evaluations seed = 42
def f2(a,b,c,d):
    e,f,g,h,i,j,k,l,m,n,o,p,q = b,b,d,a,b,a,a,b,a,b,c,d,a
    p = d - l
    o = q - c
    p = np.square(p)
    e = n + j
    j = c - m
    q = np.square(o)
    p = q + p
    g = a + d
    h = np.sqrt(p)
    l = np.square(i)
    l = e + j

    f = o * a
    return h


X = np.random.randint(-10,10,size=(100,4))
Y = np.array([distance(*x) for x in X])

print 'INPUTS'
print X[:10]
print 'OUTPUTS'
print Y[:10]
Yf1 = np.array([f1(*x) for x in X])
Yf2 = np.array([f2(*x) for x in X])

print 'f1 is_valid',is_valid(Y,Yf1)
print 'f2 is_valid',is_valid(Y,Yf2)