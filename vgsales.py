#importing all the libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#load the csv file and create a dataframe

games_sales_df=pd.read_csv('vgsales.csv')
print(games_sales_df)
#print the column and null values information
print(games_sales_df.info())
# Check the column names
print(games_sales_df.columns)

games_sales_df.drop(games_sales_df[games_sales_df.Year.isnull()].index, inplace = True) #remove null value in Year of release column
games_sales_df.drop(games_sales_df[games_sales_df.Name.isnull()].index, inplace = True) #remove null value in Name column
games_sales_df.drop(games_sales_df[games_sales_df.Publisher.isnull()].index, inplace = True) #remove null value in Publisher column
games_sales_df.info()

#Convert the values contained in the Year column into integer values.

games_sales_df['Year'] = games_sales_df['Year'].astype(int)
print(games_sales_df)
print(games_sales_df['Year'].dtype)

#Find the top 10 most-sold genres of video games sold globally. 

top_genres = games_sales_df.Genre.value_counts().head(10)
print(top_genres)
plt.figure(figsize=(12,6))
#sns.barplot(x=top_genres.value_counts().index, y=top_genres.index)
plt.title("Top 10 game genres worldwide")
plt.bar(top_genres.index, top_genres)
plt.show()

#pie chart showing the top 10 genres of most-sold video games globally

plt.figure(figsize=(24,12))
plt.title("Top 10 Genre")
plt.pie(top_genres, labels=top_genres.index, autopct='%1.1f%%', startangle=180)
plt.legend(loc = 2,fontsize  = 10, bbox_to_anchor = (1, 1), ncol = 2)
plt.title("Most sold video games globally")
#plt.show()

#Create genre-wise bar plots for the total number of units sold across different regions and the world.

#Total sale every year
sales_df = games_sales_df.groupby('Year', as_index = False).sum()

x_axis = sales_df['Year']
y_axis = sales_df['Global_Sales']

plt.figure(figsize=(20,10), dpi= 60)
plt.plot(x_axis, y_axis, label = 'Sales', color = 'green')
plt.xlabel('Year')
plt.ylabel('Sales')
plt.title('Total Game Sale Each Year')
plt.legend()
#plt.show()

#Create genre-wise bar plots for the total number of units sold across different regions and the world.
na = sales_df['NA_Sales']
eu = sales_df['EU_Sales']
jp = sales_df['JP_Sales']
total = sales_df['Global_Sales']

plt.title('Sales Comparison Between Region And Global')
plt.plot(x_axis, total, label = 'Global')
plt.plot(x_axis, na, label = 'US')
plt.plot(x_axis, eu, label = 'EU')
plt.plot(x_axis, jp, label = 'JP')
plt.legend(bbox_to_anchor =(1, 1))
plt.show()

# top platforms
platform_counts = games_sales_df.Platform.value_counts()
print(platform_counts)

#pie chart for the top platforms
plt.figure(figsize=(24,12))
plt.title("Top 10 Platform Globally")
plt.pie(platform_counts, labels=platform_counts.index, autopct='%1.1f%%', startangle=180);
plt.legend(loc = 2,fontsize  = 10, bbox_to_anchor = (1, 1), ncol = 2)
#plt.show()

#top 10 publishers
top_publishers = games_sales_df.Publisher.value_counts().head(10)
print(top_publishers)
plt.figure(figsize=(12,6))
plt.xticks(rotation=75)
sns.barplot(x=top_publishers.value_counts().index, y=top_publishers.index)
plt.title("Top 10 game publishers globally")
#plt.bar( top_publishers.index,top_publishers)
#plt.show()

#What genre of video game is most popular in Japan in terms of the total number of units sold? Also, provide the total number of units sold in Japan for that genre.
total_sales_jp = games_sales_df.JP_Sales.sum()
print(total_sales_jp)
top_1000_jp = games_sales_df.sort_values('JP_Sales',ascending = False).head(1000)
print(top_1000_jp)

# value_counts : return a Series containing counts of unique values
top_1000_jp_genre = top_1000_jp.Genre.value_counts()
print("Top games sold in Japan based on Genre",top_1000_jp_genre)

plt.figure(figsize=(24,12))
plt.title("Top 10 Genre Japan")
plt.pie(top_1000_jp_genre, labels=top_1000_jp_genre.index, autopct='%1.1f%%', startangle=180);
plt.legend(loc = 2,fontsize  = 10, bbox_to_anchor = (1, 1), ncol = 2)
plt.show()