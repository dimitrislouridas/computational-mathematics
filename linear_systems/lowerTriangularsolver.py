import numpy as np

# Given matrix A and vector b
A = np.array([[1, 0, 0, 0, 0],
              [1, 2, 0, 0, 0],
              [1, 2, 3, 0, 0],
              [1, 2, 3, 4, 0],
              [1, 2, 3, 4, 5]], dtype='float')

b = np.array([1, 2, 3, 4, 5], dtype='float').reshape((-1, 1))

# Print the original matrix A and vector b
print('A')
print(A)
print('b')
print(b)

# Lower triangular solver function
def lowerTriangularsolver(A, b):
    x = np.zeros_like(b, dtype='float')
    n = x.shape[0]

    # Forward substitution loop
    for i in range(n):
        s = 0
        for j in range(0, i):
            s += A[i][j] * x[j]
        x[i] = (b[i] - s) / A[i][i]

    return x

# Upper triangular solver function
def upperTriangularsolver(A, b):
    # Solving using lowerTriangularsolver on the transposed matrix
    ret = lowerTriangularsolver(A.T, b.T)
    return ret

# Solve the lower triangular system Ax = b
print('x (Lower Case)')
x = lowerTriangularsolver(A, b)
print(x)
print('check')
print(np.dot(A, x))

# Upper triangular case
print('Upper Case')
# We know that Ax = b (lower case) is equivalent to x^T A^T = b^T (upper case)

# In this example, A is chosen as A^T and b2 as b^T
x2 = upperTriangularsolver(A.T, b.T)

# Print the result x2
print('x2 (Upper Case)')
print(x2)

# Check: x2^T * A^T should be equal to b^T
print('check')
print(np.dot(x2.T, A.T))

# Print the transposed vector b (b^T)
print('b2')
print(b.T)
