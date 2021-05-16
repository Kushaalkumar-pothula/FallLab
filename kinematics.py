#======================Kinematics======================
def velocity(t):
    """
    Calculates velocity of a freely falling object
    Args:
    -t: time
    Returns:
    -vel: free fall velocity
    """
    g = 9.81 #m/s^2
    vel = g*t
    return vel

def position(vel, t):
    """
    Calculates position of a freely falling object
    Args:
    -vel: Velocity of the object at a given time
    -t: time
    Returns:
    -y: Position of the body
    """
    y = 100
    y = y - (vel*t)
    return y
#==========================================================
