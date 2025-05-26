#!/usr/bin/env python3
"""
Main script to demonstrate the Mobius strip modeling.

This script showcases the MobiusStrip class and its visualization capabilities.
"""

import numpy as np
import matplotlib.pyplot as plt
from mobius_strip import MobiusStrip, plot_mobius_strip, interactive_plot


def demonstration():
    """
    Demonstrate the MobiusStrip class with different parameters and calculations.
    """
    print("Mobius Strip Demonstration")
    print("-" * 30)
    
    # Create a Mobius strip with default parameters
    mobius = MobiusStrip(radius=3.0, width=1.0, resolution=100)
    
    # Calculate and print geometric properties
    surface_area = mobius.calculate_surface_area()
    edge_length = mobius.calculate_edge_length()
    
    print(f"Default Mobius Strip (R=3.0, w=1.0):")
    print(f"  Surface Area: {surface_area:.4f}")
    print(f"  Edge Length: {edge_length:.4f}")
    print()
    
    # Try different parameters
    params = [
        (2.0, 0.5, 100),  # Small strip
        (4.0, 1.5, 100),  # Large strip
        (3.0, 2.0, 100),  # Wide strip
    ]
    
    for r, w, res in params:
        mobius.update_parameters(radius=r, width=w, resolution=res)
        surface_area = mobius.calculate_surface_area()
        edge_length = mobius.calculate_edge_length()
        
        print(f"Mobius Strip (R={r}, w={w}):")
        print(f"  Surface Area: {surface_area:.4f}")
        print(f"  Edge Length: {edge_length:.4f}")
    
    print("\nVisualization:")
    print("  1. Static visualization - creates a single figure with the default strip")
    print("  2. Comparison visualization - shows strips with different parameters")
    print("  3. Interactive visualization - allows adjusting parameters in real-time")
    
    choice = input("\nSelect a visualization option (1/2/3): ")
    
    if choice == '1':
        # Create a static visualization
        mobius = MobiusStrip()
        fig = plt.figure(figsize=(10, 8))
        ax = fig.add_subplot(111, projection='3d')
        plot_mobius_strip(mobius, ax, cmap='viridis')
        plt.tight_layout()
        plt.show()
    
    elif choice == '2':
        # Create a comparison visualization
        fig = plt.figure(figsize=(15, 5))
        
        # Default parameters
        ax1 = fig.add_subplot(131, projection='3d')
        mobius = MobiusStrip(radius=3.0, width=1.0)
        plot_mobius_strip(mobius, ax1, cmap='viridis')
        ax1.set_title('Default (R=3.0, w=1.0)')
        
        # Narrow strip
        ax2 = fig.add_subplot(132, projection='3d')
        mobius = MobiusStrip(radius=3.0, width=0.5)
        plot_mobius_strip(mobius, ax2, cmap='plasma')
        ax2.set_title('Narrow (R=3.0, w=0.5)')
        
        # Large radius
        ax3 = fig.add_subplot(133, projection='3d')
        mobius = MobiusStrip(radius=4.0, width=1.0)
        plot_mobius_strip(mobius, ax3, cmap='cividis')
        ax3.set_title('Large Radius (R=4.0, w=1.0)')
        
        plt.tight_layout()
        plt.show()
    
    elif choice == '3':
        # Launch interactive visualization
        interactive_plot()
    
    else:
        print("Invalid choice. Exiting.")


if __name__ == "__main__":
    demonstration()