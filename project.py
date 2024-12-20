#!/usr/bin/env python
# coding: utf-8

# # EDA for ULTRA MARATHON RUNNING

# In[1]:


# importing libraries


# In[2]:


import pandas as pd
import numpy as np
import seaborn as sns


# In[3]:


df = pd.read_csv("TWO_CENTURIES_OF_UM_RACES.csv")


# # Checking the data

# In[4]:


df.head(10) # cheaking first 10 observation


# In[5]:


df.tail(10) # cheaking last 10 observation


# In[6]:


df.info()


# In[7]:


df.dtypes # checking datatypes of all columns


# In[8]:


df.describe()


# # As you can see the decribe function does not give us information that we need as it not valid here

# In[9]:


df.shape # checking rows and cloumns


# In[10]:


# Adjust display options to show all unique values
pd.set_option('display.max_seq_items', None)  # Show full sequences for long lists


# In[11]:


df['Event name'].unique() # As we cannot see the whole list we are using list below


# In[12]:


unique_values_list = list(df['Event name'].unique())
print(unique_values_list)


# # now we check for all the races done in India

# In[13]:


filtered_df = df[df['Event name'].str.contains(r'\(IND\)', na=False)]

filtered_df


# # cleaning the columns as per requirements

# In[14]:


#filtered_df['Event distance/length'] = filtered_df['Event distance/length'].str.split('km').str.get(0)


# In[15]:


#filtered_df['Event distance/length'] = filtered_df['Event distance/length'].str.split('Km').str.get(0)


# In[16]:


#filtered_df['Event distance/length'] = filtered_df['Event distance/length'].str.split('mi').str.get(0)


# In[17]:


#filtered_df['Event distance/length'] = filtered_df['Event distance/length'].str.split('hr').str.get(0)


# In[18]:


#filtered_df['Event distance/length'] = filtered_df['Event distance/length'].str.split('h').str.get(0)


# In[19]:


filtered_df['Athlete performance'] = filtered_df['Athlete performance'].str.split(' ').str.get(0)


# In[20]:


filtered_df['Athlete club'] = filtered_df['Athlete club'].str.split('*').str.get(-1)


# In[21]:


filtered_df['Athlete age category'] = filtered_df['Athlete age category'].str.split('M').str.get(-1)


# In[22]:


filtered_df['Athlete age category'] = filtered_df['Athlete age category'].str.split('W').str.get(-1)


# In[23]:


filtered_df['Athlete age category'] = filtered_df['Athlete age category'].str.split('U').str.get(-1)


# In[24]:


filtered_df = filtered_df.dropna() # Here we are dropping all the null values in the dataframe


# In[25]:


filtered_df


# In[26]:


filtered_df2 = filtered_df.drop(['Athlete club','Athlete year of birth','Athlete country'], axis = 1)


# In[27]:


filtered_df2


# In[28]:


filtered_df2.isna().sum() # now all the null values has been removes and we have the requried data we need


# In[29]:


filtered_df2[filtered_df2.duplicated() == 1] #chhecking for duplicates


# # As we cannot see "1" anyhwere in the dataframe there is no duplicate

# In[30]:


filtered_df2.reset_index(drop = True) # ressting the index of all observation from 0 to EOL


# # Here we can see we have obsevation that starts from 0 and ends at 1703

# In[31]:


filtered_df2.dtypes


# In[32]:


filtered_df2['Athlete average speed'] = filtered_df2['Athlete average speed'].astype(float)


# In[34]:


#filtered_df2['Event distance/length'] = filtered_df2['Event distance/length'].astype(int)


# In[35]:


filtered_df2['Athlete age category'] = filtered_df2['Athlete age category'].astype(int)


# In[36]:


filtered_df2.dtypes


# In[37]:


filtered_df2


# # Renaming columns for proper use

# In[47]:


df3 = filtered_df2.rename(columns = {'Year of event' : 'year',
                                          'Event dates' : 'race_date',
                                          'Event name' : 'race_name',
                                          'Event distance/length' : 'race_distance',
                                          'Event number of finishers' : 'race_number_of_finishers',
                                          'Athlete performance' : 'athlete_performance',
                                          'Athlete gender' : 'athlete_gender',
                                          'Athlete age category' : 'athlete_age',
                                          'Athlete average speed' : 'athlete_avg_speed',
                                          'Athlete ID' : 'athlete_id'
                                          
                                          
    
    
    
    
    
    
    
})


# In[48]:


df3.head()


# # Chart and graph

# In[64]:


df3['year'].unique()


# In[62]:





# In[63]:


sns.histplot(df3['athlete_gender'])


# In[ ]:


#here we can see that comparison between male and female ran in marathons from 1982 to 2022


# In[68]:


sns.histplot(df3, x = 'year' , y = 'athlete_age')


# # Here we can see that most of the particiapants are grom and after the year 2010

# In[69]:


sns.histplot(df3, x = 'year' , hue = 'athlete_age')


# # Here we can say that most he the praticipants are from age 23 and 35

# # Differece in speed for male and female in all race types

# In[91]:


df3.groupby(['race_distance','athlete_gender'])['athlete_avg_speed'].mean()


# In[92]:


# what age group are best in races


# In[ ]:




