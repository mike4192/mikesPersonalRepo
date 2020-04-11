import numpy as np
import math
from math import pi
import matplotlib.pyplot as plt




class SpotMicroStickFigure(object):
    """Encapsulates an 12 DOF spot micro stick figure  

    Encapuslates a 12 DOF spot micro stick figure. The 12 degrees of freedom represent the twelve joint angles.
    Contains inverse kinematic capabilities
    two bar linkage for the purpose of demonstrating
    forward and inverse kinematics by plotting states of the two bar system

    Attributes:
        a1: length of first link, must be positive and non-zero
        a2: length of second link, must be positive and non-zero
        q1: rotation angle of link 1 in radians relative to fixed coordinate system
        q2: rotation angle of link 2 in radians relative to link 1 pose coordinate system
    """