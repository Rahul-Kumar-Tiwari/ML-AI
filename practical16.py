import numpy as np
zr=np.zeros([3,4])
print("zero filed array zr=\n",zr)

ar=np.ones([4,4])
print("1's filed array ones= \n",ar)

print(ar*4)
print(ar.dtype)

ar=np.arange(1,6)
print("ar = ",ar)
print(ar.shape)

ar[3]=16
print(ar)