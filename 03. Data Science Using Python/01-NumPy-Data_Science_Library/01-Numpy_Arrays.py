import numpy as np

# Transforming a list into a NumPy array
my_list = [1,2,3,4,5]

k = np.array(my_list)
print(k)
print(type(k))

matrix = [[1,2,3],[7,8,9],[4,5,6]]
my_matrix = np.array(matrix)
print(my_matrix)

print(np.arange(1,11,2))

print(np.zeros(5,dtype=int))
print(np.zeros((5,2),dtype=int))

print(np.linspace(0,10,21))

print(np.eye(2,dtype=int))

a = np.random.rand(4,3)
print("a=",a)

b = np.random.randint(5,11,(4,5))
print("b=",b)

c = np.random.randn(3,4)
print("c=",c)

np.random.seed(40)
d = np.random.rand(2)
print("d=",d)


