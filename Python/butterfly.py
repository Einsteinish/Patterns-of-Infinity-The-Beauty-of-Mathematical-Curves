import numpy as np
import matplotlib.pyplot as plt

# Define the parameter t
t = np.linspace(0, 12 * np.pi, 10000)

# Compute x(t) and y(t)
x = np.sin(t) * (np.exp(np.cos(t)) - 2 * np.cos(4 * t) - np.sin(t / 12)**5)
y = np.cos(t) * (np.exp(np.cos(t)) - 2 * np.cos(4 * t) - np.sin(t / 12)**5)

# Plot the curve
plt.figure(figsize=(8, 8))
plt.plot(x, y, color='red')
plt.title("Butterfly Curve")
plt.xlabel("x(t)")
plt.ylabel("y(t)")
plt.grid(True)
plt.axis('equal')  # Ensure equal scaling for x and y axes
plt.show()
