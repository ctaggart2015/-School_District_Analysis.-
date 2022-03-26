#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Create a grade level DataFrames.
ninth_graders = school_data_complete_df[(school_data_complete_df["grade"] == "9th")]

tenth_graders = school_data_complete_df[(school_data_complete_df["grade"] == "10th")]

eleventh_graders = school_data_complete_df[(school_data_complete_df["grade"] == "11th")]

twelfth_graders = school_data_complete_df[(school_data_complete_df["grade"] == "12th")]


# In[2]:


# Group each grade level DataFrame by the school name for the average math score.
ninth_grade_math_scores = ninth_graders.groupby(["school_name"]).mean()["math_score"]

tenth_grade_math_scores = tenth_graders.groupby(["school_name"]).mean()["math_score"]

eleventh_grade_math_scores = eleventh_graders.groupby(["school_name"]).mean()["math_score"]

twelfth_grade_math_scores = twelfth_graders.groupby(["school_name"]).mean()["math_score"]


# In[3]:


# Group each grade level DataFrame by the school name for the average reading score.
ninth_grade_reading_scores = ninth_graders.groupby(["school_name"]).mean()["reading_score"]

tenth_grade_reading_scores = tenth_graders.groupby(["school_name"]).mean()["reading_score"]

eleventh_grade_reading_scores = eleventh_graders.groupby(["school_name"]).mean()["reading_score"]

twelfth_grade_reading_scores = twelfth_graders.groupby(["school_name"]).mean()["reading_score"]


# In[4]:


# Combine each grade level Series for average math scores by school into a single DataFrame.
math_scores_by_grade = pd.DataFrame({
               "9th": ninth_grade_math_scores,
               "10th": tenth_grade_math_scores,
               "11th": eleventh_grade_math_scores,
               "12th": twelfth_grade_math_scores})

math_scores_by_grade.head()


# In[5]:


# Combine each grade level Series for average reading scores by school into a single DataFrame.
reading_scores_by_grade = pd.DataFrame({
              "9th": ninth_grade_reading_scores,
              "10th": tenth_grade_reading_scores,
              "11th": eleventh_grade_reading_scores,
              "12th": twelfth_grade_reading_scores})

reading_scores_by_grade.head()


# In[6]:


# Format each grade column.
  math_scores_by_grade["9th"] = math_scores_by_grade["9th"].map("{:.1f}".format)

  math_scores_by_grade["10th"] = math_scores_by_grade["10th"].map("{:.1f}".format)

  math_scores_by_grade["11th"] = math_scores_by_grade["11th"].map("{:.1f}".format)

  math_scores_by_grade["12th"] = math_scores_by_grade["12th"].map("{:.1f}".format)

  # Make sure the columns are in the correct order.
  math_scores_by_grade = math_scores_by_grade[
                 ["9th", "10th", "11th", "12th"]]

  # Remove the index name.
  math_scores_by_grade.index.name = None
  # Display the DataFrame.
  math_scores_by_grade.head()


# In[7]:


# Format each grade column.
  reading_scores_by_grade["9th"] = reading_scores_by_grade["9th"].map("{:,.1f}".format)

  reading_scores_by_grade["10th"] = reading_scores_by_grade["10th"].map("{:,.1f}".format)

  reading_scores_by_grade["11th"] = reading_scores_by_grade["11th"].map("{:,.1f}".format)

  reading_scores_by_grade["12th"] = reading_scores_by_grade["12th"].map("{:,.1f}".format)

  # Make sure the columns are in the correct order.
  reading_scores_by_grade = reading_scores_by_grade[
                 ["9th", "10th", "11th", "12th"]]

  # Remove the index name.
  reading_scores_by_grade.index.name = None
  # Display the data frame.
  reading_scores_by_grade.head()


# In[ ]:




