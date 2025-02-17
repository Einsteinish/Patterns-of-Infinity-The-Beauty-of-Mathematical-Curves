import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the parameter t
# t = np.linspace(0, 12 * np.pi, 10000)
t = np.linspace(0, 12 * np.pi, 1000)  # use 1000 points

# Compute x(t) and y(t)
x = np.sin(t) * (np.exp(np.cos(t)) - 2 * np.cos(4 * t) - np.sin(t / 12)**5)
y = np.cos(t) * (np.exp(np.cos(t)) - 2 * np.cos(4 * t) - np.sin(t / 12)**5)

# Set up the figure and axis
fig, ax = plt.subplots(figsize=(8, 8))
ax.set_xlim(min(x), max(x))
ax.set_ylim(min(y), max(y))
ax.set_xlabel("x(t)")
ax.set_ylabel("y(t)")
ax.set_title("Butterfly Curve Animation")
ax.grid(True)
ax.set_aspect('equal')  # Ensure equal scaling for x and y axes

# Initialize an empty line for the curve
line, = ax.plot([], [], lw=2, color='red')

# Animation function
def animate(i):
    # Update the line data up to the i-th point
    line.set_data(x[:i], y[:i])
    return line,

# Create the animation
ani = animation.FuncAnimation(
    fig, animate, frames=len(t), interval=20, blit=True, repeat=False
)

# To save the animation as a video file (e.g., MP4)
try:
    ani.save("butterfly_curve.mp4", writer="ffmpeg", fps=60)
    print("Animation saved successfully!")
except Exception as e:
    print(f"Error saving animation: {e}")

# Display the animation
plt.show()


