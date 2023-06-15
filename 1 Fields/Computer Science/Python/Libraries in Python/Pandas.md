# Pandas DataFrames

- **Pandas**: Python library for processing and evaluating data
  - **Installation**: `pip install pandas`

- **DataFrame**: Two-dimensional, size-mutable, tabular data structure
  - **Columns**: Named, can hold different data types
  - **Index**: Row labels for the DataFrame
  - **Operations**: Supports various data manipulation tasks (e.g., filtering, aggregation)

- **Creation**: Various methods to create DataFrames
  - **From dictionaries**: `pd.DataFrame({"col1": [1, 2], "col2": [3, 4]})`
  - **From lists**: `pd.DataFrame([{'col1': 1, 'col2': 3}, {'col1': 2, 'col2': 4}])`
  - **From CSV files**: `pd.read_csv("file.csv")`
  - **From Excel files**: `pd.read_excel("file.xlsx")`
  - **From SQL databases**: `pd.read_sql_query("SELECT * FROM table", connection)`

- **Indexing**: Selecting specific data from the DataFrame
  - **Column selection**: `df["column_name"]` or `df.column_name`
  - **Row selection**: `df.loc[index]` or `df.iloc[position]`
  - **Conditional selection**: `df[df["column_name"] > value]`

- **Manipulation**: Transforming and modifying the DataFrame
  - **Add columns**: `df["new_column"] = new_data`
  - **Drop columns**: `df.drop("column_name", axis=1, inplace=True)`
  - **Rename columns**: `df.rename(columns={"old_name": "new_name"}, inplace=True)`
  - **Change data types**: `df["column_name"].astype(new_dtype)`

- **Aggregation**: Computing summary statistics for the DataFrame
  - **Descriptive statistics**: `df.describe()`
  - **Groupby operations**: `df.groupby("column_name").agg({"agg_column": "sum"})`
  - **Pivot tables**: `pd.pivot_table(df, values="agg_column", index="row_name", columns="col_name", aggfunc="sum")`

- **Handling missing data**: Techniques to deal with missing values
  - **Drop missing**: `df.dropna(axis=0, how="any")`
  - **Fill missing**: `df.fillna(value)`

- **Merging and joining**: Combining multiple DataFrames
  - **Concatenate**: `pd.concat([df1, df2], axis=0)`
  - **Merge**: `pd.merge(df1, df2, on="key_column", how="inner")`
  - **Join**: `df1.join(df2, on="key_column", how="inner")`

- **Saving**: Exporting the DataFrame to external formats
  - **To CSV**: `df.to_csv("output.csv", index=False)`
  - **To Excel**: `df.to_excel("output.xlsx", index=False)`
  - **To SQL**: `df.to_sql("table_name", connection, if_exists="replace", index=False)`

## Example: Creating and Manipulating a Pandas DataFrame

```python
import pandas as pd

# Create a DataFrame from a dictionary
data = {"Name": ["Alice", "Bob", "Carol"],
        "Age": [30, 25, 35],
        "City": ["New York", "San Francisco", "Los Angeles"]}

df = pd.DataFrame(data)

# Add a new column
df["Country"] = "USA"

# Rename a column
df.rename(columns={"City": "Location"}, inplace=True)
```

___
Type: #microtopic 
Topics: [[Computer Science]], [[Python]], [[Libraries in Python]]