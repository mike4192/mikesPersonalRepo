#!/usr/bin/env python

import numpy as np
import math as m

def rotx(a):
    """Creates a numpy rotaion matrix about the x axis

    Args:
        a: angle for rotation in radians
    
    Returns:
        The rotation matrix about the x axis
    """
    rotxMatrix = np.array(
        [[1,                     0,                0],  
         [0,              m.cos(a),        -m.sin(a)],  
         [0,              m.sin(a),         m.cos(a)]])
    return rotxMatrix


def roty(a):
    """Creates a numpy rotaion matrix about the y axis

    Args:
        a: angle for rotation in radians
    
    Returns:
        The rotation matrix about the y axis
    """
    rotxMatrix = np.array(\
        [[m.cos(a),              0,         m.sin(a)] ,  \
         [0,                     1,                0],   \
         [-m.sin(a),             0,         m.cos(a)]])
    return rotxMatrix



def rotz(a):
    """Creates a numpy rotaion matrix about the x axis

    Args:
        a: angle for rotation in radians
    
    Returns:
        The rotation matrix about the z axis
    """
    rotxMatrix = np.array(\
        [[m.cos(a),      -m.sin(a),                0],   \
         [m.sin(a),       m.cos(a),                0],  \
         [0,                     0,                1]])
    return rotxMatrix
