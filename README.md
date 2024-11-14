# Merge DataFrames

This module contains a function to merge two Pandas DataFrames on a specified column with a specified join type.

## Installation

To install this package, use the following command:

```bash
pip install git+https://github.com/laxmankusuma/merge_dataframes.git


Usage:

from merge_dataframes import merge_dataframes
import pandas as pd

df1 = pd.DataFrame({'id': [1, 2, 3], 'name': ['Alice', 'Bob', 'Charlie']})
df2 = pd.DataFrame({'id': [1, 2, 4], 'age': [24, 25, 23]})

merged_df = merge_dataframes(df1, df2, on='id', how='inner')
print(merged_df)
