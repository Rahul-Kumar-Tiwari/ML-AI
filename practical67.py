from copy import deepcopy
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import warnings
warnings.filterwarnings(action="ignore")
plt.style.use('ggplot')
plt.rcParams['figure.figsize']=(12,7)

data=pd.read_csv("ML Data/KMeansData.csv")
print("Input data and Shape")
print(data.shape)
print(data.head())

f1=data['V1'].values
f2=data["V2"].values
plt.scatter(f1,f2,c='b',s=10)
plt.show()

x=np.array(list(zip(f1,f2)))

#Euclidean Distance Calculater
def eu_dist(a,b,ax=1):
    return np.linalg.norm(a-b,axis=ax)

k=3
C_x=np.random.randint(0,np.max(x)-20,size=k)
print("C_x=",C_x)

C_y=np.random.randint(0,np.max(x)-20,size=k)
print("C_y=",C_y)

c=np.array(list(zip(C_x,C_y)),dtype=np.float32)
print("Initial Centroids(Random Position) : ")
print(c)
print(c.shape)

plt.scatter(f1,f2,s=10,c='b')
plt.scatter(C_x,C_y,marker='*',s=300,c='r')
plt.show()

#To store the value of centroids when it updates
C_old=np.zeros(c.shape)
print("c=\n",c)
print("C_old\n",C_old)

print("len(x)=",len(x))

#Cluster Lables(0,1,2)
clusters=np.zeros(len(x))

#zero filled numpy array of 3000 elements
print("cluster:=",clusters)

#Error func.-Distance between new centroids and old centroids

error=eu_dist(c,C_old,None)
#loop will run till the error becomes zero
while error.all():      #error!=0
    #loop will run till the
    for i in range(len(x)):
        distances=eu_dist(x[i],c)
        cluster=np.argmin(distances)
        clusters[i]=cluster
    C_old=deepcopy(c)
    print(C_old)
    for i in range(k):
        points=[ x[j] for j in range(len(x)) if clusters[j]==i]
        c[i]=np.mean(points,axis=0)
    error=eu_dist(c,C_old)
colors=['b','c','r']
fig, ax=plt.subplots()
for i in range(k):
    points=np.array([x[j] for j in range(len(x)) if clusters[j]==i])
    ax.scatter(points[:,0],points[:,1],s=25,c=colors[i])
ax.scatter(c[:,0],c[:,1],marker="*",s=100,c='y')
print("Final Centroid: ",c)
plt.show()


from sklearn.cluster import KMeans
print("Kmeans of sklearn")
kmeans=KMeans(n_clusters=3)

data=pd.read_csv("ML Data/KMeansData.csv")
f1=data['V1'].values
f2=data['V2'].values

X=np.array(list(zip(f1,f2)))
kmeans=kmeans.fit(X)

labels=kmeans.predict(x)
print("Lables : ",labels)

centroids=kmeans.cluster_centers_
print("KMeans algo Centroid values :- \n")
print("Kmeans : Manual centroid\n",c)
print("Kmeans sklearn: centroids",centroids)
