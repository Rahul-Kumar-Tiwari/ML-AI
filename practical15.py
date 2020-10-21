import numpy as np
d1=np.array([[1,2],
            [3,4],
            [5,6],
            [7,8],
            [9,10],
            [11,12],
            [13,14]])

print(d1)
print(d1.shape)
print(d1.ndim)
print("loop printing",d1[::,1:3:1])
for i in range(len(d1)):
    print("loop printing")
print("d1[::2,0]=",d1[::2,0])
print("d1[::2]= \n",d1[::2])
print(d1[1::2,1])
print(d1[1::3,0])
print(d1[...,1])

