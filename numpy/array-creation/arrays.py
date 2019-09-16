import numpy as np

# Excercise #1
a = [1, 1.2, 2, 2.2, 3, 3.2] 
arr = np.array(a)
print(arr)

# Excercise #2
aran = np.arange(-2,2,0.2,dtype='f8')
print(aran)

# Excercise #3
floatarr = np.linspace(0.5,1.5,num=11)
print(floatarr)

# Excercise #4
string = 'ABCDEFSA'
arr = np.array(string,dtype='c')
print(arr)
