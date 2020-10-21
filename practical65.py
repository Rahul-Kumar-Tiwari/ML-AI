import warnings
warnings.filterwarnings(action="ignore")

import pandas as pd
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score

filename="ML DATA/indians-diabetes.data.csv"
hnames=['preg','plas','pres','skin','test','mass','pedi','age','class']
dataframe=pd.read_csv(filename,names=hnames)

array=dataframe.values

x=array[:,0:8]
y=array[:,8]
print(x)
print(y)
kfold=KFold(n_splits=10,random_state=7)
#1) spot checking for logistic Regression

from sklearn.linear_model import LogisticRegression
model=LogisticRegression()
results=cross_val_score(model,x,y,cv=kfold)
print("validation Score for Logestic Regression : ",results.mean())

#2) spot checking for Linear Discrement Analysis(LDA)
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
model=LinearDiscriminantAnalysis()
results=cross_val_score(model,x,y,cv=kfold)
print("Validation Score for Linear Disccirment Analysis : ",results.mean())

#3) Spot checking for k-Nearest Neighbors(KNN)
from sklearn.neighbors import KNeighborsClassifier
model=KNeighborsClassifier()
results=cross_val_score(model,x,y,cv=kfold)
print("Validation Score for KNN : ",results.mean())




from sklearn.svm import SVC
model=SVC()
results=cross_val_score(model,x,y,cv=kfold)
print("Validation Score for Svm: ",results.mean())




from sklearn.naive_bayes import GaussianNB
model=GaussianNB()
results=cross_val_score(model,x,y,cv=kfold)
print("validation ",results.mean())

from sklearn.tree import DecisionTreeClassifier
model=DecisionTreeClassifier()
results=cross_val_score(model,x,y,cv=kfold)
print("Validation Score for CART Decision Tree : ",results.mean())