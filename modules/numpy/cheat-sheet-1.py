import numpy as np

# Create a 1-dimensional array
a = np.array([1, 2, 3])
print(a)

# Create a 2-dimensional array
b = np.array([[1, 2, 3], [4, 5, 6]])
print(b)

# Create an array of all zeros
c = np.zeros((2, 3))
print(c)

# Create an array of all ones
d = np.ones((2, 3))
print(d)

# Create an array filled with a constant
e = np.full((2, 3), 7)
print(e)

# Create an identity matrix
f = np.eye(3)
print(f)

# Create an array with random values
g = np.random.random((2, 3))
print(g)

# Create an array from a list of lists
h = np.array([[1, 2, 3], [4, 5, 6]])
print(h)

# Get the number of dimensions of an array
i = h.ndim
print(i)

# Get the shape of an array
j = h.shape
print(j)

# Get the data type of an array
k = h.dtype
print(k)

# Get the size of an array
l = h.size
print(l)

# Get the size of an element in an array
m = h.itemsize
print(m)

# Get the total size of an array
n = h.nbytes
print(n)

# Get the number of elements in an array
o = np.prod(h.shape)
print(o)

# Reshape an array
p = h.reshape((3, 2))
print(p)

# Transpose an array
q = h.T
print(q)

# Flatten an array
r = h.flatten()
print(r)

# Indexing and slicing
s = h[:, 1:]
print(s)

# Boolean indexing
t = h[h > 3]
print(t)

# Array operations
u = h + 1
print(u)

v = h * 2
print(v)

w = h / 2
print(w)

x = h // 2
print(x)

y = h ** 2
print(y)

z = np.sin(h)
print(z)

# Matrix multiplication
aa = h @ p
print(aa)
