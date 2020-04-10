#!/usr/bin/env python

import numpy as np
import math as m

def htx(a,x,y,z):
    """Create a 4x4 numpy homogeneous transformation matrix about the x axis

    The first three columns represent the new basis vectors in the global coordinate
    system of a coordinate system rotated by this matrix. The 3 elements of the last
    column represent the linear translation of of that coordinate system  

    Args:
        a: angle for rotation in radians
        x: Translation along the x axis of the rotated coordinate system 
        y: Translation along the y axis of the rotated coordinate system
        z: Translation along the z axis of the rotated coordinate system

    
    Returns:
        The homogeneous transformation matrix about the x axis
    """
    rotxMatrix = np.array(
        [[1,                     0,                0,       0],  
         [0,              m.cos(a),        -m.sin(a),       0],  
         [0,              m.sin(a),         m.cos(a),       0],
         [0,                     0,                0,       1]])
    
    txMatrix = np.array(
        [[1,                     0,                0,       x],
         [0,                     1,                0,       y],
         [0,                     0,                1,       z],
         [0,                     0,                0,       1]]
    )
    return rotxMatrix @ txMatrix


def hty(a,x,y,z):
    """Create a 4x4 numpy homogeneous transformation matrix about the y axis

    The first three columns represent the new basis vectors in the global coordinate
    system of a coordinate system rotated by this matrix. The 3 elements of the last
    column represent the linear translation of of that coordinate system  

    Args:
        a: angle for rotation in radians
        x: Translation along the x axis of the rotated coordinate system 
        y: Translation along the y axis of the rotated coordinate system
        z: Translation along the z axis of the rotated coordinate system

    
    Returns:
        The homogeneous transformation matrix about the x axis
    """
    rotxMatrix = np.array(
       [[m.cos(a),              0,         m.sin(a),        0],
        [0,                     1,                0,        0],
        [-m.sin(a),             0,         m.cos(a),        0],
        [0,                     0,                0,        1]])

    txMatrix = np.array(
        [[1,                     0,                0,       x],
         [0,                     1,                0,       y],
         [0,                     0,                1,       z],
         [0,                     0,                0,       1]]
    )
    return rotxMatrix @ txMatrix



def htz(a,x,y,z):
    """Create a 4x4 numpy homogeneous transformation matrix about the z axis

    The first three columns represent the new basis vectors in the global coordinate
    system of a coordinate system rotated by this matrix. The 3 elements of the last
    column represent the linear translation of of that coordinate system  

    Args:
        a: angle for rotation in radians
        x: Translation along the x axis of the rotated coordinate system 
        y: Translation along the y axis of the rotated coordinate system
        z: Translation along the z axis of the rotated coordinate system

    
    Returns:
        The homogeneous transformation matrix about the x axis
    """
    rotxMatrix = np.array(
        [[m.cos(a),      -m.sin(a),                0,       0], 
         [m.sin(a),       m.cos(a),                0,       0],
         [0,                     0,                1,       0],
         [0,                     0,                0,       1]])

    txMatrix = np.array(
        [[1,                     0,                0,       x],
         [0,                     1,                0,       y],
         [0,                     0,                1,       z],
         [0,                     0,                0,       1]]
    )
    return rotxMatrix @ txMatrix
