import myfunctions as de
import math

def f1a(y,x):
    return (y*math.log(y))/x
def f1b(y,x):
    return 6-((2*y)/x)

#Question 1A
de.euler(2,2.71828,f1a,0.2,5)
de.euler(2,2.71828,f1a,0.1,5)
de.euler(2,2.71828,f1a,0.02,5)
de.euler(2,2.71828,f1a,0.01,5)

#Question 1B
de.euler(3,1,f1b,0.22,5)
de.euler(3,1,f1b,0.12,5)
de.euler(3,1,f1b,0.022,5)
de.euler(3,1,f1b,0.012,5)

#Question 2

def f2(z,y,x):
    return 1-x-z
def g2(z,x):
    return z
    
de.rk4(0,2,1,g2,f2,0.2,-5,5)
de.rk4(0,2,1,g2,f2,0.7,-5,5)
de.rk4(0,2,1,g2,f2,0.01,-5,5)
de.rk4(0,2,1,g2,f2,0.05,-5,5)

#Question 3

def f3(z,y,x):
    return z+1
def g3(z,x):
    return z

de.boundary(0,1,1,2*(2.71828-1),5.5,g3,f3,0.2,0.0001)
de.boundary(0,1,1,2*(2.71828-1),5.5,g3,f3,0.02,0.0001)
de.boundary(0,1,1,2*(2.71828-1),5.5,g3,f3,0.05,0.0001)
de.boundary(0,1,1,2*(2.71828-1),5.5,g3,f3,0.005,0.0001)
