"""
Visualization utilities for the Mobius strip.
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D
from .mobius_strip import MobiusStrip


def plot_mobius_strip(mobius: MobiusStrip, ax=None, cmap='viridis', alpha=0.8, edge_color='red', show_edges=True):
    """
    Plot the Mobius strip using matplotlib.
    
    Args:
        mobius (MobiusStrip): The Mobius strip to plot.
        ax (Axes3D, optional): The 3D axes to plot on. If None, a new figure is created.
        cmap (str, optional): The colormap to use.
        alpha (float, optional): The transparency of the surface.
        edge_color (str, optional): The color of the edge lines.
        show_edges (bool, optional): Whether to show the edges of the strip.
    
    Returns:
        Axes3D: The 3D axes with the plot.
    """
    if ax is None:
        fig = plt.figure(figsize=(10, 8))
        ax = fig.add_subplot(111, projection='3d')
    
    # Get coordinates
    x, y, z = mobius.get_coordinates()
    
    # Plot the surface with a colormap based on z values
    surf = ax.plot_surface(x, y, z, cmap=cmap, alpha=alpha, antialiased=True)
    
    # Add a color bar
    plt.colorbar(surf, ax=ax, shrink=0.5, aspect=5)
    
    # Plot the edges if requested
    if show_edges:
        edge1, edge2 = mobius.get_edge_points()
        ax.plot(edge1[0], edge1[1], edge1[2], color=edge_color, linewidth=2)
        ax.plot(edge2[0], edge2[1], edge2[2], color=edge_color, linewidth=2)
    
    # Set labels and title
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_title(f'Mobius Strip (R={mobius.radius}, w={mobius.width})')
    
    # Set equal aspect ratio
    max_range = np.array([x.max()-x.min(), y.max()-y.min(), z.max()-z.min()]).max() / 2.0
    mid_x = (x.max()+x.min()) * 0.5
    mid_y = (y.max()+y.min()) * 0.5
    mid_z = (z.max()+z.min()) * 0.5
    ax.set_xlim(mid_x - max_range, mid_x + max_range)
    ax.set_ylim(mid_y - max_range, mid_y + max_range)
    ax.set_zlim(mid_z - max_range, mid_z + max_range)
    
    return ax


def interactive_plot():
    """
    Create an interactive plot of the Mobius strip with adjustable parameters.
    
    This function requires a running matplotlib interactive backend.
    """
    from matplotlib.widgets import Slider, Button
    
    # Create initial Mobius strip
    mobius = MobiusStrip()
    
    # Set up the figure and 3D axis
    fig = plt.figure(figsize=(12, 8))
    ax = fig.add_subplot(111, projection='3d')
    
    # Add sliders for parameters
    slider_color = 'lightgoldenrodyellow'
    ax_radius = plt.axes([0.25, 0.02, 0.65, 0.03], facecolor=slider_color)
    ax_width = plt.axes([0.25, 0.06, 0.65, 0.03], facecolor=slider_color)
    ax_resolution = plt.axes([0.25, 0.10, 0.65, 0.03], facecolor=slider_color)
    
    # Create sliders
    s_radius = Slider(ax_radius, 'Radius', 1.0, 5.0, valinit=mobius.radius)
    s_width = Slider(ax_width, 'Width', 0.1, 2.0, valinit=mobius.width)
    s_resolution = Slider(ax_resolution, 'Resolution', 20, 150, valinit=mobius.resolution, valstep=5)
    
    # Add reset button
    reset_ax = plt.axes([0.8, 0.14, 0.1, 0.04])
    reset_button = Button(reset_ax, 'Reset', color=slider_color, hovercolor='0.975')
    
    # Add text for displaying surface area and edge length
    props_ax = plt.axes([0.05, 0.14, 0.4, 0.05])
    props_ax.axis('off')
    props_text = props_ax.text(0, 0, '', fontsize=10)
    
    # Initial plot
    plot_mobius_strip(mobius, ax)
    
    # Update properties text
    def update_properties_text():
        area = mobius.calculate_surface_area()
        edge_length = mobius.calculate_edge_length()
        props_text.set_text(f'Surface Area: {area:.2f}\nEdge Length: {edge_length:.2f}')
    
    update_properties_text()
    
    # Define update function for sliders
    def update(_):
        ax.clear()
        mobius.update_parameters(
            radius=s_radius.val,
            width=s_width.val,
            resolution=int(s_resolution.val)
        )
        plot_mobius_strip(mobius, ax)
        update_properties_text()
        fig.canvas.draw_idle()
    
    # Define reset function
    def reset(_):
        s_radius.reset()
        s_width.reset()
        s_resolution.reset()
    
    # Connect callbacks
    s_radius.on_changed(update)
    s_width.on_changed(update)
    s_resolution.on_changed(update)
    reset_button.on_clicked(reset)
    
    plt.tight_layout()
    plt.subplots_adjust(bottom=0.2)
    plt.show()