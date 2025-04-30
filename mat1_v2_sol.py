import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-2.5, 2.5, 10).reshape((-1, 1))

# Plot x^2 with red circles
plt.plot(x, x * x, 'ro', label='x^2')

# Plot exp(x) with blue dashed line
plt.plot(x, np.exp(x), 'b--', label='exp')

# Plot sin(x) with solid magenta line
plt.plot(x, np.sin(x), '-m', label='sin')

# Correct the line to turn on the axes
plt.axis('auto')

plt.title('Matplotlib plot')
plt.legend()
plt.show()
