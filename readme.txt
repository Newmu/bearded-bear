 file with a description of what you're done, 
  a description of how to compile/create your system, and pointers to anything that I positively absolutely have to look at to appreciate how great you are.

Amanda Lee
Amanda.Lee@students.olin.edu

Alec Radford
Alec.Radford@students.olin.edu


WHAT WE DID:
In this folder there are a variety of programs that all return a functional model of inputted data.
We have simple programs such as "mult.py" and "mult_and_add.py" that use modified search algorithms to find functions that will fit the given data.
"polynomial.py" uses linear regression to learn polynomial function up to a degree of three. 
"separation.py" and "derivative.py" deal with data sets that would best be represented with piecewise functions. "separation.py" does a brute force search of all possible separation points in order to find where the function should be split. "derivative.py" roughly calculated the derivative the piecewise function to find the separation point. 

The main part of our project is a program generator that will return functions that best represent either quadratic or distance functions with random parameters. This is done by starting with a general function, evaluating the error, making a small change to the function, and determining whether the error is more or less than before. 
To compile the main part of our project (the program generator) simply run "hcwr_pg.py". 


SAMPLE EXECUTION
Below is a sample execution of our program generator.

Amandas-MacBook-Pro:bearded-bear alee1$ /usr/bin/python2.7 hcwr_pg.py
Learning quadratic function
0 evals, new min mean error 180.9400
2 evals, new min mean error 179.5700
241 evals, new min mean error 174.7000
438 evals, new min mean error 174.1400
453 evals, new min mean error 28.1300
1567 evals, new min mean error 27.6900
1859 evals, new min mean error 5.6100
10000 evals 1606 per second 5.6100 best mean error
20000 evals 1596 per second 5.6100 best mean error
30000 evals 1557 per second 5.6100 best mean error
40000 evals 1394 per second 5.6100 best mean error
48017 evals, new min mean error 0.0000

Learned program in 48018 evaluations taking 39 seconds

Learning distance function
0 evals, new min mean error 12.3694
13 evals, new min mean error 12.1851
14 evals, new min mean error 10.6075
202 evals, new min mean error 10.6057
1495 evals, new min mean error 10.3967
2226 evals, new min mean error 6.6273
4436 evals, new min mean error 5.4170
10000 evals 1283 per second 5.4170 best mean error
20000 evals 1313 per second 5.4170 best mean error
30000 evals 1352 per second 5.4170 best mean error
40000 evals 1371 per second 5.4170 best mean error
50000 evals 1365 per second 5.4170 best mean error
60000 evals 1368 per second 5.4170 best mean error
70000 evals 1357 per second 5.4170 best mean error
80000 evals 1356 per second 5.4170 best mean error
90000 evals 1357 per second 5.4170 best mean error
100000 evals 1361 per second 5.4170 best mean error
110000 evals 1364 per second 5.4170 best mean error
115944 evals, new min mean error 3.7475
120000 evals 1367 per second 3.7475 best mean error
130000 evals 1363 per second 3.7475 best mean error
140000 evals 1289 per second 3.7475 best mean error
147800 evals, new min mean error 3.2024
150000 evals 1279 per second 3.2024 best mean error
154002 evals, new min mean error 3.1162
157464 evals, new min mean error 2.7729
160000 evals 1262 per second 2.7729 best mean error
162477 evals, new min mean error 0.0000

Learned program in 162478 evaluations taking 129 seconds

General Quadratic Function:

def f(a,b,c,d):
    e,f,g,h,i,j,k,l,m,n,o,p,q = a,c,c,a,c,d,a,d,c,b,a,d,b
    k = h * h
    l = e * c

    i = b * k
    i = i + p





    o = n - i

    i = i + l
    return i


Euclidean Distance Function:

def f(a,b,c,d):
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
