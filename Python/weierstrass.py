import numpy as np
import matplotlib.pyplot as plt

# Parameters
a = 0.5  # Must satisfy 0 < a < 1
b = 7  # Must be a positive odd integer and satisfy ab > 1 + 3π/2
N = 100  # Number of terms in the series
x = np.linspace(-2, 2, 10000)  # Range of x values

# Weierstrass Function
def weierstrass(x, a, b, N):
    total = 0
    for n in range(N):
        total += a**n * np.cos(b**n * np.pi * x)
    return total

# Compute the function
y = weierstrass(x, a, b, N)

# Plot the Weierstrass Function
plt.figure(figsize=(10, 6))
plt.plot(x, y, color='blue', linewidth=1)
plt.title(f'Weierstrass Function: a={a}, b={b}, N={N}')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid(True)
plt.show()
