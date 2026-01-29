import numpy as np

# Cholesky decomposition function
def cholesky(A):
    # Initialize matrix L with zeros
    L = np.zeros_like(A)
    n = A.shape[0]  # Size of the matrix

    # Loop over columns
    for j in range(n):
        # Loop over rows starting from the current column index
        for i in range(j, n):
            # Diagonal element case (i == j)
            if i == j:
                s = 0
                # Calculate the sum of squared elements in the current column up to the diagonal
                for k in range(j):
                    s += L[i][k] ** 2
                # Compute and assign the diagonal element
                L[j][j] = (A[j][j] - s) ** 0.5
            
            # If not in Diagonal element case 
            else:
                s = 0
                # Calculate the sum of products of corresponding elements in the current row and column up to the diagonal
                for k in range(j):
                    s += L[i][k] * L[j][k]
                # Compute and assign the non-diagonal element
                L[i][j] = (A[i][j] - s) / L[j][j]

    # Return the lower triangular matrix L
    return L


# Example 
# Perform Cholesky decomposition on matrix S

# Given matrix A
A = np.array([[1, 0, 0, 0, 0],
              [1, 2, 0, 0, 0],
              [1, 2, 3, 0, 0],
              [1, 2, 3, 4, 0],
              [1, 2, 3, 4, 5]], dtype='float')

# Symmetric matrix S obtained by multiplying transpose of A by A
S = np.dot(A.T, A)

# Perform Cholesky decomposition on matrix S
L = cholesky(S)

# Print original matrix A
print('A')
print(A)

# Print symmetric matrix S obtained by multiplying transpose of A by A
print('S')
print(S)

# Print lower triangular matrix L obtained from Cholesky decomposition
print('L')
print(L)

# Print the result of the check: L * L^T should be equal to S
print('check')
print(np.dot(L, L.T))
