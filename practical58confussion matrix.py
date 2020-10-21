import pandas as pd
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import cross_val_score,train_test_split



import warnings
warnings.filterwarnings("ignore")

from sklearn.linear_model import LogisticRegression
filename="ML DATA/indians-diabetes.data.csv"
hnames=['preg','plas','pres','skin','test','mass','pedi','age','class']
dataframe=pd.read_csv(filename,names=hnames)

array=dataframe.values

x=array[:,0:8]
y=array[:,8]

test_data_size=0.33
seed=7

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=test_data_size,random_state=seed)
model=LogisticRegression()

model.fit(x_train,y_train)
predicted=model.predict(x_test)

matrix=confusion_matrix(y_test,predicted)
print(matrix)

