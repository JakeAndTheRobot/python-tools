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

## Data Structures

```python
# create a Series from a list
s = pd.Series([1, 3, 5, np.nan, 6, 8])

# create a DataFrame from a NumPy array
df = pd.DataFrame(np.random.randn(6, 4))

# create a DataFrame from a dictionary
df = pd.DataFrame({'A': 1.,
                   'B': pd.Timestamp('20230101'),
                   'C': pd.Series(1, index=list(range(4)), dtype='float32'),
                   'D': np.array([3] * 4, dtype='int32'),
                   'E': pd.Categorical(["test", "train", "test", "train"]),
                   'F': 'foo'})
```

## DataFrame Operations

```python
# view the head of a DataFrame
df.head()

# view the tail of a DataFrame
df.tail(3)

# display the index, columns, and the underlying NumPy data
df.index
df.columns
df.values

# describe the statistics of a DataFrame
df.describe()

# transpose the DataFrame
df.T

# sort the DataFrame by a column
df.sort_values(by='column_name')

# slice the DataFrame by column
df['A']

# slice the DataFrame by row
df[0:3]

# slice the DataFrame by row and column
df.iloc[0:3, 0:2]

# filter the DataFrame by a column value
df[df['A'] > 0]

# group the DataFrame by a column and apply a function
df.groupby('A').sum()
```

## Series Operations

```python
# slice the Series by index
s[0:3]

# slice the Series by label
s['a':'c']

# filter the Series by a value
s[s > 0]

# apply a function to the Series
s.apply(lambda x: x * 2)
```
