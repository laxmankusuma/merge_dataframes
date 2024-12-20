# Merge DataFrames

This module contains a function to merge two Pandas DataFrames on a specified column with a specified join type.

## Installation

To install this package, use the following command:

```bash
pip install git+https://github.com/laxmankusuma/merge_dataframes.git


Usage:

from merge_dataframes.merge_dataframes import merge_dataframes
import pandas as pd

df1 = pd.DataFrame({'id': [1, 2, 3], 'name': ['Alice', 'Bob', 'Charlie']})
df2 = pd.DataFrame({'id': [1, 2, 4], 'age': [24, 25, 23]})

merged_df = merge_dataframes(df1, df2, on='id', how='inner')
print(merged_df)


To make this code into a wheel file, follow the steps below:

pip install setuptools wheel
python setup.py bdist_wheel
This will create a dist directory containing a .whl file.

To install the .whl file created in the dist directory:

Install the .whl File: Use the following pip command to install the .whl file:
pip install /path/to/yourfile.whl
Replace /path/to/yourfile.whl with the actual path to your .whl file. For example:
pip install dist/yourfile-0.1-py3-none-any.whl
