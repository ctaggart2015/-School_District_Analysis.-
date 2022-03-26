#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Sort and show top five schools.
top_schools = per_school_summary_df.sort_values(["% Overall Passing"], ascending=False)

top_schools.head()


# In[2]:


# Sort and show top five schools.
bottom_schools = per_school_summary_df.sort_values(["% Overall Passing"], ascending=True)

bottom_schools.head()


# In[3]:


class Cat:
    def __init__(self, name):
        self.name = name


# In[4]:


first_cat = Cat('Felix')
print(first_cat.name)


# In[5]:


second_cat.name


# In[6]:


class Dog:
    def __init__(self, name, color, sound):
        self.name = name
        self.color = color
        self.sound = sound

    def bark(self):
        return self.sound + ' ' + self.sound


# In[7]:


first_dog = Dog('Fido', 'brown', 'woof!')
print(    first_dog.name)
print(first_dog.color)
first_dog.bark()


# In[8]:


df.head()


# In[ ]:




