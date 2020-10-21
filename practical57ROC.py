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

kfold=KFold(n_splits=10)
model=LogisticRegression()

scoringMethod='roc_auc'
results=cross_val_score(model,x,y,cv=kfold,scoring=scoringMethod)
print("Logloss: %.3f(%.3f)"%(results.mean()*100,results.std()*100))