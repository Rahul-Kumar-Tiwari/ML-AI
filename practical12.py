import warnings
warnings.filterwarnings(action="ignore")

from matplotlib import pyplot as plt
import pandas as pd
from pandas.plotting import scatter_matrix
import numpy

filename="ML DATA/indians-diabetes.data.csv"
hnames=['preg','plas','pres','skin','test','mass','pedi','age','class']
df=pd.read_csv(filename,names=hnames)

scatter_matrix(df)
plt.show()