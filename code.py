#!/usr/bin/env python
# coding: utf-8

# In[5]:



import pandas as pd 
from matplotlib import pyplot as plt 

covid = 'covid19-pk.csv'

df = pd.read_csv(covid)
Sindh = df["Sindh"] #Blue line
Punjab = df["Punjab"]#Orange line
Bal = df["Balochistan"] #Green line
AJK = df["AJK"] #Red line
KPK = df["KPK"] #purple line
ICT = df["ICT"] #brown line
GB = df["GB"] #pink line 
plt.plot(df.Date,Sindh)
plt.plot(df.Date,Punjab)
plt.plot(df.Date,Bal)
plt.plot(df.Date,AJK)
plt.plot(df.Date,KPK)
plt.plot(df.Date,ICT)
plt.plot(df.Date,GB)
plt.xticks(['Mar 31, 2020','Apr 5, 2020', 'Apr 10, 2020' ,'Apr 15, 2020','Apr 20, 2020', 'Apr 26, 2020'], ['Mar 31, 2020','Apr 5, 2020', 'Apr 10, 2020' ,'Apr 15, 2020','Apr 20, 2020', 'Apr 26, 2020'], rotation='vertical')
plt.xlabel('Timeline')
plt.ylabel('Number of Confirmed Cases')
plt.legend(['Sindh', 'Punjab', 'Bal','AJK','KPK', 'ICT', 'GB'])
plt.show()


# In[ ]:





# In[ ]:




