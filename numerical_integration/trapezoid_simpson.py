import numpy as np
import matplotlib.pyplot as plt

# Real integral/area value for comparison
real_value = 0.74682413279

# Our function f
def f(x):
    return np.exp(-np.square(x))

# Number of intervals for trapezoid and Simpson's rule
trapezoid_subs = [10, 20, 40, 80, 160]
simpson_subs = [2, 4, 8, 16, 32]

# Store the absolute value of error calculated in trapezoid and Simpson's rule functions
trapezoid_error = []
simpson_error = []

# Function for trapezoidal rule
def trapezoid(h, y):
    n = len(y)
    s = y[0] / 2.0

    for i in range(1, n - 1):
        s += y[i]

    s += y[n - 1] / 2.0

    return h * s

# Function for Simpson's rule
def simpson(h, y):
    n = len(y)
    s = y[0]

    for i in range(1, n - 1):
        val = 2
        if i % 2 == 1:
            val = 4
        s += val * y[i]

    s += y[n - 1]

    return h * s / 3.0

# x-axis is between [0, 1]
lo = 0
hi = 1

# Execute trapezoid
for num in trapezoid_subs:
    # Calculate h
    h = (hi - lo) / num
    # Store num+1 points into x using np.arange
    x = np.arange(start=lo, stop=hi + h, step=h)
    y = f(x)
    estimated = trapezoid(h, y)
    trapezoid_error.append(np.abs(real_value - estimated))

# Execute Simpson's rule
for num in simpson_subs:
    # Calculate h
    h = (hi - lo) / num
    # Store num+1 points into x using np.arange
    x = np.arange(start=lo, stop=hi + h, step=h)
    y = f(x)
    estimated = simpson(h, y)
    simpson_error.append(np.abs(real_value - estimated))

# Print errors
print('Trapezoid error')
print(trapezoid_error)

# Check convergence (should approach 4)
for i in range(1, len(trapezoid_error)):
    print(trapezoid_error[i - 1] / trapezoid_error[i])

print('Simpson error')
print(simpson_error)

# Check convergence (should approach 16)
for i in range(1, len(simpson_error)):
    print(simpson_error[i - 1] / simpson_error[i])

# Plotting the errors
plt.subplot(2, 1, 1)
plt.plot(trapezoid_subs, trapezoid_error, '*')
plt.plot(trapezoid_subs, trapezoid_error)
plt.title('Trapezoid')
plt.ylabel('Error')
plt.grid()

plt.subplot(2, 1, 2)
plt.plot(simpson_subs, simpson_error)
plt.title('Simpson 1/3')
plt.ylabel('Error')
plt.xlabel('Num of intervals')
plt.grid()

plt.show()
