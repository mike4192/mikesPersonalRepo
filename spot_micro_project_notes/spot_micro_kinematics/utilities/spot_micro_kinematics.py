from . import transformations
from math import pi, cos, sin
import numpy as np

def t_rightback(t_m,l,w):
    '''Creates a 4x4 numpy homogeneous transformation matrix representing coordinate system and 
    position of the rightback leg of a quadriped. Assumes legs postioned in corners of a rectangular
    plane defined by a width and length 

    Args:
        t_m: 4x4 numpy matrix. Homogeneous transform representing the coordinate system of the center
        of the robot body
        l: length of the robot body
        w: width of the robot body

    Returns: 
        4x4 numpy matrix. A homogeneous transformation representing the position of the right back leg
    '''
    temp_homog_transf = np.block( [ [ transformations.roty(pi/2), np.array([[-l/2],[0],[w/2]])  ],
                                    [np.array([0,0,0,1])] ]    )
    return t_m @ temp_homog_transf

def t_rightfront(t_m,l,w):
    '''Creates a 4x4 numpy homogeneous transformation matrix representing coordinate system and 
    position of the rightfront leg of a quadriped. Assumes legs postioned in corners of a rectangular
    plane defined by a width and length 

    Args:
        t_m: 4x4 numpy matrix. Homogeneous transform representing the coordinate system of the center
        of the robot body
        l: length of the robot body
        w: width of the robot body

    Returns: 
        4x4 numpy matrix. A homogeneous transformation representing the position of the right front leg
    '''
    temp_homog_transf = np.block( [ [ transformations.roty(pi/2), np.array([[l/2],[0],[w/2]])  ],
                                    [np.array([0,0,0,1])] ]    )
    return t_m @ temp_homog_transf

def t_leftfront(t_m,l,w):
    '''Creates a 4x4 numpy homogeneous transformation matrix representing coordinate system and 
    position of the left front leg of a quadriped. Assumes legs postioned in corners of a rectangular
    plane defined by a width and length 

    Args:
        t_m: 4x4 numpy matrix. Homogeneous transform representing the coordinate system of the center
        of the robot body
        l: length of the robot body
        w: width of the robot body

    Returns: 
        4x4 numpy matrix. A homogeneous transformation representing the position of the left front leg
    '''
    temp_homog_transf = np.block( [ [ transformations.roty(-pi/2), np.array([[l/2],[0],[-w/2]])  ],
                                    [np.array([0,0,0,1])] ]    )
    return t_m @ temp_homog_transf

def t_leftback(t_m,l,w):
    '''Creates a 4x4 numpy homogeneous transformation matrix representing coordinate system and 
    position of the left back leg of a quadriped. Assumes legs postioned in corners of a rectangular
    plane defined by a width and length 

    Args:
        t_m: 4x4 numpy matrix. Homogeneous transform representing the coordinate system of the center
        of the robot body
        l: length of the robot body
        w: width of the robot body

    Returns: 
        4x4 numpy matrix. A homogeneous transformation representing the position of the left back leg
    '''
    temp_homog_transf = np.block( [ [ transformations.roty(-pi/2), np.array([[-l/2],[0],[-w/2]])  ],
                                    [np.array([0,0,0,1])] ]    )
    return t_m @ temp_homog_transf


def t_0_to_1(theta1,l1):
    '''Create the homogeneous transformation matrix for joint 0 to 1 for a quadriped leg.

    Args:
        theta1: Rotation angle in radians of the hip joint
        l1: Length of the hip joint link

    Returns:
        A 4x4 numpy matrix. Homogeneous transform from joint 0 to 1
    '''
    # I believe there is a typo in the paper. The paper lists this matrix as:
    # 
    # t =    [ cos(theta1)     -sin(theta1)    0        -l1*cos(theta1);
    #          sin(theta1)     -cos(theta1)    0        -l1*sin(theta1);
    #                    1                0    0                      0;
    #                    0                0    0                      1;]
    # 
    # However I believe index [2],[0] should be zero, and index [2],[2] should be 1 instead.
    # If not, then the rotated z axis disapears?? And from the diagram, it appears the transformed
    # axis's z axis is the same as the original. So I think the matrix should be:
    # 
    # t =    [ cos(theta1)     -sin(theta1)    0        -l1*cos(theta1);
    #          sin(theta1)     -cos(theta1)    0        -l1*sin(theta1);
    #                    0                0    1                      0;
    #                    0                0    0                      1;]
    
    t_01 = np.block( [ [ transformations.rotz(theta1), np.array([[-l1*cos(theta1)],[-l1*sin(theta1)],[0]])  ],
                                    [np.array([0,0,0,1])] ]    )

    
    return t_01



