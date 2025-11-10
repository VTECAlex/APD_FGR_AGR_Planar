import nazca as nd
import nazca.geometries as geom


import numpy as np

def quarter_circle_curve(start, end, npoints=50, direction='cw'):
    """
    Generate (x, y) coordinates for a smooth 90° curve connecting two points.

    Parameters
    ----------
    start : tuple (x1, y1)
        Starting coordinate.
    end : tuple (x2, y2)
        Ending coordinate (must be 90° apart from start).
    npoints : int
        Number of points in the curve.
    direction : str
        'cw' = clockwise bend, 'ccw' = counterclockwise bend.

    Returns
    -------
    coords : list of (x, y)
        List of (x, y) tuples describing the curve.
    """

    x1, y1 = start
    x2, y2 = end

    # Compute vector difference
    dx, dy = x2 - x1, y2 - y1

    # The 90° arc will be part of a circle, so radius is abs(dx or dy)
    R = np.sqrt(dx**2 + dy**2)

    # Midpoint and rotation logic depend on bend direction
    if direction == 'cw':
        cx = x1
        cy = y2
        theta1, theta2 = np.pi/2, 0
    else:  # 'ccw'
        cx = x2
        cy = y1
        theta1, theta2 = np.pi, np.pi/2

    # Generate points along the arc
    theta = np.linspace(theta1, theta2, npoints)
    x = cx + R * np.cos(theta)
    y = cy + R * np.sin(theta)

    return list(zip(x, y))

rounded_radius = 20

circle_points = quarter_circle_curve((0,-20), (20,0), npoints=50, direction='cw')
# print(type(circle_points))
for i in range(len(circle_points)):
    print(circle_points[i])

rounded_corner = nd.Polygon(layer=19, points=[circle_points])
rounded_corner.put(0,0)


nd.export_gds(filename='rounded_corners.gds')
