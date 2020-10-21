from matplotlib import pyplot as plt
import pandas
filename="ML DATA/indians-diabetes.data.csv"
hnames=['preg','plas','pres','skin','test','mass','pedi','age','class']
df=pandas.read_csv(filename,names=hnames)
#kind=Density/box
df.plot(kind='density',subplots="True",layout=(3,3),sharex=False)
plt.show()