import numpy as np

"""
Indexing and Slicing
"""

my_arr = np.arange(0,11)
indexval = my_arr[8]
print("indexval :",indexval)
sliceval = my_arr[1:5]
print("sliceval :",sliceval)

"""
Broadcasting
"""

my_arr[0:3] = 120
print("Broadcasted :",my_arr)

my_arr = np.arange(0,11)
slice_arr =  my_arr[0:3]
slice_arr[:] = 120
print("Sliced Array :",slice_arr)
print("My Array :",my_arr) # Sliced Array Just Points to the Original Array so the changes will
                           # Take Effect in Original Array as well

"""
Creating copy of Array
"""
my_arr = np.arange(0,11)
new_arr = my_arr.copy()
new_arr[0:2] = 120
print("New Array :",new_arr)
print("My Array :",my_arr)


"""
Indexing and Slicing in Multidimensional array
"""

my_arr= np.array([[5,10,15],[20,25,30],[35,40,45]])
print("Multi Dimensional Array:\n",my_arr)
print("Return Row 1:\n",my_arr[0])
print("Return Last Row:\n",my_arr[-1])
print("Return Cell Value of 2nd Row and 2nd Column:\n",my_arr[1,1])

print("Return Row 1 and Row 2:\n",my_arr[:2])
print("Return from Column 2 values in Row 1 and Row 2:\n",my_arr[:2,1:])

my_arr = np.arange(1,11)
print("Checking a Conditon :",my_arr > 4)

cond_arr = my_arr > 4
print("Condition Fulfilled :",my_arr[cond_arr])