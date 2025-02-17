import numpy as np
import matplotlib.pyplot as plt

# Define the resolution and range of the complex plane
width, height = 800, 800  # Image resolution
x_min, x_max = -2.0, 1.0  # Range for Re(c)
y_min, y_max = -1.5, 1.5  # Range for Im(c)
max_iter = 100  # Maximum number of iterations
threshold = 2  # Divergence threshold

# Create a grid of complex numbers c
x = np.linspace(x_min, x_max, width)
y = np.linspace(y_min, y_max, height)
X, Y = np.meshgrid(x, y)
c = X + 1j * Y  # Complex plane

# Initialize the output image
mandelbrot = np.zeros((height, width))

# Iterate the Mandelbrot formula
z = np.zeros_like(c, dtype=complex)
for i in range(max_iter):
    z = z**2 + c
    mask = (np.abs(z) < threshold)  # Points that haven't diverged yet
    mandelbrot += mask  # Increment the iteration count for non-diverged points

# Plot the Mandelbrot Set
plt.figure(figsize=(10, 10))
plt.imshow(mandelbrot, extent=(x_min, x_max, y_min, y_max), cmap='hot', origin='lower')
plt.colorbar(label='Iterations')
plt.title('Mandelbrot Set')
plt.xlabel('Re(c)')
plt.ylabel('Im(c)')
plt.show()
