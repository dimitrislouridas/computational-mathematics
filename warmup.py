import numpy as np

# Number of random points to generate
n = 200000

# Function to generate a random number between 0 and 1
def random():
    return np.random.random()

# Create n random points as (x, y) coordinates
p = [(random(), random()) for i in range(n)]

# Count points that are within the unit circle
s = 0

for point in p:
    x, y = point
    if x**2 + y**2 <= 1:
        s += 1

# or this code instead of for loop
# s = sum( [ 1 for point in p if point[0]**2 + point[1]**2 <= 1 ] )


# Estimate π using Monte Carlo method: 4 * (points_in_circle / total_points)
estimated_pi = 4 * s / n

# Print the estimated value of π
print(estimated_pi)
