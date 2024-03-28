#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd

# Loading the dataset
data = pd.read_csv("C:/Users/athar/Desktop/Part 1/4.Dataset/BLI_29112023224043012.csv")
print(data.columns)


# In[2]:


# Dropping unnecessary columns
columns_to_drop = ['MEASURE', 'Unit Code', 'PowerCode Code', 'Reference Period Code', 'Flags']
data.drop(columns=columns_to_drop, inplace=True)
print(data.columns)


# In[3]:


# Renaming columns for clarity
data.rename(columns={'INDICATOR': 'Indicator Code'}, inplace=True)

# Checking for missing values across the dataset
missing_values = data.isnull().sum()
print(missing_values)

# If missing values are found in 'Value', we need to decide on the strategy to handle them
# Here, we fill them with the mean of the column, but this should only be done if it makes sense contextually
if data['Value'].isnull().any():
    data['Value'].fillna(data['Value'].mean(), inplace=True)


# In[4]:


# Filtering data for the "Life Satisfaction" indicator for View 1
specific_indicator = 'Life satisfaction'
filtered_data = data[data['Indicator'] == specific_indicator]


# In[5]:


# Filtering data for each inequality measure and create separate charts for View 2
inequality_measures = filtered_data['Inequality'].unique()


# In[6]:


# Checking the column names to find the one that corresponds to employment rate
print(data.columns)


# In[7]:


# Looking for a column name that suggests it might be related to employment, such as 'Employment Rate'
# If we find such a column, we replace 'Employment_Rate_Column_Name' with the actual column name
# Then we can use this column in our visualizations
# Listing all unique indicators to check if employment-related data is present
unique_indicators = data['Indicator'].unique()
employment_related_indicators = [ind for ind in unique_indicators if 'employ' in ind.lower()]
employment_related_indicators


# In[8]:


# Filtering the dataset for the "Employment rate" indicator for View 3
employment_data = data[data['Indicator'] == 'Employment rate']

# At this point, data has been cleaned and life_satisfaction_data and employment_data are ready for visualization 


# In[9]:


import pandas as pd
import altair as alt

# Creating a bar chart
bar_chart = alt.Chart(filtered_data).mark_bar().encode(
    x=alt.X('Country:N', sort='-y'),  # Sort countries by the value in descending order
    y='Value:Q',
    color='Inequality:N',  # Color bars by 'Inequality' to add another dimension to the data
    tooltip=['Country', 'Value', 'Inequality']
).properties(
    title='Life Satisfaction Across Countries',
    width=600,
    height=400
)

# Displaying the chart
bar_chart


# In[10]:


import pandas as pd
import altair as alt

# Creating seperate bar charts
charts = []
for measure in inequality_measures:
    chart = alt.Chart(filtered_data[filtered_data['Inequality'] == measure]).mark_bar().encode(
        x=alt.X('Country:N', sort='-y'),
        y='Value:Q',
        color=alt.Color('Country:N', legend=None),  # Use color to differentiate countries
        tooltip=['Country', 'Value']
    ).properties(
        title=f'Life Satisfaction for {measure}',
        width=600
    )
    charts.append(chart)

# Combining charts horizontally
hconcat_chart = alt.hconcat(*charts)
hconcat_chart


# In[11]:


import pandas as pd
import altair as alt

# Creating a bar chart for the Employment rate
employment_chart = alt.Chart(employment_data).mark_bar().encode(
    x=alt.X('Country:N', sort='-y'),  # Sort the bars based on the employment rate values
    y='Value:Q',  # The quantitative value for the employment rate
    color=alt.Color('Inequality:N', legend=alt.Legend(title="Inequality")),  # Color by inequality
    tooltip=['Country', 'Value', 'Inequality']
).properties(
    title='Employment Rate Across Countries',
    width=600,
    height=400
)

employment_chart


# In[12]:


# Saving each chart as an HTML file
bar_chart.save('view1.html')
hconcat_chart.save('view2.html')
employment_chart.save('view3.html')

# Then, in our HTML page, we can embed these views using <iframe> tags

