#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import os


# In[ ]:


raw_data_url = 'https://gist.githubusercontent.com/bobbae/b4eec5b5cb0263e7e3e63a6806d045f2/raw/279b794a834a62dc108fc843a72c94c49361b501/data.csv'
df_data = pd.read_csv(raw_data_url)


# In[ ]:


# Count total number of rows 
print(df_data.shape[0])


# In[ ]:


def isFloat(string):
    try:
        float(string)
        return True
    except ValueError:
        return False


# In[ ]:


df_numeric = df_data[df_data['Profit (in millions)'].apply(lambda x: isFloat(x))]


# In[ ]:


# Count total rows where value of profit is numeric
print(df_numeric.shape[0])


# In[ ]:


data2 = df_numeric.sort_values(by='Profit (in millions)', ascending = False)


# In[ ]:


with open(os.path.join(os.getcwd(), 'data2.json'), 'w') as outfile:
    outfile.write(data2.reset_index(drop=True).to_json(orient='records'))


# In[ ]:


# Top 20 rows with valid 'profit' numeric values
print(data2.head(20).reset_index(drop=True))


# In[ ]:




