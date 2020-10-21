import pandas as pd

from sklearn.preprocessing import Normalizer
from numpy import set_printoptions

filename="ML DATA/indians-diabetes.data.csv"
hnames=['preg','plas','pres','skin','test','mass','pedi','age','class']
dataframe=pd.read_csv(filename,names=hnames)

array=dataframe.values

x=array[:,0:8]
y=array[:,8]


scaler=Normalizer()
normalizedX=scaler.fit_transform(x)

print(normalizedX[0:30,:])