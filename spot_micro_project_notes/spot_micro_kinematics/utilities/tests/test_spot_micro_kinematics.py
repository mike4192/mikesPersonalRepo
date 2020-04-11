"""Tests for the spot micro kinematics module"""

import unittest
from .. import spot_micro_kinematics
from .. import transformations
import numpy as np
from math import cos, sin, pi

class TestSpotMicroKinematics(unittest.TestCase):
    '''Tests rotation matrices'''

    def test_t_rightback(self):
        '''Test the homogeneous transformation via a contrived example'''
        
        # First create a homogenous transformation representing the robot center body.
        # No rotations, no translations

        t_m = transformations.homog_transform(0,0,0,0,0,0)

        t_rightback = spot_micro_kinematics.t_rightback(t_m,2,3)

        known_true_rot = np.array(
            [   [cos(pi/2),   0,  sin(pi/2),  -2/2],
                [0,           1,          0,     0],
                [-sin(pi/2),  0,  cos(pi/2),   3/2],
                [0,           0,          0,     1]    ])

        try:
            np.testing.assert_array_almost_equal(t_rightback, known_true_rot)
            res = True
        except AssertionError as err:
            res = False
            print (err)
        self.assertTrue(res)
        
