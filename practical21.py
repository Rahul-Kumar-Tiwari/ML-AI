import numpy as np
x=np.array([1,2,3,4])
print(np.sum(x))
print(x.sum())


print("---sum by rows and by columns----")
x=np.array([[1,2],[3,4]])
print("x=\n",x)


print(x.sum())
print(x.sum(axis=0))      #collumn sum
print(x[:,0].sum(),x[:,1].sum())

print(x.sum(axis=1))    #row sum
print(x[0,:].sum(),x[1,:].sum())

print("----Extrema-----")
x=np.array([1,3,2])
print(x.min())
print(x.max())

# logical operations
print(np.all([True,True,False]))
print(np.any([True,True,False]))

print("Numpy can be used for array comparasions")
a=np.zeros((10,10))
print("a=",a)

print(np.any(a!=0))
print(np.all(a==a))

a=np.array([1,2,3,2])
b=np.array([2,2,3,2])
c=np.array([6,4,4,5])
print(((a<=b)&(b<=c)).all())

print("-------Statistics:------")
x=np.array([1,2,3,1,1])
print("x.mean()=",x.mean())
print(np.median(x))
print(x.std())