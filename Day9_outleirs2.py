#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns


# In[46]:


#Create aa sample dataset that contains the data[300,304,308....] 95 elements and [12000,13000,18000,21000,20000]
df = pd.DataFrame({
        'CustomerID':[x for x in range(1,101)],
    'MonthlySpend': [300+x*4 for x in range(95)]+[12000,13000,18000,21000,20000]
})
df.head()


# In[33]:


q1 = np.quantile(df['MonthlySpend'],0.25)
print(f' The First qunatile is: {q1}')
q2 = np.quantile(df['MonthlySpend'],0.5)
print(f' The 2nd qunatile is: {q2}')
q3 = np.quantile(df['MonthlySpend'],0.75)
print(f' The 3rd qunatile is: {q3}')
IQR = q3-q1
print(f' The IQR  is: {IQR}')
L = q1-1.5*IQR
U = q3+1.5*IQR
print(f' The Lower Bound {L} and Upper Bound is {U}')


# In[48]:


out_liers = df[(df['MonthlySpend']<L) | (df['MonthlySpend']>U)]
out_liers


# In[50]:


No_out_liers = df[(df['MonthlySpend']>L) & (df['MonthlySpend']<U)]
No_out_liers


# In[ ]:





# In[75]:


#user defined function to take outliers 
def out_lier(x):
    q1 = np.quantile(x,0.25)
    print(f' The First qunatile is: {q1}')
    q2 = np.quantile(x,0.5)
    print(f' The 2nd qunatile is: {q2}')
    q3 = np.quantile(x,0.75)
    print(f' The 3rd qunatile is: {q3}')
    IQR = q3-q1
    print(f' The IQR  is: {IQR}')
    L = q1-1.5*IQR
    U = q3+1.5*IQR
    print(f' The Lower Bound is: {L} and Upper Bound is: {U}')
#out = df['MonthlySpend']
out_lier(df['MonthlySpend'])


# In[68]:


out_lier(df['CustomerID'])


# In[67]:


out_lier(df)


# In[ ]:





# In[ ]:





# In[ ]:




