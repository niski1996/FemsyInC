import itertools
import functools
import numpy as np
import math
def foo(factors,val):
    factors=factors[:]
    factors.reverse()
    for num,fac in enumerate(factors):
        factors[num] = fac*val**num
    factors.reverse()
    return functools.reduce(lambda x,y:x+y,factors)

def der(fac, num):
    li=[]
    for step in range(num):
        li.append(fac:=list(np.polyder(fac)))
    return li



def taylor_1(fac,delta,val, num):
    sum=foo(fac,val)
    li_der = der(fac,num)
    for step in range(num):
        sum+=delta**(step+1)*foo(li_der[step],val)/math.factorial(step+1)
    return sum

a=[4,12,5,54,2]
der_a = der(a,1)[0]
print(foo(a,8))
print(foo(der_a,8))
print((foo(a,9)-foo(a,7))/(2*1))