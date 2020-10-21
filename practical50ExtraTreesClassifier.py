from sklearn.ensemble import ExtraTreesClassifier

import pandas as pd

import warnings
warnings.filterwarnings("ignore")

filename="ML DATA/indians-diabetes.data.csv"
hnames=['preg','plas','pres','skin','test','mass','pedi','age','class']
dataframe=pd.read_csv(filename,names=hnames)

array=dataframe.values

x=array[:,0:8]
y=array[:,8]

model=ExtraTreesClassifier()
model.fit(x,y)
scores=model.feature_importances_
print(scores)

result=list(zip(hnames,scores))
print("\n\n")
print(result)
print("\n\n")

from operator import itemgetter
print(sorted(result,key=itemgetter(1),reverse=True))