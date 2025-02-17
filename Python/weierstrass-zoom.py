import numpy as np
import matplotlib.pyplot as plt

# Parameters
a = 0.5  # Must satisfy 0 < a < 1
b = 7  # Must be a positive odd integer and satisfy ab > 1 + 3π/2
N = 100  # Number of terms in the series
x_zoom = np.linspace(0.5, 0.6, 5000)  # Higher resolution in zoomed range

# Weierstrass Function
def weierstrass(x, a, b, N):
    total = np.zeros_like(x)
    for n in range(N):
        total += a**n * np.cos(b**n * np.pi * x)
    return total

# Compute the function in the zoomed range
y_zoom = weierstrass(x_zoom, a, b, N)

# Plot the zoomed-in Weierstrass Function
plt.figure(figsize=(10, 6))
plt.plot(x_zoom, y_zoom, color='red', linewidth=1)
plt.title(f'Weierstrass Function (Zoomed-In): a={a}, b={b}, N={N}, Interval=[0.5, 0.6]')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid(True)
plt.show()

