import myfunctions as de
import math
def f1(y,x):
    return (y*math.log(y))/x
def f2(y,x):
    return 6-((2*y)/x)
#Question 1
de.euler(2,2.71828,f1,0.2,5)
de.euler(2,2.71828,f1,0.1,5)
de.euler(2,2.71828,f1,0.02,5)
de.euler(2,2.71828,f1,0.01,5)
#Question 2
de.euler(3,1,f2,0.22,5)
de.euler(3,1,f2,0.12,5)
de.euler(3,1,f2,0.022,5)
de.euler(3,1,f2,0.012,5)