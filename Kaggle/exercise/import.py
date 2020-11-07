import math as mt
import numpy as nm


id=nm.random.randint(low=1,high=20,size=10)
print(id)
print(id+5)
print(id<=10)


lis=[[1,2,3,4,5],[6,7,8,9,0]]
nuAray=nm.asarray(lis)
print(lis,nuAray)
print(nuAray[1,3],lis[1][-1])
