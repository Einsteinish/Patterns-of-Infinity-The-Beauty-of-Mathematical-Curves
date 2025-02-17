import numpy as np
import matplotlib.pyplot as plt

# Parameters
A = 1  # Amplitude for x
B = 1  # Amplitude for y
a = 3  # Frequency for x
b = 2  # Frequency for y
delta = np.pi / 4  # Phase shift for x
t = np.linspace(0, 2 * np.pi, 1000)  # 1000 points from 0 to 2π

# Compute x(t) and y(t)
x = A * np.sin(a * t + delta)
y = B * np.sin(b * t)

# Plot the Lissajous curve
plt.figure(figsize=(8, 8))
plt.plot(x, y, color='blue', linewidth=2)
plt.title(f'Lissajous Curve: a={a}, b={b}, δ={delta:.2f}')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.axis('equal')  # Ensure equal scaling for x and y axes
plt.show()
