#Array Question 4 - Product of array
import numpy as np
 
lst = [-1,1,0,3,-3]
mul = []

for i in range(0,len(lst)):
    rem = lst[i]
    lst.pop(i)
    mullst = np.prod(lst)
    mul.append(mullst)
    lst.insert(i,rem)

print(mul)
