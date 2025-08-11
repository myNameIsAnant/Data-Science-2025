# Import Numpy as np
import numpy as np

# Create an array of 10 Zeros
print(np.zeros(10))

# Create an array of 10 Ones
print(np.ones(10))

# Create an array of 10 Fives
print(np.ones(10)*5)

# Create an array of integers from 10 to 50
print(np.arange(10,51))

# Create an array of integers of Even Numbers from 10 to 50
print(np.arange(10,51,2))

# Create 3x3 Matrix with Values 0 to 8
print(np.arange(0,9).reshape(3,3))

# Create 3x3 Identity Matrix
print(np.eye(3,3))

# Generate Random Number b/w 0 and 1
print(np.random.rand())

# Generate 25 Random Numbers 
# sampled from Normal distribution
print(np.random.randn(25))

# Generate a Matrix using Linespace
print(np.linspace(0,1,101))

# Generate a Matrix using 20 Linary spaced variables
# b/w 0 ans 1
print(np.linspace(0,1,20))

### From Matrix Below
mat = np.arange(1,26).reshape(5,5)
print("Given Matrix :",mat)

"""
Output:
array([[12, 13, 14, 15],
       [17, 18, 19, 20],
       [22, 23, 24, 25]])
"""
print("Required Matrix 1:\n",mat[2:,1:])

"""
Output 20
"""
print("Required Output 2 :",mat[3][-1])


"""
Output:
array([[ 2],
       [ 7],
       [12]])
"""
print("Required Matrix 3:\n",mat[:3,1:2])


"""
Output:
array([21, 22, 23, 24, 25])
"""
print("Required Matrix 4:\n",mat[-1])

"""
Output:
array([[16, 17, 18, 19, 20],
       [21, 22, 23, 24, 25]])
"""
print("Required Matrix 5:\n",mat[-2:])

# Get the sum of all the values in mat
print("Sum of all values in mat :",mat.sum())

# Get the standard deviation of the values in mat
print("STD DEV of all values in mat :",mat.std())

# Get the sum of all the columns in mat
print("Column Wise of all values in mat :",mat.sum(axis=0))

# Get Same Random Numbers
np.random.seed(42)
print("Get Same Random Number :",np.random.rand())