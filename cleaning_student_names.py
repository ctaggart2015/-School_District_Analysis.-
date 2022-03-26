#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Add the Pandas dependency.
import pandas as pd


# In[2]:


# Files to load
student_data_to_load = "Resources/students_complete.csv"


# In[3]:


# Read the student data file and store it in a Pandas DataFrame.
student_data_df = pd.read_csv(student_data_to_load)
student_data_df.head()


# In[4]:


# Put the student names in a list.
student_names = student_data_df["student_name"].tolist()
student_names


# In[5]:


name = "Mrs. Linda Santiago"


# In[6]:


# Split the student name and determine the length of the split name.
for name in student_names:
    print(name.split(), len(name.split()))


# In[7]:


# Create a new list and use it for the for loop to iterate through the list.
students_to_fix = []

# Use an if statement to check the length of the name.
# If the name is greater than or equal to "3", add the name to the list.

for name in student_names:
    if len(name.split()) >= 3:
        students_to_fix.append(name)

# Get the length of the students whose names are greater than or equal to "3".
len(students_to_fix)


# In[8]:


# Add the prefixes less than or equal to 4 to a new list.
prefixes = []
for name in students_to_fix:
    if len(name.split()[0]) <= 4:
        prefixes.append(name.split()[0])

print(prefixes)


# In[9]:


# Add the suffixes less than or equal to 3 to a new list.
suffixes = []
for name in students_to_fix:
    if len(name.split()[-1]) <= 3:
        suffixes.append(name.split()[-1])

print(suffixes)


# In[10]:


# Get the unique items in the "prefixes" list.
set(prefixes)


# In[11]:


# Get the unique items in the "suffixes" list.
set(suffixes)


# In[12]:


# Add each prefix and suffix to remove to a list.
prefixes_suffixes = ["Dr. ", "Mr. ","Ms. ", "Mrs. ", "Miss ", " MD", " DDS", " DVM", " PhD"]


# In[13]:


student_data_df["student_name"].str.replace()


# In[ ]:


# Iterate through the "prefixes_suffixes" list and replace them with an empty space, "" when it appears in the student's name.
for word in prefixes_suffixes:
    student_data_df["student_name"] = student_data_df["student_name"].str.replace(word,"")

