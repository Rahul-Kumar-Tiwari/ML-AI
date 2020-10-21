import pandas as pd
from sklearn.decomposition import PCA


import warnings
warnings.filterwarnings("ignore")

filename="ML DATA/indians-diabetes.data.csv"
hnames=['preg','plas','pres','skin','test','mass','pedi','age','class']
dataframe=pd.read_csv(filename,names=hnames)

array=dataframe.values

x=array[:,0:8]
y=array[:,8]

pca=PCA(n_components=3)
fit=pca.fit(x)
resultx=pca.transform(x)
print("\n\n",resultx)

print("Explained Variance: %s"%fit.explained_variance_ratio_)