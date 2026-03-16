#!/usr/bin/env python
# coding: utf-8

# # PYTHON_CASE_STUDY:
# There have been huge disasters in history, but the magnitude of the Titanic’s disaster ranks as high as the depth it sank to. So much so that subsequent disasters have always been described as “titanic in proportion” – implying huge losses.
# Anyone who has read about the Titanic, know that a perfect combination of natural events and human errors, led to the sinking of the Titanic on its fateful maiden journey from Southampton to New York on April 14, 1912.
# There have been several questions put forward to understand the cause/s of the tragedy – foremost among them is: What made it sink and even more intriguing How can a 46,000 ton ship sink to the depth of 13,000 feet in a matter of 3 hours? This is a mind boggling question indeed!
# The average age of the people (both male and female) who died in the tragedy using Using that dataset we will perform some Analysis and will draw out some insights  like finding the average age of male and females died in Titanic,Number of males and females died in each compartment.
# 
# 

# In[2]:


import pandas as pd

#Extracting data from csv file and creating dataframe based on data by pandas

df = pd.read_csv("/Users/as-mac-1352/Downloads/titanic_data.csv")


# In[2]:


df


# In[3]:


df.shape #(rows,columns)


# In[4]:


df.columns #Names of columns


# # Problem statement-1:
# 
# In this problem statement we will find the average age of males and females who died in the Titanic tragedy

# In[3]:


df.dropna()
#average age of females died in the Titanic tragedy
female_avg_age=df[["Sex","Age"]][(df["Survived"]==1) & (df["Sex"]=="female")].groupby("Sex")["Age"].mean().reset_index()

#average age of males died in the Titanic tragedy
male_avg_age=df[["Sex","Age"]][(df["Survived"]==1) & (df["Sex"]=="male")].groupby("Sex")["Age"].mean().reset_index()

#average age of females and males who died in the Titanic tragedy
avg_age=df[["Sex","Age"]][(df["Survived"]==1)].groupby("Sex")["Age"].mean().reset_index()


# In[4]:


female_avg_age


# In[5]:


male_avg_age


# In[6]:


avg_age


# # Problem statement-2:
# 
# In this problem statement we will find the number of people died or survived in each class with their genders and ages.
# 

# In[9]:


#Age column have NaN values so we are filling O instead of NaN

df["Age"]=df["Age"].fillna(0)

#Number of females survived in Titanic Tragedy
female_survival_count = df[["Age","Pclass","Survived"]][(df["Sex"]=="female") & (df["Survived"]==0)].groupby(["Pclass","Age"])["Survived"].size().reset_index()


# In[10]:


female_survival_count.Survived.sum()


# In[11]:


#Number of males survived in Titanic Tragedy
male_survival_count = df[(df["Sex"]=="male") & (df["Survived"]==0)].groupby(["Pclass","Age","Sex"])["Survived"].count().reset_index()


# In[12]:


male_survival_count.Survived.sum()


# In[13]:


male_survival_count


# In[14]:


#total Number of people died in Tragedy

died_count = df[["Age","Pclass","Survived","Sex"]][(df["Survived"]==1)].groupby(["Sex","Pclass","Age"])["Survived"].size().reset_index()


# In[15]:


##Total passengers died in Titanic Tragedy

died_count.Survived.sum()


# In[16]:


died_count


# In[17]:


#Survival count of passsengers of both sex 

survival_count = df[["Age","Pclass","Survived","Sex"]][(df["Survived"]==0)].groupby(["Sex","Pclass","Age"])["Survived"].size().reset_index()


# In[18]:


survival_count


# In[19]:


##
survival_count.Survived.sum()


# In[20]:


total_passengers = survival_count.Survived.sum() + died_count.Survived.sum()


# In[21]:


total_passengers


# In[23]:


survival_count.to_csv('output_file.csv', index=False)


# In[ ]:





# In[ ]:





# In[ ]:




