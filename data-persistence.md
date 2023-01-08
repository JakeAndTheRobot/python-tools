## pickle

```python
import pickle

# some data to save
data = {'a': [1, 2.0, 3, 4+6j],
        'b': ('string', u'Unicode string'),
        'c': None}

# open a file to save the data
with open('data.pickle', 'wb') as f:
    # save the data to the file
    pickle.dump(data, f)

# open a file to load the data from
with open('data.pickle', 'rb') as f:
    # load the data from the file
    data = pickle.load(f)

# print the data to the console
print(data)
```

## json
```python
import json

# some data to save
data = {'a': [1, 2.0, 3, 4+6j],
        'b': ('string', u'Unicode string'),
        'c': None}

# convert the data to a JSON string
json_data = json.dumps(data)

# open a file to save the data
with open('data.json', 'w') as f:
    # save the JSON string to the file
    f.write(json_data)

# open a file to load the data from
with open('data.json', 'r') as f:
    # load the JSON string from the file
    json_data = f.read()

# convert the JSON string back to Python data
data = json.loads(json_data)

# print the data to the console
print(data)
```
## sqlite3
```python
import sqlite3

# connect to the database
conn = sqlite3.connect('data.db')

# create a table
conn.execute('''CREATE TABLE data (key text, value text)''')

# add some data
conn.execute("INSERT INTO data VALUES ('a', '1')")
conn.execute("INSERT INTO data VALUES ('b', '2')")

# commit the changes
conn.commit()

# retrieve the data
cursor = conn.execute("SELECT * FROM data")
for row in cursor:
    print(row)

# close the connection
conn.close()
```
## shelve
```python
import shelve

# some data to save
data = {'a': [1, 2.0, 3, 4+6j],
        'b': ('string', u'Unicode string'),
        'c': None}

# open a shelve file to save the data
with shelve.open('data.shelve') as s:
    # save the data to the shelve file
    s['data'] = data

# open a shelve file to load the data from
with shelve.open('data.shelve') as s:
    # load the data from the shelve file
    data = s['data']

# print the data to the console
print(data)
```
## h5py
```python
import h5py

# some data to save
data = {'a': [1, 2.0, 3, 4+6j],
        'b': ('string', u'Unicode string'),
        'c': None}

# create an HDF5 file to save the data
with h5py.File('data.hdf5', 'w') as f:
    # save the data to the HDF5 file
    for key, value in data.items():
        f[key] = value

# open the HDF5 file to load the data from
with h5py.File('data.hdf5', 'r') as f:
    # load the data from the HDF5 file
    data = {key: value[()] for key, value in f.items()}

# print the data to the console
print(data)
```
## csv
```python
import csv

# some data to save
data = [['a', 1], ['b', 2], ['c', 3]]

# open a file to save the data
with open('data.csv', 'w', newline='') as f:
    # create a CSV writer
    writer = csv.writer(f)
    
    # write the data to the file
    for row in data:
        writer.writerow(row)

# open a file to load the data from
with open('data.csv', 'r', newline='') as f:
    # create a CSV reader
    reader = csv.reader(f)
    
    # load the data from the file
    data = list(reader)

# print the data to the console
print(data)
```
## pandas
```python
import pandas as pd

# some data to save
data = {'a': [1, 2, 3], 'b': [4, 5, 6]}

# create a pandas DataFrame from the data
df = pd.DataFrame(data)

# save the DataFrame to an Excel file
df.to_excel('data.xlsx', index=False)

# open the Excel file to load the data from
df = pd.read_excel('data.xlsx')

# print the data to the console
print(df)
```
## pyarrow
```python
import pyarrow as pa
import pyarrow.parquet as pq

# some data to save
data = {'a': [1, 2, 3], 'b': [4, 5, 6]}

# create a pandas DataFrame from the data
df = pd.DataFrame(data)

# convert the DataFrame to a PyArrow Table
table = pa.Table.from_pandas(df)

# save the Table to a Parquet file
pq.write_table(table, 'data.parquet')

# open the Parquet file to load the data from
table = pq.read_table('data.parquet')

# convert the Table to a pandas DataFrame
df = table.to_pandas()

# print the data to the console
print(df)
```
