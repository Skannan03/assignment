# # NumPy aims to provide an array object that is up to 50x faster than traditional Python lists.
# #
# # The array object in NumPy is called ndarray, it provides a lot of supporting functions that make working with ndarray very easy.
# #
# # Arrays are very frequently used in data science, where speed and resources are very important.
#
# import numpy as np
# arr = np.array([1, 2, 3, 4, 5])
#
# print(arr)
# print(type(arr))
#
# arr = np.array(42)
#
# print(arr)
# # Create a 2-D array containing two arrays with the values 1,2,3 and 4,5,6:
# arr = np.array([[1, 2, 3], [4, 5, 6]])
# print(arr)
# # 3-D arrays
# # An array that has 2-D arrays (matrices) as its elements is called 3-D array.
# arr = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
# print(arr)
#
# import numpy as np
#
# arr = np.array([1, 2, 3, 4])
#
# print(arr[2] + arr[3])
# # Access 2-D Arrays
#
# arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])
#
# print('2nd element on 1st row: ', arr[0, 1])
#
# # Access 3-D Arrays
# arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
#
# print(arr[1, 1, 2])
#
#
# arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])
#
# print('Last element from 2nd dim: ', arr[1, -1])
#
# print(arr[1:5])
# print(arr[4:])
#
# arr = np.array([1, 2, 3, 4, 5, 6, 7])
#
# print(arr[:4])
#
# arr = np.array([1, 2, 3, 4, 5, 6, 7])
#
# print(arr[-3:-1])
# print(arr[1:5:2])
#
# arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
#
# print(arr[0:2, 2])
# print(arr[0:2, 1:4])
# print(arr.dtype)
# arr = np.array(['apple', 'banana', 'cherry'])
#
# print(arr.dtype)
#
# arr = np.array([1, 2, 3, 4], dtype='S')
#
# print(arr)
# print(arr.dtype)
#
# arr = np.array([1, 2, 3, 4], dtype='i4')
#
# print(arr)
# print(arr.dtype)
#
# import numpy as np
#
# # arr = np.array(['a', '2', '3'], dtype='i')
#
# arr = np.array([1.1, 2.1, 3.1])
#
# newarr = arr.astype('i')
#
# print(newarr)
# print(newarr.dtype)
#
#
# arr = np.array([1.1, 2.1, 3.1])
#
# newarr = arr.astype(int)
#
# print(newarr)
# print(newarr.dtype)
#
# arr = np.array([1, 0, 3])
#
# newarr = arr.astype(bool)
#
# print(newarr)
# print(newarr.dtype)
#
#
# arr = np.array([1, 2, 3, 4, 5])
# x = arr.copy()
# arr[0] = 42
#
# print(arr)
# print(x)
#
# arr = np.array([1, 2, 3, 4, 5])
# x = arr.view() #Make a view, change the view, and display both arrays:
# arr[0] = 42
# x[0] = 31
#
# print(arr)
# print(x)
# print(arr.shape)
#
# arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
#
# newarr = arr.reshape(4, 3)
#
# print(newarr)
#
# newarr = arr.reshape(2, 3, 2)
#
# print(newarr)
#
# arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
#
# print(arr.reshape(2, 4).base)
#
# # Flattening the arrays
# # Flattening array means converting a multidimensional array into a 1D array.
# #
# # We can use reshape(-1) to do this.
#
# arr = np.array([[1, 2, 3], [4, 5, 6]])
#
# newarr = arr.reshape(-1)
#
# print(newarr)
#
# arr = np.array([1, 2, 3])
#
# for x in arr:
#   print(x)
#
# arr = np.array([[1, 2, 3], [4, 5, 6]])
#
# for x in arr:
#       print(x)
#
# for x in arr:
#   for y in x:
#     print(y)
#
# arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
#
# for x in arr:
#   print(x)
#
# for x in arr:
#   for y in x:
#     for z in y:
#       print(z)
#
# a = np.array([1, 2, 3])
# b = np.array([4, 5, 6])
#
# print(a + b)   # Element-wise addition
# print(a * b)   # Element-wise multiplication
# print(a ** 2)  # Square each element
# print(np.sum(arr))     # Sum of all elements
# print(np.mean(arr))    # Mean (average)
# print(np.min(arr))     # Minimum value
# print(np.max(arr))     # Maximum value
# print(np.std(arr))     # Standard deviation
#
# arr = np.array([1, 2, 3, 4, 5, 6,7])
#
# newarr = np.array_split(arr, 5)
#
# # print(newarr)
#
# arr = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12]])
#
# newarr = np.array_split(arr, 3)
#
# print(newarr)
#
# arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])
#
# newarr = np.array_split(arr, 3, axis=1)
#
# print(newarr)
#
# import numpy as np
#
# arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
#
# x = np.where(arr%2 == 0)
#
# print(x)
#
# import numpy as np
#
# arr = np.array([6, 7, 8, 9])
#
# x = np.searchsorted(arr, 7)
#
# print(x)
#
# arr = np.array([6, 7, 8, 9])
#
# x = np.searchsorted(arr, 7, side='right')
#
# print(x)
#
# arr = np.array([1, 3, 5, 7])
#
# x = np.searchsorted(arr, [2, 4, 6])
#
# print(x)
#
# arr = np.array([3, 2, 0, 1])
#
# print(np.sort(arr))

###############################################################################
# What is a Series?
# A Pandas Series is like a column in a table.
#
# It is a one-dimensional array holding data of any type.
import pandas as pd
#
# a = [1, 7, 2]

# myvar = pd.Series(a)
#
# print(myvar)
#
# myvar = pd.Series(a, index=["x", "y", "z"])
#
# print(myvar)
#
# calories = {"day1": 420, "day2": 380, "day3": 390}
#
# myvar = pd.Series(calories)
#
# print(myvar)
#
# myvar = pd.Series(calories, index=["day1", "day2"])
#
# print(myvar)
#
# data = {
#     "calories": [420, 380, 390],
#     "duration": [50, 40, 45]
# }
#
# # load data into a DataFrame object:
# df = pd.DataFrame(data)
#
# print(df)
#
# print(df.loc[0])
# print(df.loc[[0, 1]])
#
# df = pd.DataFrame(data, index = ["day1", "day2", "day3"])
# print(df)
#
#
# print(df.loc["day2"])


# df = pd.read_csv('data.csv')
#
# print(df)
#
# print(df.to_string())
#
# pd.options.display.max_rows = 9999
#
# df = pd.read_csv('data.csv')
#
# print(df)

# print(df.head())
# print(df.head(10))
# new_df = df.dropna()
# print(new_df.to_string())
#
# df.dropna(inplace = True)
#
# print(df.to_string())
#
# df.fillna(130, inplace = True)
# # df["Calories"].fillna(130, inplace = True)
#
# df = pd.read_csv('data.csv')

# x = df["Calories"].mean()
#
# df["Calories"].fillna(x, inplace = True)
# x = df["Calories"].median()
#
# df["Calories"].fillna(x, inplace = True)
#
# x = df["Calories"].mode()[0]
#
# df["Calories"].fillna(x, inplace = True)

import pandas as pd

df = pd.read_csv('data.csv')
print(df.head())

df['Date'] = pd.to_datetime(df['Date'])

print(df.to_string())

df['Date'] = pd.to_datetime(df['Date'])

print(df.to_string())

# Replacing Values
df.loc[7, 'Duration'] = 45

for x in df.index:
  if df.loc[x, "Duration"] > 120:
    df.loc[x, "Duration"] = 120


# duplicates
print(df.duplicated())

# Removing Duplicates
# To remove duplicates, use the drop_duplicates() method.

df.drop_duplicates(inplace = True)


# df.corr()