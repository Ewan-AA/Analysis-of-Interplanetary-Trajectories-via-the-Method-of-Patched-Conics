# Re-importing libraries after state reset
import matplotlib.pyplot as plt
import numpy as np

# Create the figure and axis
fig, ax = plt.subplots(figsize=(8, 8))

# Define the circles
circle1 = plt.Circle((0, 0), 0.75, color='blue', fill=False, linewidth=2,label='Orbit 1')  # Smaller circle
circle2 = plt.Circle((0, 0), 2, color='red', fill=False, linewidth=2,label='Orbit 2')  # Larger circle

# Define the ellipse parameters
ellipse_center = (-0.625, 0)
ellipse_width = 2.75  # Semi-major axis * 2
ellipse_height = 0.75  # Semi-minor axis * 2

# Parametrize the ellipse
theta = np.linspace(0, 2 * np.pi, 500)
a = ellipse_width / 2  # Semi-major axis
b = ellipse_height / 2  # Semi-minor axis

# Ellipse center
x_center, y_center = ellipse_center

# Parametric equations for the ellipse
x = x_center + a * np.cos(theta)
y = y_center + b * np.sin(theta)

# Split into upper and lower halves
upper_mask = y >= 0
lower_mask = y < 0

x_upper, y_upper = x[upper_mask], y[upper_mask]
x_lower, y_lower = x[lower_mask], y[lower_mask]

# Draw the circles
ax.add_artist(circle1)
ax.add_artist(circle2)

# Plot the upper half of the ellipse (solid)
ax.plot(x_upper, y_upper, linestyle='-', color='green', linewidth=2,label='Hohmann Ellipse Trajectory')

# Plot the lower half of the ellipse (dotted)
ax.plot(x_lower, y_lower, linestyle=':', color='green', linewidth=2)

# Set limits and aspect ratio
ax.set_xlim(-2.5, 2.5)
ax.set_ylim(-2.5, 2.5)
ax.set_aspect('equal', adjustable='datalim')

# Annotate the apoapsis and periapsis
ax.plot(0.75, 0, 'go')
ax.plot(-2, 0, 'ro')

ax.plot([-2, 0.75], [0, 0], color='purple', linestyle='-', linewidth=2,label='Semi-major Axis')

# Add legend and grid
ax.legend(loc='upper right')
ax.grid(True)
plt.title("Hohmann Transfer")
plt.show()
plt.savefig('Hohmann Transfer.png',dpi=400)