import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Parameters
A = 1  # Amplitude for x
B = 1  # Amplitude for y
a = 3  # Frequency for x
b = 2  # Frequency for y
t = np.linspace(0, 2 * np.pi, 1000)  # 1000 points from 0 to 2π

# Initialize the figure
fig, ax = plt.subplots(figsize=(8, 8))
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title('Lissajous Curve Animation')
ax.grid(True)
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1.5, 1.5)
ax.set_aspect('equal')

# Initialize an empty line for the curve
line, = ax.plot([], [], lw=2)

# Animation function
def animate(delta):
    x = A * np.sin(a * t + delta)
    y = B * np.sin(b * t)
    line.set_data(x, y)
    ax.set_title(f'Lissajous Curve: a={a}, b={b}, δ={delta:.2f}')
    return line,

# Create the animation
ani = animation.FuncAnimation(
    fig, animate, frames=np.linspace(0, 2 * np.pi, 100), interval=50, blit=True
)

# Save the animation as an MP4 file
ani.save('lissajous-animation.mp4', writer='ffmpeg', fps=30)

# Display the animation
plt.show()

