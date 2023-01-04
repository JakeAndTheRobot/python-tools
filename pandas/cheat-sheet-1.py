# import pandas
import pandas as pd

# read a CSV file
df = pd.read_csv('file.csv')

# display the first 5 rows of the dataframe
df.head()

# display the last 10 rows of the dataframe
df.tail(10)

# select a single column
df['column_name']

# select multiple columns
df[['column_1', 'column_2']]

# select a single row
df.loc[row_index]

# select a specific cell
df.loc[row_index, 'column_name']

# select a range of rows
df[start:end]

# filter rows based on a condition
df[df['column_name'] > value]

# group data by a column and calculate the mean of each group
df.groupby('column_name').mean()

# pivot table
pd.pivot_table(df, index='column_name', values='other_column_name')

# plot a line chart
df.plot(x='column_name_1', y='column_name_2', kind='line')

# save dataframe to CSV
df.to_csv('new_file.csv', index=False)
