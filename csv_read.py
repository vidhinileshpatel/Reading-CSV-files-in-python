import pandas as pd
# pd acts as alias for pandas

# df is the name of the data frame that we make using pandas.
df = pandas.read_csv('Enter your file name along with the entire path.')
print(df)   # view the data frame, to see the contents.

# info() gives the information about the data, its data types, number of columns, memory usage, number of entries
df.info()
