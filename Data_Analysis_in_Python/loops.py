import numpy as np
# np.nan_to_num()
# handle NaN values in numpy arrays
# np.nan
# np.isnan
arr = np.array([1, 2, np.nan, 4, np.nan, ])
# removing missing values from numpy array
# remove_nan1 = arr[~np.isnan(arr)]
# remove_nan2 = arr[np.isnan(arr)]
# print(remove_nan1)
# print(remove_nan2)
# is_nan = np.isnan(arr)
# print(is_nan)  
# print (arr) 
# replace missing values with np.nan_to_num()
filled_arr = np.nan_to_num(arr, nan=0)
print(filled_arr)


