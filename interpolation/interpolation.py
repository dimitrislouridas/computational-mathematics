import numpy as np
import matplotlib.pyplot as plt

# Define the Runge function
def f(x):
    return 1.0 / (1 + 25 * x**2)

# Generate 20 equally spaced points between -1 and 1
x = np.linspace(-1, 1, 20)
y = f(x)

# Define the interpolation function
def interpolation(x, y, z):
    # x, y, z must all be 1D arrays

    # x and y are the original data points (x, y)
    # z is the vector where we want to estimate the polynomial values

    # Initialize the array to store interpolated values
    val = np.zeros((z.shape[0], 1))

    # Iterate for each point in z
    for k in range(z.shape[0]):
        # Calculate val[k] using Lagrange polynomial interpolation
        for i in range(x.shape[0]):
            # Initialize the product for the Lagrange basis polynomial
            prod = 1
            # Iterate for all x_j
            for j in range(x.shape[0]):
                if i != j:
                    # Calculate the Lagrange basis polynomial product
                    prod *= (z[k] - x[j]) / (x[i] - x[j])
            # Update the interpolated value for the current z[k]
            val[k] += prod * y[i]

    return val

# Use linspace to generate 39 points between -1 and 1
z = np.linspace(-1, 1, 39)

# Calculate 20 Chebyshev points
inp = np.arange(1, 21).reshape((-1, 1))
cheb_x = np.cos((2 * inp - 1) * np.pi / (2 * inp.shape[0]))
cheb_y = f(cheb_x)

# Print Chebyshev points for reference
print(cheb_x)

# Run interpolation with uniform partition
uniform_estimated = interpolation(x, y, z)

# Run interpolation with Chebyshev partition
cheb_estimated = interpolation(cheb_x, cheb_y, z)

# Plotting the results
plt.plot(z, f(z), label='true values')
plt.plot(x, y, '*', label='interpolated points')
plt.plot(cheb_x, cheb_y, 'b+', label='Chebyshev points')

plt.plot(z, uniform_estimated, '--', label='uniform estimated values')
plt.plot(z, cheb_estimated, 'y-', label='Chebyshev estimated values')

plt.axis([-1.5, 1.5, -1.5, 7])
plt.grid()
plt.legend()
plt.show()
