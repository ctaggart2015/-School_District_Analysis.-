#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Combine the data into a single dataset.
school_data_complete_df = pd.merge(student_data_df, school_data_df, on=["school_name", "school_name"])
school_data_complete_df.head()


# In[2]:


# Get the total number of students.
student_count = school_data_complete_df.count()
student_count


# In[3]:


school_data_complete_df[column].count()


# In[4]:


school_data_complete_df["Student ID"].count()


# In[5]:


# Calculate the total number of schools.
school_count = school_data_df["school_name"].count()
school_count


# In[6]:


# Calculate the total number of schools
school_count_2 = school_data_complete_df["school_name"].unique()
school_count_2


# In[7]:


# Calculate the total budget.
total_budget = school_data_df["budget"].sum()
total_budget


# In[8]:


# Calculate the average reading score.
average_reading_score = school_data_complete_df["reading_score"].mean()
average_reading_score


# In[9]:


# Calculate the average math score.
average_math_score = school_data_complete_df["math_score"].mean()
average_math_score


# In[10]:


passing_math = school_data_complete_df["math_score"] >= 70
passing_reading = school_data_complete_df["reading_score"] >= 70


# In[11]:


# Get all the students who are passing math in a new DataFrame.
passing_math = school_data_complete_df[school_data_complete_df["math_score"] >= 70]
passing_math.head()


# In[12]:


# Get all the students that are passing reading in a new DataFrame.
passing_reading = school_data_complete_df[school_data_complete_df["reading_score"] >= 70]


# In[13]:


# Calculate the number of students passing math.
passing_math_count = passing_math["student_name"].count()

# Calculate the number of students passing reading.
passing_reading_count = passing_reading["student_name"].count()


# In[14]:


# Calculate the percent that passed math.
passing_math_percentage = passing_math_count / float(student_count) * 100

# Calculate the percent that passed reading.
passing_reading_percentage = passing_reading_count / float(student_count) * 100


# In[15]:


# Calculate the students who passed both math and reading.
passing_math_reading = school_data_complete_df[(school_data_complete_df["math_score"] >= 70) & (school_data_complete_df["reading_score"] >= 70)]

passing_math_reading.head()


# In[16]:


# Calculate the number of students who passed both math and reading.
overall_passing_math_reading_count = passing_math_reading["student_name"].count()
overall_passing_math_reading_count


# In[17]:


# Calculate the overall passing percentage.
overall_passing_percentage = overall_passing_math_reading_count / student_count * 100
overall_passing_percentage


# In[18]:


# Adding a list of values with keys to create a new DataFrame.
district_summary_df = pd.DataFrame(
          [{"Total Schools": school_count,
          "Total Students": student_count,
          "Total Budget": total_budget,
          "Average Math Score": average_math_score,
          "Average Reading Score": average_reading_score,
          "% Passing Math": passing_math_percentage,
         "% Passing Reading": passing_reading_percentage,
        "% Overall Passing": overall_passing_percentage}])
district_summary_df


# In[19]:


# Format the columns.
district_summary_df["Average Math Score"] = district_summary_df["Average Math Score"].map("{:.1f}".format)

district_summary_df["Average Reading Score"] = district_summary_df["Average Reading Score"].map("{:.1f}".format)

district_summary_df["% Passing Math"] = district_summary_df["% Passing Math"].map("{:.0f}".format)

district_summary_df["% Passing Reading"] = district_summary_df["% Passing Reading"].map("{:.0f}".format)

district_summary_df["% Overall Passing"] = district_summary_df["% Overall Passing"].map("{:.0f}".format)


# In[20]:


# Reorder the columns in the order you want them to appear.
new_column_order = ["column2", "column4", "column1"]

# Assign a new or the same DataFrame the new column order.
df = df[new_column_order]


# In[21]:


Reorder the columns in the order you want them to appear.
new_column_order = ["Total Schools", "Total Students", "Total Budget","Average Math Score", "Average Reading Score", "% Passing Math", "% Passing Reading", "% Overall Passing"]

# Assign district summary df the new column order.
district_summary_df = district_summary_df[new_column_order]
district_summary_df


# In[ ]:




