#understanding the data with visualization


#a)-univariate plots
#In this section we will look at three technique
#that you can use to understand each attribute of
#your dataset independentaly
    # 1) Univariate histogram plots
    # 2) Univariate Density plots
    # 3) Univariate Box and Whisker plots

from matplotlib import pyplot as plt
import pandas
filename="ML DATA/indians-diabetes.data.csv"
hnames=['preg','plas','pres','skin','test','mass','pedi','age','class']
df=pandas.read_csv(filename,names=hnames)
print(type(df))
df.hist()
plt.show()