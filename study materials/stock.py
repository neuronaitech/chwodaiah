import pandas as pd
import matplotlib.pyplot as plt
k=pd.read_csv('kk.csv')
k['pr']=k['High']*k['Low']
k['density']=k['High']+k['Low']
k['data']=k['High']-k['Low']
k['population']=k['High']+k['Low']
k.to_datetime(k.Series(['05/23/2005']), format="%m/%d/%Y")
k.describe()
k.values
k.T
k.values[0]
k.iloc[:3,:2]
k.iloc[0,2]=500000
k.ix[:2,:'density']
print("iloc[:,:3]",k.iloc[:,:3])
k[1:10]
k=k.drop('pr',axis=1)
k.plot(kind='bar')
plt.scatter(k.High,k.Low,color='r')
plt.show()
