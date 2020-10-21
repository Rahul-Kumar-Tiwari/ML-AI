import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import pickle
import warnings
warnings.filterwarnings(action="ignore")

filename="ML DATA/indians-diabetes.data.csv"
hnames=['preg','plas','pres','skin','test','mass','pedi','age','class']
dataframe=pd.read_csv(filename,names=hnames)

array=dataframe.values

x=array[:,0:8]
y=array[:,8]

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.33,random_state=7)

model=LogisticRegression()
model.fit(x_train,y_train)

filename='finalized_model.sav'
pickle.dump(model,open(filename,'wb'))

print('MODEL DUMPED SUCESSFULLY INTO A FILE BY PICKLE....\n......\n.....\n...')

loaded_model=pickle.load(open(filename,'rb'))
print("model loaded sucessfully from file by pickle")

result=loaded_model.score(x_test,y_test)
print(result)