#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd
import numpy as np


# In[6]:


practice_df = pd.read_csv(r"C:\Users\Vadty\OneDrive\Desktop\Desktop\Unicus\Python datasets\melbourne.csv")
practice_df


# In[7]:


practice_df.isnull().sum()


# - Above we can observe that most of the columns has null values. 
# - To work with null values we have to delete or impute nulls.
# - we can't identify how much weightage of null values in a column. 
# - So we have to take percentage in each column of null values

# In[8]:


(practice_df.isnull().sum()/len(practice_df))*100


# - Above, columns which are had null values more than 30% will be removed
# - because there not much effectiive to the dataset as they consist mostly null values

# In[ ]:





# In[9]:


practice_df_col=practice_df.loc[:,(practice_df.isnull().sum()/len(practice_df)*100)<=30]
practice_df_col


# In[10]:


practice_df_col.isnull().sum()/len(practice_df_col)*100


# - Now columns with most null values are removed.
# - now lets check for the rows null values.
# - we can observe that some of the columns still had null values but not much hence we can perform removing rows

# In[15]:


practice_df_col.isnull().sum(axis=1)


# - here we can observe some of the rows has mostly null values.
# - currently we have 18 columns if a row consist more than 3 null values then we can remove it.
# - if the data is not much effective

# In[12]:


practice_df_row=practice_df_col[practice_df_col.isnull().sum(axis=1)<=3]
practice_df_row


# - Here we can observe that all rows consist less than or equal to 3 null values.
# - we can conclude  that cleaned and removed null values
# - which columns and rows has excess null values
# - To understand which columns has most null values we can make it as percentage

# In[25]:


practice_df_row.isnull().sum()/len(practice_df_row)*100


# - here column Price has most null values we can remove it or impute.
# - we can drop records in Price column where rows are null.
# - because if price of a customer is null then the data of the person not required.
# - hence we can remove his row. According we can remove null values in Price variable.
# 

# In[30]:


practice_df_row.dropna(subset=['Price'],inplace=True)


# In[35]:


practice_df_row.isnull().sum()/len(practice_df_row)*100


# - we can observe that some of the columns still has lesser null values.
# - I imputed them with median of their appropriate column.
# - Median is less sensitive  to ouliers compared to the mean.

# In[34]:


medians = practice_df_row.median()
cleaned_df=practice_df_row.fillna(medians)
cleaned_df.isnull().sum()


# In[ ]:




