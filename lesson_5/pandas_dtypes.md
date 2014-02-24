|Name of type | Function | Base Python Equivalent |
|------------|---------|-------------------------|
|Object | The most general dtype. Will be assigned to your column if column has mixed types (numbers and strings). | String | 
|int64 | Numerical characters. 64 refers to memory allocated to hold this character. | Int. |
| float64 | Numerical characters with decimals. If a column contains numbers and NaNs, pandas will default to float64, in case your missing value has a decimal | float |
|datetime64, timedelta[ns] | Values meant to hold time data. Look into these for time series experiments | -- |

##Casting

Much like we learned in base python, we can transfer between types like so:

```python

my_value.astype("Desired type")

```

