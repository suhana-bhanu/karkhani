# Mobius Strip Modeling

This Python package models a Mobius strip using parametric equations and computes key geometric properties.

## Features

- Create a Mobius strip with customizable radius, width, and resolution
- Visualize the strip in 3D with matplotlib
- Calculate surface area and edge length numerically
- Interactive parameter adjustment for real-time visualization

## Mathematical Background

The Mobius strip is represented using the following parametric equations:

```
x(u,v) = (R + v⋅cos(u/2))⋅cos(u)
y(u,v) = (R + v⋅cos(u/2))⋅sin(u)
z(u,v) = v⋅sin(u/2)
```

Where:
- u ∈ [0,2π]
- v ∈ [-w/2,w/2]
- R is the radius (distance from center to strip)
- w is the width of the strip

## Code Structure

- `mobius_strip/`: Main package directory
  - `__init__.py`: Package initialization
  - `mobius_strip.py`: Core MobiusStrip class implementation
  - `visualization.py`: Visualization utilities
- `main.py`: Demonstration script

## Usage

```python
from mobius_strip import MobiusStrip, plot_mobius_strip

# Create a Mobius strip
mobius = MobiusStrip(radius=3.0, width=1.0, resolution=100)

# Calculate geometric properties
surface_area = mobius.calculate_surface_area()
edge_length = mobius.calculate_edge_length()

print(f"Surface Area: {surface_area}")
print(f"Edge Length: {edge_length}")

# Visualize the strip
import matplotlib.pyplot as plt
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')
plot_mobius_strip(mobius, ax)
plt.show()
```

For interactive visualization:

```python
from mobius_strip import interactive_plot
interactive_plot()
```

## Implementation Notes

### Surface Area Calculation

The surface area is calculated using numerical integration. For the Mobius strip, the surface area element is:

dA = |R_u × R_v| du dv

where R_u and R_v are partial derivatives of the position vector with respect to u and v.

### Edge Length Calculation

The edge length is calculated by summing the distances between consecutive points along the boundary of the strip.

## Requirements

- NumPy
- Matplotlib

## Running the Demo

```
python main.py
```