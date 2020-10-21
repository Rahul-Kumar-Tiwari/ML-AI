import numpy as np
import pandas as pd


s=pd.Series([1,3,5.0,np.nan,15,7,8])
print(s)


dates=pd.date_range('20190101',periods=6,freq="D")
print(dates)
print(dates[0])

print(np.random.randn(6,4))

df=pd.DataFrame(np.random.randn(6,4),index=dates,columns=["A","B","C","D"])
print(df)

print("Headings in Dataframe:",df.columns)
print("Row Heading in dataframe:",df.index)
print("Values in Dataframe:",df.values)

df2=pd.DataFrame({'A':1.0,
      'B':pd.Timestamp("20190102"),
      'C':pd.Series(1,index=list(range(4)),dtype='float64'),
      'D':np.array([3]*4, dtype='int64'),
      'E':pd.Categorical(["test",'train','train','test'],categories=['test','train']),
      'F':'foo'})
print(df2)

print(df2.dtypes)
print(df.head())
print(df.tail(3))
print(df.sample(3))
print(df.describe(include="all"))       #include = all for selecting text columns

print(df.T)       #For Transpose

print("\n\n Original values:\n",df)
print("\n\n ndf.sort_index(axis=1,ascending=False): \n")
print(df.sort_index(axis=1,ascending=False))

print(df.sort_index(axis=0,ascending=False))

print("original values:\n",df)
print("Sorted values:\n",df.sort_values(by='B',ascending=True))


print(df.A)
print()
print(df['A'])

print(df['2019-01-01':"2019-01-03"])

print(df[0:3])
print(df['20190101':"20190103"])

print(df.loc[dates[0]])
print("ggg")

print(df.loc[:,['A','B']])
print(df.loc['20190101':"20190104",['A','B']])

print(df.loc["20190104",['C','D']])

print(df.loc[dates[0],'A'])
print(df.at[dates[0],'A'])          #at compute faster than loc
print(df.iloc[3])
print("hello")
print(df.iloc[3:5,0:2])

print(df.iloc[[1,2,4],[0,2]])

print(df.iloc[1:3,:])

print(df.iloc[:,1:3])

print(df.iloc[1,1])

print(df.iat[1,1])      #iat compute faster than iloc

#Boolean Indexing

print(df.A)

print("\n\n")
print(df.A>0)

print("\n\n\n")
print(df[df.A>0])
print("\n\n\n")
print(df['B'][df.A>0])
