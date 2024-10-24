#import the libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#Load the csv file in aa data frame

life_df=pd.read_csv('LifeExpectancy.csv')
print(life_df)
print(life_df.info())
print(life_df.columns)


#Q1. Rename some columns if they contain leading and trailing spaces (by removing spaces).
#Remove spaces from column names in Pandas by 2 methods:1.df.columns = df.columns.str.replace(' ', '') 2.df.columns = df.columns.str.replace(' ', '_')
#life_df.columns=life_df.columns.str.replace(' ','_') Adding a underscore

life_df.columns=life_df.columns.str.replace(' ','')
print(life_df.columns)

#Q2.Which columns in the dataset have missing values and how many?

#Ans 2.To count the number of NaN values in all columns of the data frame, we can use the isna() and sum() functions without specifying a column.

# Counting NaN values in all columns using isna(),sum()
nan_count = life_df.isna().sum()

print(nan_count)

#Counting NaN values in all columns using isnull()df.isnull().sum() gives the features name along with the count of null values for that particular feature.
print(life_df.isnull().sum())

#Drop all the columns from the DataFrame containing more than 15% percent of the missing values.
# Threshold for missing values (15% of total rows)
threshold = 0.15 * len(life_df)
print("15% of the data frame",threshold)

# Drop columns where the number of missing values is greater than the threshold
life_df_cleaned = life_df.dropna(thresh=len(life_df) - threshold, axis=1)

print(life_df_cleaned)
print(life_df_cleaned.isnull().sum())


life_df_filled = life_df_cleaned.fillna(life_df_cleaned.median())

print("Pinting the data frame after filling null values",life_df_filled)

print("Printing the sum of all null values in all the columns",life_df_filled.isnull().sum())
