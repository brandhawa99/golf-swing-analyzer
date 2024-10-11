import numpy as np
import math

def calculate_angle(a, b, c):
    a = np.array([a.x, a.y])  # First point (e.g., shoulder)
    b = np.array([b.x, b.y])  # Mid point (e.g., elbow)
    c = np.array([c.x, c.y])  # End point (e.g., wrist)

    radians = math.atan2(c[1] - b[1], c[0] - b[0]) - math.atan2(a[1] - b[1], a[0] - b[0])
    angle = np.abs(radians * 180.0 / np.pi)

    if angle > 180.0:
        angle = 360 - angle

    return angle
