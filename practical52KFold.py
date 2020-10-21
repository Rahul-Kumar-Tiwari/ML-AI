import pandas as pd
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score



import warnings
warnings.filterwarnings("ignore")

from sklearn.linear_model import LogisticRegression
filename="ML DATA/indians-diabetes.data.csv"
hnames=['preg','plas','pres','skin','test','mass','pedi','age','class']
dataframe=pd.read_csv(filename,names=hnames)

array=dataframe.values

x=array[:,0:8]
y=array[:,8]

model=LogisticRegression()
num_folds=10
kfold=KFold(n_splits=num_folds,shuffle=True)
results=cross_val_score(model,x,y,cv=kfold)

print("Result : ",results)
print( )
print("Accuracy: %.3f%% "%(results.mean()*100.0))

print( )
print("std.Deviation=%.3f"%(results.std()*100.0))