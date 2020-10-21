from pandas import read_csv
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression

filename="ML Data/housing.csv"
hnames=['CRIM','ZN','INDUS','CHAS','NOX','RM','AGE','DIS','RAD','TAX','PTRATIO','B','LSTAT','MEDV']
dataframe=read_csv(filename,names=hnames)
array=dataframe.values

x=array[:,0:13]
y=array[:,13]

kfold=KFold(n_splits=10)
model=LinearRegression()

scoringMethod='r2'
results=cross_val_score(model,x,y,cv=kfold,scoring=scoringMethod)

print("R^2 %.3f"%(results.mean()))