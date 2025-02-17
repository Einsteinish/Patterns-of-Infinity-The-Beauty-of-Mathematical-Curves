import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the resolution
width, height = 800, 800  # Image resolution
max_iter = 200  # Maximum number of iterations
threshold = 2  # Divergence threshold

# Define zoom parameters
num_frames = 100  # Number of frames in the animation
center_x, center_y = -0.7435, 0.1314  # Zoom into this point
zoom_factor = 1.5  # Zoom-in speed

# Function to compute the Mandelbrot set
def mandelbrot_set(x_min, x_max, y_min, y_max, width, height, max_iter):
    x = np.linspace(x_min, x_max, width)
    y = np.linspace(y_min, y_max, height)
    X, Y = np.meshgrid(x, y)
    c = X + 1j * Y  # Complex plane

    z = np.zeros_like(c, dtype=complex)
    mandelbrot = np.zeros((height, width))

    for i in range(max_iter):
        mask = (np.abs(z) < threshold)  # Points that haven't diverged yet
        z[mask] = z[mask]**2 + c[mask]
        mandelbrot[mask] += 1  # Increment the iteration count

    return mandelbrot

# Function to generate each frame for animation
def update(frame):
    zoom = zoom_factor ** (-frame / 10)  # Exponential zoom-in effect
    x_range = 3.0 * zoom
    y_range = 3.0 * zoom * (height / width)

    x_min, x_max = center_x - x_range / 2, center_x + x_range / 2
    y_min, y_max = center_y - y_range / 2, center_y + y_range / 2

    mandelbrot = mandelbrot_set(x_min, x_max, y_min, y_max, width, height, max_iter)

    ax.clear()
    ax.imshow(mandelbrot, extent=(x_min, x_max, y_min, y_max), cmap='hot', origin='lower')
    ax.set_title(f'Mandelbrot Zoom Frame {frame+1}')
    ax.set_xlabel('Re(c)')
    ax.set_ylabel('Im(c)')

# Set up the figure and animation
fig, ax = plt.subplots(figsize=(8, 8))
ani = animation.FuncAnimation(fig, update, frames=num_frames, interval=50)

# Save as MP4
ani.save('mandelbrot_zoom.mp4', writer='ffmpeg', fps=30)

plt.show()

