#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
url = "https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2020/2020-05-05/villagers.csv"
df = pd.read_csv(url)
df.isna().sum()


# import pandas as pd
# url = "https://rw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2020/2020-05-05/villagers.csv"
# df = pd.read_csv(url)
# df.isna().sum()

# In[1]:


import pandas as pd


# In[2]:


rows, columns = df.shape


# In[3]:


print("Columns:", df.columns)


# In[4]:


print(f"Number of rows: {rows}")


# In[5]:


print(f"Number of columns: {columns}")


# In[6]:


print(df.describe())


# In[7]:


print(df.describe(include='object'))


# In[8]:


print(df.isnull().sum())


# In[9]:


print(df.info())


# The definition of "observation" is every individual data points in the dataset. In this case, "observation" refers to specific villagers.
# The definition of "variable" is every columns or features in the datase. In this case, "variable" refers to the caharaeristics of villagers, including their names, species, personality types, etc.

# In[10]:


missing_values = df.isnull().sum()


# In[11]:


print(missing_values[missing_values > 0])


# If any numeric column has missing values, the "count" reported by df.describe() for that column will be less than the total number of rows reported by df.shape. 

# In[1]:


rows, columns = df.shape


# In[2]:


DF.groupby("col1")["col2"].describe()


# In[3]:


pd.read_csv(url


# Summary of Exchanges
# 1. Dataset Overview:
# 
# Question: You asked about analyzing a Titanic dataset to understand the columns of information and the amount of data available.
# Response: I provided Python code to load the dataset, check the columns, and understand the shape of the data using pandas.
# 2. Code for Dataset Analysis:
# 
# Question: You requested code to determine the number of rows and columns in the dataset.
# Response: I provided code using df.shape to get the number of rows and columns.
# 3. Summarizing Columns:
# 
# Question: You inquired about how to provide simple summaries of the columns.
# Response: I explained using df.describe() for numeric columns, df.describe(include='object') for categorical columns, and df.info() for a general overview, including missing values.
# 4. Checking Missing and Non-Numerical Values:
# 
# Question: You asked how to check for missing values and non-numerical values in the dataset.
# Response: I provided code for checking missing values with df.isnull().sum() and identifying non-numerical columns with df.select_dtypes(include=['object']).columns.
# 5. Handling Errors with Dataset Loading:
# 
# Question: You encountered an error related to df.shape and NameError.
# Response: I advised ensuring that the dataset was loaded properly before accessing df.shape and provided a complete code example to load the dataset and check its shape.
# 6. HTTP Error 500:
# 
# Question: You encountered an HTTP 500 error while trying to load the dataset from a URL.
# Response: I suggested checking the URL, using an alternative source, or downloading the dataset manually to use a local file path.
# 7. SyntaxError:
# 
# Question: You encountered a SyntaxError: incomplete input.
# Response: I provided a checklist to ensure that the code is complete and properly formatted, including a complete example to avoid syntax errors.
# Feel free to use this summary for your homework assignment! If you need any more details or adjustments, let me know.
# 
# https://chatgpt.com/share/66e39c23-8758-8013-8726-cb693f8a9858
