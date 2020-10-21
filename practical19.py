import numpy as np
n4=np.array([10,-1,0,90,300,3,-6,2])
print(n4)

n4.sort()
print(n4)

n4=np.array([10,-1,0,90,300,3,-6,2])
print("n4=",n4)
print(n4.argsort())
print(n4)

for i in n4.argsort():
    print(n4[i],end=" ")

print(n4[n4.argsort()])
print("n4=",n4)

na=np.array([[1,2,3],
             [4,5,6]])

print("na= \n",na)
print(na.transpose())
print(na)

print(np.eye(6))

a=np.ones([3,3])
a=a*3
a[2,2]=4
I=np.eye(3)
b=np.dot(a,I)
print(a)
print(I)
print(b)


na=np.array([[1,2],
             [5,6]])
print("na =\n ",na)
print("-----------------------------------")
print(np.dot(na,na))

print("---------------Element wise Comparision------------")
a=np.array([1,2,3,4])
b=np.array([1,1,3,3])
print(a==b)
print(a>b)

print("---------------Array wise Comparision------------")
a=np.array([1,2,3,4])
b=np.array([2,3,4,5])
c=np.array([1,2,3,4])
print(np.array_equal(a,b))
print(np.array_equal(a,c))

print("---------------Logical operation------------")
a=np.array([1,1,0,0],dtype=bool)
b=np.array([1,0,1,0],dtype=bool)
print("a=",a)
print("b=",b)
print(np.logical_or(a,b))
print(np.logical_and(a,b))

print(np.pi)
print(np.linspace(-5,5,11))

print(np.linspace(-np.pi,np.pi,256))


j=np.arange(5)
print(2**(j+1)-j)






