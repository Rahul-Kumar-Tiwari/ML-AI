import pandas
import urllib.request
import numpy as np
hnames=["sepal-length","sepal-width","petal-length",'petal-width','class']
web_path=urllib.request.urlopen("https://goo.gl/QnHW4g")
dataframe=pandas.read_csv(web_path,names=hnames)
print(dataframe)
pandas.set_option("precision",2)
a=np.array(dataframe)
print(a)

# for i in range(0,len(a)):
#     if((a[i,4])=="Iris-setosa"):
#         a[i,4]=1
#     elif ((a[i,4]) == 'Iris-versicolor'):
#         a[i,4]=2
#     elif ((a[i,4]) == 'Iris-virginica'):
#         a[i,4] = 3
np_array=a[:,0:4:]
print(a[:,4:])
print(np_array)

print(np_array.shape)
print(np_array.ndim)
#print(np_array*3)

#
# print(np_array.sum())
# print(np_array.mean())
# print(np_array.std())
# print(np_array.max())
# print(np_array.min())
# print(np_array.size)
# print(np_array.dtype)
# print(np.median(np_array))
# print(np_array.sum(axis=0))
# print(np_array.sum(axis=1))
#
# print()
#
# a=np_array[:,0]
# b=np_array[:,1]
# c=np_array[:,2]
# d=np_array[:,3]
# e=np_array[:,4]
#
#
# for i in a.argsort():
#     print(a[i],b[i],c[i],d[i],e[i])
#
#
#
# import matplotlib.pyplot as plt
# plt.plot(a,b,'yH')    #r-,bo,bs,b*
#
# plt.xlabel("----sepal-length------->")
# plt.ylabel("------sepal-width------->")
# plt.axis([4.1,8.0,3.0,4.0])
#
# plt.show()
#
#
# plt.bar(a,b,label='Blue bar',color='b')
# plt.bar(c,d,label='Green bar',color='g')
# plt.show()
#
# plt.hist(e,bins=3)
# plt.show()
#
# plt.scatter(a,b,marker='v',color='r')
# plt.show()
# plt.scatter(c,d,marker='^',color='m')
# plt.show()
#
# labels="Iris-setosa",'Iris-versicolor','Iris-virginica'
# x=np.count_nonzero(e == 1)
# y=np.count_nonzero(e == 2)
# z=np.count_nonzero(e == 3)
#
# sections=[x,y,z]
# colors=['c','g','y']
#
# plt.pie(sections,labels=labels,colors=colors,
#         startangle=45
#         ,explode=(0,0,0),
#         autopct='%1.2f%%')
#
# plt.title("Pie Chart Example")
# plt.show()