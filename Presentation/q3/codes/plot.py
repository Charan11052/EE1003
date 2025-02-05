import numpy as np
import matplotlib.pyplot as plt

# Function to generate points for the curve y = sqrt(16 - x^2)
def generate_circle_points():
    x_vals = np.linspace(-4, 4, 500)  # Increased number of points for smoother curve
    y_vals = np.sqrt(16 - x_vals**2)
    return x_vals, y_vals

# Points A and B where the curve meets the x-axis
A = np.array([4, 0])
B = np.array([-4, 0])

# Generate points for the curve
x_vals, y_vals = generate_circle_points()

# Create the plot
plt.figure(figsize=(8, 6))
plt.plot(x_vals, y_vals, label=r'$y = \sqrt{16 - x^2}$', color='blue', linewidth=2)

# Fill the area under the curve
plt.fill_between(x_vals, y_vals, color='lightblue', alpha=0.4)

# Set the axis position
ax = plt.gca()
ax.spines['top'].set_color('none')
ax.spines['left'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['bottom'].set_position('zero')

# Plot the x-axis (y = 0)
plt.axhline(0, color='black', linewidth=1)

# Label the coordinates A and B
tri_coords = np.vstack((A, B)).T
plt.scatter(tri_coords[0, :], tri_coords[1, :], color='red', zorder=5)  # Red dots for A and B
vert_labels = ['A(4,0)', 'B(-4,0)']
for i, txt in enumerate(vert_labels):
    plt.annotate(txt,  # this is the text
                 (tri_coords[0, i], tri_coords[1, i]),  # this is the point to label
                 textcoords="offset points",  # how to position the text
                 xytext=(0, 10),  # distance from text to points (x,y)
                 fontsize=12, color='red',  # Font size and color for labels
                 ha='center')  # horizontal alignment

# Plot settings
plt.xlabel(r'$x$-axis', fontsize=14, labelpad=10)  # Labeled x-axis with padding for better spacing
plt.ylabel(r'$y$-axis', fontsize=14, labelpad=10)  # Labeled y-axis with padding for better spacing
plt.title(r'Region Bounded by $y = \sqrt{16 - x^2}$ and the x-axis is $8\pi$ sq.units', fontsize=16)
plt.legend(loc='best', fontsize=12)
plt.grid(True, which='both', linestyle='--', linewidth=0.7, alpha=0.7)  # More visible grid
plt.axis('equal')

# Save the plot with a higher resolution
plt.savefig('plot.png', dpi=300, bbox_inches='tight')

# Show the plot
plt.show()

