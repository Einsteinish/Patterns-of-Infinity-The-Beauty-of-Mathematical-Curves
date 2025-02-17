import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Parameters
width, height = 800, 800  # Image resolution
max_iter = 100  # Maximum number of iterations
threshold = 2  # Divergence threshold
zoom_factor = 0.05  # Zoom factor per frame
num_frames = 100  # Number of frames in the animation

# Initial range for the complex plane
x_min, x_max = -2.0, 1.0
y_min, y_max = -1.5, 1.5

# Target zoom region (center of the zoom)
target_x, target_y = -0.5, 0.0  # Center of the zoom

# Initialize the figure
fig, ax = plt.subplots(figsize=(10, 10))
ax.set_xlabel('Re(c)')
ax.set_ylabel('Im(c)')
ax.set_title('Mandelbrot Set Zoom Animation')

# Function to compute the Mandelbrot Set
def compute_mandelbrot(x_min, x_max, y_min, y_max):
    x = np.linspace(x_min, x_max, width)
    y = np.linspace(y_min, y_max, height)
    X, Y = np.meshgrid(x, y)
    c = X + 1j * Y
    z = np.zeros_like(c, dtype=complex)
    mandelbrot = np.zeros((height, width))

    for i in range(max_iter):
        z = z**2 + c
        mask = (np.abs(z) < threshold)
        mandelbrot += mask

    return mandelbrot

# Function to update the plot for each frame
def update(frame):
    global x_min, x_max, y_min, y_max

    # Zoom into the target region
    x_range = x_max - x_min
    y_range = y_max - y_min
    x_min = target_x - x_range * zoom_factor**frame / 2
    x_max = target_x + x_range * zoom_factor**frame / 2
    y_min = target_y - y_range * zoom_factor**frame / 2
    y_max = target_y + y_range * zoom_factor**frame / 2

    # Compute the Mandelbrot Set for the new region
    mandelbrot = compute_mandelbrot(x_min, x_max, y_min, y_max)

    # Update the plot
    ax.clear()
    ax.imshow(mandelbrot, extent=(x_min, x_max, y_min, y_max), cmap='hot', origin='lower')
    ax.set_xlabel('Re(c)')
    ax.set_ylabel('Im(c)')
    ax.set_title(f'Mandelbrot Set Zoom Animation (Frame {frame + 1}/{num_frames})')

# Create the animation
ani = animation.FuncAnimation(
    fig, update, frames=num_frames, interval=50, repeat=False
)

# Save the animation
try:
    ani.save("mandelbrot_zoom.mp4", writer="ffmpeg", fps=20)
    print("Animation saved successfully!")
except Exception as e:
    print(f"Error saving animation: {e}")

# Display the animation
plt.show()
