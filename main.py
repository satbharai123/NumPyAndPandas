import numpy as np
import pandas as pd

# Create a 1D array
arr1d = np.array([1, 2, 3, 4, 5, 6])
print("array: ")
print(arr1d)

# print the element at the last index
print("value at last index : ")
print(arr1d[-1])

# print reverse order of array
print("array in reverse order : ")
print(arr1d[::-1])

# Reshape the 1D array into a 2D array with 2 rows and 3 columns
arr2d = arr1d.reshape(3, 2)

# Print the original and reshaped arrays
print("Original array:\n", arr1d)
print("Reshaped array:\n", arr2d)

# intersection of the arrays
x = np.array([1, 3, 4, 6])
y = np.array([1, 3, 7, 8])
print("intersection")
print(np.intersect1d(x, y))

# replacing even numbers with a common value
print("replace even numbers with 10 in array 1")
x[(x % 2) == 0] = 10
print(x)

# Sample series using dictionary in Pandas
the_series = {"x": "hello", "y": "inn", "z": "world"}
the_series = pd.Series(the_series)
print(the_series)

sample_series = pd.Series(list('12323'))
sample_series.name = 'num'
print(sample_series.head())

series1 = pd.Series(list('123456'))
series2 = pd.Series(list('1234'))
x1 = pd.Series(series1[~series1.isin(series2)])
print(x1)

# random
sample_series1 = pd.Series(np.random.randint(1, 20, 25))
data_frame = pd.DataFrame(sample_series1.values.reshape(5, 5))
print(data_frame)

# eye function
eye_fun1 = np.eye(6)
print(eye_fun1)
# last element
print(eye_fun1[-1])

