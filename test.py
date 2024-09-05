import numpy as np

def calculate_collision(m1, v1, m2, v2):
    """
    Calculate the velocities of two balls after an elastic collision.
    
    Parameters:
    m1, m2: masses of the balls
    v1, v2: initial velocities of the balls (numpy arrays)
    
    Returns:
    v1f, v2f: final velocities of the balls (numpy arrays)
    """
    v1f = v1 - (2 * m2 / (m1 + m2)) * np.dot(v1 - v2, v1 - v2) / np.linalg.norm(v1 - v2)**2 * (v1 - v2)
    v2f = v2 - (2 * m1 / (m1 + m2)) * np.dot(v2 - v1, v2 - v1) / np.linalg.norm(v2 - v1)**2 * (v2 - v1)
    return v1f, v2f

# Example usage
m1 = 1.0  # mass of ball 1
m2 = 1.0  # mass of ball 2
v1 = np.array([2.0, 1.0])  # initial velocity of ball 1
v2 = np.array([-1.0, -1.0])  # initial velocity of ball 2

v1f, v2f = calculate_collision(m1, v1, m2, v2)

print("Final velocity of ball 1:", v1f[0])
print("Final velocity of ball 2:", v2f)
