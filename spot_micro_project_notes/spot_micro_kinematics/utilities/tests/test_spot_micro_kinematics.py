"""Tests for the spot micro kinematics module"""

import unittest
from .. import spot_micro_kinematics
from .. import transformations
import numpy as np
from math import cos, sin, pi

class TestSpotMicroKinematics(unittest.TestCase):
    '''Tests rotation matrices'''

    def test_t_rightback(self):
        '''Test the homogeneous transformation to the right back leg via a contrived example'''
        
        # First create a homogenous transformation representing the robot center body.
        # No rotations, no translations

        t_m = transformations.homog_transform(0,0,0,0,0,0)
        l = 2
        w = 3
        t_rightback = spot_micro_kinematics.t_rightback(t_m,l,w)

        known_true_rot = np.array(
            [   [cos(pi/2),   0,  sin(pi/2),  -l/2],
                [0,           1,          0,     0],
                [-sin(pi/2),  0,  cos(pi/2),   w/2],
                [0,           0,          0,     1]    ])

        try:
            np.testing.assert_array_almost_equal(t_rightback, known_true_rot)
            res = True
        except AssertionError as err:
            res = False
            print (err)
        self.assertTrue(res)
        

    def test_t_rightfront(self):
        '''Test the homogeneous transformation to the right front leg via a contrived example'''
        
        # First create a homogenous transformation representing the robot center body.
        # No rotations, no translations

        t_m = transformations.homog_transform(0,0,0,0,0,0)
        l = 2
        w = 3
        t_rightfront = spot_micro_kinematics.t_rightfront(t_m,l,w)

        known_true_rot = np.array(
            [   [cos(pi/2),   0,  sin(pi/2),   l/2],
                [0,           1,          0,     0],
                [-sin(pi/2),  0,  cos(pi/2),   w/2],
                [0,           0,          0,     1]    ])

        try:
            np.testing.assert_array_almost_equal(t_rightfront, known_true_rot)
            res = True
        except AssertionError as err:
            res = False
            print (err)
        self.assertTrue(res)
        
    def test_t_leftfront(self):
        '''Test the homogeneous transformation to the left front leg via a contrived example'''
        
        # First create a homogenous transformation representing the robot center body.
        # No rotations, no translations

        t_m = transformations.homog_transform(0,0,0,0,0,0)
        l = 2
        w = 3
        t_leftfront = spot_micro_kinematics.t_leftfront(t_m,l,w)

        known_true_rot = np.array(
            [   [cos(-pi/2),   0,  sin(-pi/2),   l/2],
                [0,           1,          0,     0],
                [-sin(-pi/2),  0,  cos(-pi/2),   -w/2],
                [0,           0,          0,     1]    ])

        try:
            np.testing.assert_array_almost_equal(t_leftfront, known_true_rot)
            res = True
        except AssertionError as err:
            res = False
            print (err)
        self.assertTrue(res)

    def test_t_leftback(self):
        '''Test the homogeneous transformation to the left back leg via a contrived example'''
        
        # First create a homogenous transformation representing the robot center body.
        # No rotations, no translations

        t_m = transformations.homog_transform(0,0,0,0,0,0)
        l = 2
        w = 3
        t_leftback = spot_micro_kinematics.t_leftback(t_m,l,w)

        known_true_rot = np.array(
            [   [cos(-pi/2),   0,  sin(-pi/2),   -l/2],
                [0,           1,          0,     0],
                [-sin(-pi/2),  0,  cos(-pi/2),   -w/2],
                [0,           0,          0,     1]    ])

        try:
            np.testing.assert_array_almost_equal(t_leftback, known_true_rot)
            res = True
        except AssertionError as err:
            res = False
            print (err)
        self.assertTrue(res)

    def test_t_0_to_1(self):
        '''Test the homogeneous transformation of leg joint 0 to joint 1 via a contrived example'''
        
        theta1 = 35*pi/180
        l1 = 0.4
        t = spot_micro_kinematics.t_0_to_1(theta1,l1)

        known_true = np.array(
            [   [cos(theta1),  -sin(theta1),             0,   -l1*cos(theta1)],
                [sin(theta1),   cos(theta1),             0,   -l1*sin(theta1)],
                [          0,             0,             1,                 0],
                [          0,             0,             0,                 1]    ])

        try:
            np.testing.assert_array_almost_equal(t, known_true)
            res = True
        except AssertionError as err:
            res = False
            print (err)
        self.assertTrue(res)
    