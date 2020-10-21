import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from matplotlib import pyplot as plt

filename="Delivery Fleet Data.csv"
Dataframe=pd.read_csv(filename, sep='\t')
print(Dataframe)
f1= Dataframe.iloc[:,1].values
f2= Dataframe.iloc[:, 2].values
X=np.array(list(zip(f1,f2)))
plt.style.use('ggplot')
plt.rcParams['figure.figsize']=(12,7)
plt.scatter(X[:,0],X[:,1],c='black', label='True Position')
plt.show()
print(X)
kmeans = KMeans(n_clusters=4)
kmeans.fit(X)
print(kmeans.cluster_centers_)
print(kmeans.labels_)
plt.scatter(X[:,0],X[:,1], c=kmeans.labels_, cmap='rainbow')
plt.scatter(kmeans.cluster_centers_[:,0] ,kmeans.cluster_centers_[:,1],s=200, color='black',marker="*")
plt.show()