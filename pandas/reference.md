# Reference

## Reading and Writing Data

```python
# read a CSV file
df = pd.read_csv('file.csv')

# write a dataframe to a CSV file
df.to_csv('file.csv', index=False)

# read an Excel file
df = pd.read_excel('file.xlsx', sheet_name='Sheet1')

# write a dataframe to an Excel file
df.to_excel('file.xlsx', sheet_name='Sheet1', index=False)

# read a SQL database
import sqlite3
con = sqlite3.connect('database.db')
df = pd.read_sql_query('SELECT * FROM table', con)

# write a dataframe to a SQL database
import sqlite3
con = sqlite3.connect('database.db')
df.to_sql('table', con, if_exists='replace')
```

## Selecting Data

```python
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
```

## Aggregating and Grouping Data

```python
# calculate the mean of each column
df.mean()

# calculate the mean of a single column
df['column_name'].mean()

# group data by a column and calculate the mean of each group
df.groupby('column_name').mean()

# pivot table
pd.pivot_table(df, index='column_name', values='other_column_name')
```

## Visualizing Data

```python
# plot a line chart
df.plot(x='column_name_1', y='column_name_2', kind='line')

# plot a scatter plot
df.plot(x='column_name_1', y='column_name_2', kind='scatter')

# plot a bar chart
df.plot(x='column_name_1', y='column_name_2', kind='bar')

# plot a histogram
df['column_name'].plot(kind='hist')

# plot a box plot
df.plot(kind='box')
```
