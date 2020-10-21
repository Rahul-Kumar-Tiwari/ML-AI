import warnings
warnings.filterwarnings(action="ignore")

import pandas as pd
from sklearn.model_selection import LeaveOneOut
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LogisticRegression
filename="ML DATA/indians-diabetes.data.csv"
hnames=['preg','plas','pres','skin','test','mass','pedi','age','class']
dataframe=pd.read_csv(filename,names=hnames)

array=dataframe.values

x=array[:,0:8]
y=array[:,8]

loocv=LeaveOneOut()
model=LogisticRegression()
results=cross_val_score(model,x,y,cv=loocv)

print("Result : ",results)
print( )
print( )
print("result.size: ",results.size)
print( )
print("Sum of Positive Results: %i"%(results.sum()))
print( )
print("Accuracy = %.2f%%"%(results.sum()*100/results.size))