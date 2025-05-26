"""
Mobius strip implementation with parametric equations and geometric calculations.
"""

import numpy as np
from typing import Tuple, Optional


class MobiusStrip:
    """
    A class representing a Mobius strip using parametric equations.
    
    Attributes:
        radius (float): Distance from the center to the strip.
        width (float): Width of the strip.
        resolution (int): Number of points in the mesh for each parameter.
    """
    
    def __init__(self, radius: float = 3.0, width: float = 1.0, resolution: int = 100):
        """
        Initialize the Mobius strip with given parameters.
        
        Args:
            radius (float): Distance from the center to the strip.
            width (float): Width of the strip.
            resolution (int): Number of points in the mesh for each parameter.
        """
        self.radius = radius
        self.width = width
        self.resolution = resolution
        
        # Initialize mesh coordinates
        self.u_range = np.linspace(0, 2 * np.pi, resolution)
        self.v_range = np.linspace(-width / 2, width / 2, resolution)
        
        # Pre-compute mesh grid for faster calculations
        self._update_mesh()
    
    def _update_mesh(self):
        """Update the mesh grid based on current parameters."""
        self.u_grid, self.v_grid = np.meshgrid(self.u_range, self.v_range)
        self._compute_coordinates()
    
    def _compute_coordinates(self):
        """Compute the (x, y, z) coordinates using the parametric equations."""
        # Compute intermediate values
        half_u = self.u_grid / 2
        cos_half_u = np.cos(half_u)
        sin_half_u = np.sin(half_u)
        cos_u = np.cos(self.u_grid)
        sin_u = np.sin(self.u_grid)
        
        # Apply parametric equations
        self.x = (self.radius + self.v_grid * cos_half_u) * cos_u
        self.y = (self.radius + self.v_grid * cos_half_u) * sin_u
        self.z = self.v_grid * sin_half_u
    
    def update_parameters(self, radius: Optional[float] = None, 
                          width: Optional[float] = None, 
                          resolution: Optional[int] = None):
        """
        Update the parameters of the Mobius strip.
        
        Args:
            radius (float, optional): New radius value.
            width (float, optional): New width value.
            resolution (int, optional): New resolution value.
        """
        if radius is not None:
            self.radius = radius
        if width is not None:
            self.width = width
            self.v_range = np.linspace(-width / 2, width / 2, self.resolution)
        if resolution is not None:
            self.resolution = resolution
            self.u_range = np.linspace(0, 2 * np.pi, resolution)
            self.v_range = np.linspace(-self.width / 2, self.width / 2, resolution)
        
        # Update the mesh with new parameters
        self._update_mesh()
    
    def get_coordinates(self) -> Tuple[np.ndarray, np.ndarray, np.ndarray]:
        """
        Get the (x, y, z) coordinates of the Mobius strip.
        
        Returns:
            Tuple[np.ndarray, np.ndarray, np.ndarray]: The x, y, and z coordinates.
        """
        return self.x, self.y, self.z
    
    def get_edge_points(self) -> Tuple[np.ndarray, np.ndarray, np.ndarray]:
        """
        Get the coordinates of points along the edges of the Mobius strip.
        
        Returns:
            Tuple[np.ndarray, np.ndarray, np.ndarray]: Edge points coordinates (x, y, z).
        """
        # Get edge indices (first and last rows of v_grid)
        v_min_idx = 0
        v_max_idx = self.resolution - 1
        
        # Extract edge points
        edge1_x = self.x[v_min_idx, :]
        edge1_y = self.y[v_min_idx, :]
        edge1_z = self.z[v_min_idx, :]
        
        edge2_x = self.x[v_max_idx, :]
        edge2_y = self.y[v_max_idx, :]
        edge2_z = self.z[v_max_idx, :]
        
        return (edge1_x, edge1_y, edge1_z), (edge2_x, edge2_y, edge2_z)
    
    def calculate_surface_area(self) -> float:
        """
        Calculate the surface area of the Mobius strip using numerical integration.
        
        Returns:
            float: The approximate surface area.
        """
        # For the Mobius strip, the surface area element is:
        # dA = |R_u × R_v| du dv
        # where R_u and R_v are partial derivatives of the position vector
        
        # Step 1: Calculate step sizes
        du = self.u_range[1] - self.u_range[0]
        dv = self.v_range[1] - self.v_range[0]
        
        # Step 2: Calculate partial derivatives
        # Partial derivative with respect to u
        R_u_x = -self.v_grid * np.sin(self.u_grid/2) * np.cos(self.u_grid) / 2 - (self.radius + self.v_grid * np.cos(self.u_grid/2)) * np.sin(self.u_grid)
        R_u_y = -self.v_grid * np.sin(self.u_grid/2) * np.sin(self.u_grid) / 2 + (self.radius + self.v_grid * np.cos(self.u_grid/2)) * np.cos(self.u_grid)
        R_u_z = self.v_grid * np.cos(self.u_grid/2) / 2
        
        # Partial derivative with respect to v
        R_v_x = np.cos(self.u_grid/2) * np.cos(self.u_grid)
        R_v_y = np.cos(self.u_grid/2) * np.sin(self.u_grid)
        R_v_z = np.sin(self.u_grid/2)
        
        # Step 3: Calculate cross product magnitude
        cross_x = R_u_y * R_v_z - R_u_z * R_v_y
        cross_y = R_u_z * R_v_x - R_u_x * R_v_z
        cross_z = R_u_x * R_v_y - R_u_y * R_v_x
        
        cross_magnitude = np.sqrt(cross_x**2 + cross_y**2 + cross_z**2)
        
        # Step 4: Numerical integration
        area = np.sum(cross_magnitude) * du * dv
        
        return area
    
    def calculate_edge_length(self) -> float:
        """
        Calculate the length of the edge of the Mobius strip.
        
        Returns:
            float: The approximate edge length.
        """
        # Get edge points
        (edge1_x, edge1_y, edge1_z), _ = self.get_edge_points()
        
        # Calculate distances between consecutive points
        dx = np.diff(edge1_x)
        dy = np.diff(edge1_y)
        dz = np.diff(edge1_z)
        
        # Sum up the distances to get the total length
        segment_lengths = np.sqrt(dx**2 + dy**2 + dz**2)
        total_length = np.sum(segment_lengths)
        
        # The total edge length is the perimeter
        return total_length * 2 * np.pi / self.resolution