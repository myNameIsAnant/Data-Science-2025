import numpy as np

arr = np.arange(1,10)
arr **= 2
print("Updated Array :",arr)

arr1 = np.arange(1,6)
arr2 = np.arange(1,11)
arr3 = np.arange(11,21)
# You can operations array of same sizes
print("Added Array :",arr2+arr3) # You can add array of same sizes
print("Subtracted Array :",arr3-arr2) # You can subtract array of same sizes
print("Multiplied Array :",arr2*arr3) # You can add multiply of same sizes
print("Divided Array :",arr3/arr2) # You can add divide of same sizes
print("Floor Division Array :",arr3//arr2) # You can add divide of same sizes

# print("Adding Array with diff Sizes :",arr1+arr3) - Cannot Add array of Different Sizes

## Some built in Mats Functions in Numpy

print("Square Root of 4 is :",np.sqrt(4))
print("Square Root of arr is :",np.sqrt(arr))

print("Sin 30 is :",np.sin(30))
print("Sin of arr is :",np.sin(arr))

print("Log 10 is :",np.log(10))
print("Log of arr is :",np.log(arr))

print("Value of Pi :",np.pi)

## Performing some Operations in Array
print("Sum of all elements of arr2 is :",arr2.sum())
print("Max of all elements of arr2 is :",arr2.max())
print("Min of all elements of arr2 is :",arr2.min())
print("Mean of all elements of arr2 is :",arr2.mean())
print("Variance of all elements of arr2 is :",arr2.var())
print("Std Dev of all elements of arr2 is :",arr2.std())

## Operating on Multi Dimensional Array
marr = np.arange(0,25).reshape(5,5)
print("My MultiDimensional Array :",marr)
print("Sum of all elements of marr is :",marr.sum())
print("Sum of all elements across Columns of marr is :",marr.sum(axis=0))
print("Sum of all elements across Rows of marr is :",marr.sum(axis=1))
