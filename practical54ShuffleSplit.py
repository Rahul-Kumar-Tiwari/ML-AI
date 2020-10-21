from sklearn.model_selection import ShuffleSplit
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LogisticRegression
import warnings
warnings.filterwarnings(action="ignore")

import pandas as pd

filename="ML DATA/indians-diabetes.data.csv"
hnames=['preg','plas','pres','skin','test','mass','pedi','age','class']
dataframe=pd.read_csv(filename,names=hnames)

array=dataframe.values

x=array[:,0:8]
y=array[:,8]

test_data_size=0.33
no_of_repeatations=10

shufflesplit=ShuffleSplit(n_splits=no_of_repeatations,test_size=test_data_size)
model=LogisticRegression()
results=cross_val_score(model,x,y,cv=shufflesplit)

print(results)
print("Accuracy: %.3f"%(results.mean()*100.0))
print( )
print("Std Deviation= %.3f"%(results.std()*100.0))