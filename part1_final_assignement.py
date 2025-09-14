#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import seaborn as sns
import numpy as np


# In[3]:


titanic_df = sns.load_dataset('titanic')
titanic_df


# In[6]:


titanic_df.head()


# In[4]:


titanic_df.shape


# In[5]:


titanic_df.info()


# In[ ]:





# In[18]:


titanic_df.duplicated().sum()


# - Read the file titanic.csv in the data/ folder and assign it to a dataframe called titanic.
# 
# - Does the dataframe has any missing values? If yes, how many? Assign your result to ans1a.

# In[13]:


ans1a = titanic_df.isnull().sum()
ans1a


# - Define a series, ans2a, that counts the number of males and females in the dataframe.
# 
# - How many female passengers were on the ship? Assign your result to ans2b.

# In[18]:


ans2a = pd.Series(titanic_df['sex'])
ans2b = ans2a.value_counts()
print('Number of female passengers are:',ans2b['female'])


# - What was the average fare to travel on the Titanic? Assign your result to ans4a.

# In[19]:


ans4a=titanic_df['fare'].mean()
print(f'The average fare to travel on the Titanic is:{ans4a}')


# - Define a series, ans5a, containing the letter corresponding 
# - to the port of embarkation ('C', 'Q', or 'S') in descending alphabetical order.
# 
# - Use the function sort_values().

# In[23]:


ans5a = pd.Series(titanic_df['embarked'])
ans5a.sort_values(ascending=False)


# - How many people survived the disaster? Assign your answer to ans6a.

# In[25]:


ans6a = titanic_df['survived'].value_counts()
print('Number of People survived in the disaster are:',ans6a[1])

