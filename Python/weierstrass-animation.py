import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Parameters
a = 0.5  # Must satisfy 0 < a < 1
b_values = np.linspace(0.1, 5, 100)  # Range of b values from 0.1 to 5
N = 100  # Number of terms in the series
x = np.linspace(-2, 2, 1000)  # Range of x values

# Weierstrass Function
def weierstrass(x, a, b, N):
    total = np.zeros_like(x)
    for n in range(N):
        total += a**n * np.cos(b**n * np.pi * x)
    return total

# Set up the figure and axis
fig, ax = plt.subplots(figsize=(10, 6))
line, = ax.plot([], [], color='blue', linewidth=1.5)
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)
ax.set_xlabel('x')
ax.set_ylabel('f(x)')
ax.set_title(f'Weierstrass Function Animation')

# Initialization function
def init():
    line.set_data([], [])
    return line,

# Animation update function
def update(frame):
    b = b_values[frame]
    y = weierstrass(x, a, b, N)
    line.set_data(x, y)
    ax.set_title(f'Weierstrass Function: a={a}, b={b:.2f}, N={N}')
    return line,

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=len(b_values), init_func=init, blit=False, interval=50)

# Save as an MP4 file (optional)
ani.save('weierstrass-animation.mp4', writer='ffmpeg', fps=30)

# Show the animation
plt.show()

