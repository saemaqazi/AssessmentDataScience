import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#creating a dataframe by reading the csv file
#dev_df=pd.read_csv("Developers.csv")
##print(dev_df.isnull().sum())

# Filter the required columns
#df_filtered = dev_df[['Age', 'Python', 'JavaScript']]

import pandas as pd
import matplotlib.pyplot as plt

#creating a dataframe by reading the csv file
df = pd.read_csv('Developers.csv')

# Printing the first 10 entries

print(df.head())

#check for column names and null values

print(df.info())

# Q1. Create customized line plots to compare the salary variations Age-wise for Python developer with Javascript developer.

# Filter the required columns
df_filtered = df[['Age', 'Python', 'JavaScript']]

print(df_filtered)

#Q2. What can you conclude from the comparison?

print("Conclusion from the above information and below line plot is that,the salaries of python developers across all age groups is higher than the salaries of JavaScript Developers")

# Create the line plot
plt.figure(figsize=(10,6))

# Plot Python developer salaries age-wise
plt.plot(df_filtered['Age'], df_filtered['Python'], label='Python Developer', color='b', marker='o')

# Plot JavaScript developer salaries age-wise
plt.plot(df_filtered['Age'], df_filtered['JavaScript'], label='JavaScript Developer', color='m', marker='^')

# Add titles and labels
plt.title('Age-wise Salary Comparison: Python vs JavaScript Developers')
plt.xlabel('Age')
plt.ylabel('Average Annual Salary (in dollars)')
plt.legend()

# Show the plot
plt.grid(True)
plt.show()
