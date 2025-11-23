import pandas as pd
import numpy as np

a = pd.Series([10,30,22,18])
b = pd.Series([1,2,3,4,5])
add = a+b
sub = a-b
multi = a*b
div = a/b
print("add = ",add,"sub = ",sub,"multi =",multi,"div =",div)

dict1 = {'a':100,'b':200,'c':300}
data = pd.Series(dict1)
print(data)

list1 = [10,20,30,41]
data = pd.Series(list1)
print(data)

arr = np.array([22,33,444,5])
arr2 = pd.Series(arr)

s1 = pd.Series([10,20,30,44])
s2 = pd.Series([2,33,4,16])

vs = pd.concat([s1,s2],axis =0)
hs = pd.concat([s1,s2],axis = 1)
print("\n")
print(vs)
print("\n")
print(hs)
