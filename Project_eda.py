# -*- coding: utf-8 -*-



import pandas as pd
import numpy as np


df = pd.read_csv("/Users/mac/Documents/Project 1/SAMPLEMIODATA.csv")

df.head()


df.tail()

df.info()


df.describe()


df.isnull().sum()

#no missing values found here


df.dtypes

df['BillDate'] = pd.to_datetime(df['BillDate'],errors='coerce')

df.dtypes


df.drop_duplicates(inplace=True)

import matplotlib.pyplot as plt


import pandas as pd
import seaborn as sns

numeric_df = df.select_dtypes(include=['number'])
print(numeric_df)


numeric_columns = numeric_df.columns.tolist()
print("List of numeric columns:")
print(numeric_columns)


mean = df[numeric_columns].mean()
print("Mean Values:",mean)

# Median
median = df[numeric_columns].median()
print("Median Values:",median)

# Mode
mode = df[numeric_columns].mode().iloc[0]
print("\nMode Values:",mode)

#Second Moment Business Decision

#variance
variance = df[numeric_columns].var()
print("Variance:", variance)

#standard deviation
std_dev = df[numeric_columns].std()
print("Standard Deviation:", std_dev)

#range
range_df= df[numeric_columns].max() - df[numeric_columns].min()
print("Range:", range_df)

#Third Moment Business Decision
#skewness
skew = df[numeric_columns].skew()
print("Skewness:",skew)

# Fourth moment business decision
#kurtosis
kurt = df[numeric_columns].kurt()
print("Kurtosis:",kurt)

numeric_df.describe()


plt.figure(figsize=(10, 6))
sns.boxplot(data=numeric_df)
plt.title('Box Plot for Numeric Columns')
plt.xlabel('Columns')
plt.ylabel('Values')
plt.show()

#Outlier Treatment
import numpy as np
from scipy import stats

numeric_df.shape

IQR = df[numeric_columns].quantile(0.75) - df[numeric_columns].quantile(0.25)


IQR = df[numeric_columns].quantile(0.75) - df[numeric_columns].quantile(0.25)

lower_limit = df[numeric_columns].quantile(0.25) - (IQR * 1.5)
upper_limit = df[numeric_columns].quantile(0.75) + (IQR * 1.5)

df1= pd.DataFrame(np.where(df[numeric_columns]>upper_limit, upper_limit, np.where(df[numeric_columns]<lower_limit, lower_limit, df[numeric_columns])))


plt.figure(figsize=(10, 6))
sns.boxplot(data=df1)
plt.title('Box Plot for Numeric Columns')
plt.xlabel('Columns')
plt.ylabel('Values')
plt.show()

plt.boxplot(df1)





plt.figure(figsize=(10, 6))
sns.boxplot(data=numeric_df)
plt.title('Box Plot for Numeric Columns')
plt.xlabel('Columns')
plt.ylabel('Values')
plt.show()


#First moment business decision











df['TQty'].hist()
plt.show()

df['TQty'].plot.box()
plt.show()


df['GenericName'].value_counts().plot(kind='bar')
plt.show()


# bivariate 

df.plot.scatter(x='TQty', y='TotalCost')
plt.show()


df.boxplot(column='TotalCost', by='GenericName')
plt.show()

df[numeric_df].corr()

# multivariate
import seaborn as sns




import seaborn as sns
sns.heatmap(df, annot=True)
plt.show()


# number of unique drugs quantity TOP 10 drugs used 

number_of_drugs_quantity = df['GenericName'].value_counts().reset_index()

print(number_of_drugs_quantity)

number_of_drugs_quantity.head(10)

number_of_drugs_quantity.tail(10)

top_generics=df.groupby('GenericName')['NetSales'].sum().sort_values(ascending=False).head(10)

plt.figure(figsize=(10, 6))
number_of_drugs_quantity.plot(kind='bar', color='skyblue')
plt.xlabel('Generic Name')
plt.ylabel('NetSales')
plt.title('Top 10 Generic Medicines by Net Sales')
plt.xticks(rotation=45)
plt.show()

# we can see sodium Chloride .9 percent count is 10293 which is 12.1 percent of total quantity sold or used ,
#and pantaprazole 40 mg injection 3296 subsquently important quantity used or sold in hospital so its important drug




# 
plt.pie(number_of_drugs_quantity['count'], labels=number_of_drugs_quantity['GenericName'],autopct='%1.1f%%')
plt.show

# we can say 12.1 percent SODIUM CHLOride 0.9 is used then pentaprazole 40 mg then multiple electrolytes used


#  Total Cost of medicine  top 10 
top_totalcost=df.groupby('GenericName')['TotalCost'].sum().reset_index().nlargest(10 , 'TotalCost')

top_totalcost=df.groupby('GenericName')['TotalCost'].sum().sort_values(ascending=False).head(10)

plt.figure(figsize=(10, 6))
top_totalcost.plot(kind='bar', color='skyblue')
plt.xlabel('Generic Name')
plt.ylabel('TotalCost')
plt.title('Top 10 Generic Medicines by TotatCost')
plt.xticks(rotation=45)
plt.show()






#  we can see Top 10 NetSales of medicine 
# Meropenem 1 GM INJ sales is very high its an important for sales point of view

Total_Sales=df.groupby('GenericName')['NetSales'].sum().reset_index().nlargest(10, 'NetSales')
print(Total_Sales)

Total_Sales=df.groupby('GenericName')['NetSales'].sum().reset_index().nsmallest(10, 'NetSales')
print(Total_Sales)


top_generics=df.groupby('GenericName')['NetSales'].sum().sort_values(ascending=False).head(10)

plt.figure(figsize=(10, 6))
top_generics.plot(kind='bar', color='skyblue')
plt.xlabel('Generic Name')
plt.ylabel('NetSales')
plt.title('Top 10 Generic Medicines by Net Sales')
plt.xticks(rotation=45)
plt.show()


bottom_generics=df.groupby('GenericName')['NetSales'].sum().sort_values(ascending=False).tail(10)

plt.figure(figsize=(10, 6))
bottom_generics.plot(kind='bar', color='skyblue')
plt.xlabel('Generic Name')
plt.ylabel('NetSales')
plt.title('Bottom 10 Generic Medicines by Net Sales')
plt.xticks(rotation=45)
plt.show()









# we can see lowest sales of generic medicine which are in the list and we can see the o sales of medicine 




# total cost vs Netsales  scattter plot

plt.scatter(x=df['TotalCost'] ,y =df['NetSales'],color="yellow")
plt.title("total cost vs Netsales")
plt.xlable("TotalCost")
plt.ylable("NetSales")
plt.show()



plt.bar(Total_Sales['GenericName'],Total_Sales['NetSales'])


# Total quantity drugwise 
df.groupby('GenericName')['TQty'].sum().reset_index().nlargest(10, 'TQty')



#
df.groupby(['BillDate','GenericName',])['TQty'].sum().reset_index().nlargest(10, 'TQty')

sales=df.groupby(['GenericName','NetSales'])['TQty'].sum().reset_index()
top_sales = sales.sort_values(by ='NetSales' , ascending = False)

print(top_sales)

#we can see the highest sales product is for 100620 ruppes that is human Albumin INjection

top_sales.head(5)


#  Top 10 Generic Medicines by MRP


mrp=df.groupby(['NetSales','GenericName'])['MRP'].sum().reset_index()
print(mrp)
top_mrp = mrp.sort_values(by ='MRP' , ascending = False).head(10)


plt.figure(figsize=(10, 6))
top_mrp.plot(kind='bar', color='skyblue')
plt.xlabel('Generic Name')
plt.ylabel('MRP')
plt.title('Top 10 Generic Medicines by MRP')
plt.xticks(rotation=45)
plt.show()





# Sales Date wise
salesbydate=df.groupby(['GenericName','BillDate'])['NetSales'].sum().reset_index()
salesbydate

top_sale=salesbydate.sort_values(by = 'BillDate' , ascending=False)

top_sales




# 



df['BillDate'] = pd.to_datetime(df['BillDate'])
df.set_index('BillDate', inplace=True)

df.reset_index(inplace=True)
df.info()

# Plotting the time series data
plt.figure(figsize=(10, 6))
plt.plot(df.index, df['NetSales'], marker='o', linestyle='-', color='y', label='NetSales')

# Add labels and title
plt.xlabel('BillDate')
plt.ylabel('NetSales')
plt.title('BillDate vs NetSales')
plt.legend()

# Display the plot
plt.tight_layout()
plt.grid(True)
plt.show()



# Plotting the scatter plot
plt.figure(figsize=(10, 6))
plt.scatter(df.index, df['NetSales'], color='y', label='NetSales', alpha=0.7)

# Add labels and title
plt.xlabel('BillDate')
plt.ylabel('NetSales')
plt.title('Scatter Plot of BillDate vs NetSales')
plt.legend()

# Display the plot
plt.tight_layout()
plt.grid(True)
plt.show()

# Plotting the scatter plot  Monthwise
plt.figure(figsize=(10, 6))
plt.scatter(df['Month'], df['NetSales'], color='b', alpha=0.7)

# Add labels and title
plt.xlabel('Month')
plt.ylabel('NetSales')
plt.title('Scatter Plot of NetSales vs Month')

# Display the plot
plt.tight_layout()
plt.grid(True)
plt.show()







total_qty_sold = df['TQty'].sum()

total_qty_returned = df[df['TQty'] < 0]['TQty'].sum()


return_rate = abs(total_qty_returned) / total_qty_sold

print(f"Total Quantity Sold: {total_qty_sold}")
print(f"Total Quantity Returned: {total_qty_returned}")
print(f"Return Rate: {return_rate:.2%}")


returns_df = df[df['TQty'] < 0]

print(returns_df)

returns_grouped = returns_df.groupby('GenericName')['TQty'].sum().reset_index()

returns_grouped_sorted = returns_grouped.sort_values(by='GenericName', ascending=True)

print(returns_grouped_sorted)


returns_grouped['TQty'] = returns_grouped['TQty'].abs()
plt.figure(figsize=(8, 8))
plt.pie(returns_grouped['TQty'], labels=returns_grouped['GenericName'], autopct='%1.1f%%', startangle=140)
plt.title('Percentage of Returns by Medicine')
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.show()





#Quantity Sales Per Month

df['month'] = pd.to_datetime(df['BillDate'], format='%d/%m/%Y').dt.strftime('%b')
df


df.groupby('GenericName')['month'].sum().reset_index().nlargest(10 ,'TQty')


salesbydate=df.groupby(['GenericName','month'])['NetSales'].sum().reset_index()

top_sales = salesbydate.sort_values(by ='month' , ascending = False)


top_sales.head(10)


df.info()

# Sales by usage of drug Category

salesbycategory=df.groupby('SubCategoryL3')['NetSales'].sum().reset_index().nlargest(10 ,'NetSales')

salesbycategory
top_sales1 = salesbycategory.sort_values(by ='NetSales' , ascending = False).head(10)

top_sales1.head(10)






#   is is seen Anti -Infective netsales is high  compared to other category 


#Correlation Matrix Heatmap


correlation_matrix = df[['TQty', 'UCPwithoutGST', 'PurGSTPer', 'MRP', 'TotalCost','TotalDiscount','NetSales','ReturnMRP']].corr()
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
plt.title('Correlation Heatmap for Numerical Columns')
plt.show()




