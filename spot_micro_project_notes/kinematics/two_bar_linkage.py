
import numpy as np
from transformations2 import htx, hty, htz
import math
from math import pi
import matplotlib.pyplot as plt




class TwoBarLinkage(object):
    """Encapsulates an example two bar linkage to plot and demonstrate kinematics 

    Encapuslates a two bar linkage for the purpose of demonstrating
    forward and inverse kinematics by plotting states of the two bar system

    Attributes:
        a1: length of first link, must be positive and non-zero
        a2: length of second link, must be positive and non-zero
        q1: rotation angle of link 1 in radians relative to fixed coordinate system
        q2: rotation angle of link 2 in radians relative to link 1 pose coordinate system
    """

    def __init__(self, a1=1, a2=1, q1=0, q2=0):
        """Inits TwoBarLinkage with linkage lengths and link angles"""
        # Assign attributes
        self.a1 = a1
        self.a2 = a2
        self.q1 = q1
        self.q2 = q2
        
        # Create private attributes for homogeneous transformation matrices for 
        # the pose of link1 and pose of link 2
        self._link1_pose = htz(self.q1,self.a1,0,0)
        self._link2_pose = self._link1_pose @ htz(self.q2,self.a2,0,0)

    def rotate_link1(self,ang):
        """Rotates link 1 by a delta angle in radians and updates internal pose states

        Parameters:
            ang: Delta angle to rotate link 1 from its current position

        Returns:
            Nothing        
        """
        self.q1 = self.q1 + ang
        self._link1_pose = htz(self.q1,self.a1,0,0)
    
    def rotate_link2(self,ang):
        """Rotates link 2 by a delta angle in radians and updates internal pose states

        Parameters:
            ang: Delta angle to rotate link 2 from its current position

        Returns:
            Nothing        
        """
        self.q2 = self.q2 + ang
        self._link2_pose = self._link1_pose @ htz(self.q2,self.a2,0,0)


    def get_link1_end_position(self):
        return (self._link1_pose[0,3],self._link1_pose[1,3])


    def get_link2_end_position(self):
        return (self._link2_pose[0,3],self._link2_pose[1,3])
    
    def get_link1_pose_axes(self):
        return (self._link1_pose[0:2,0],self._link1_pose[0:2,1])

    def get_link2_pose_axes(self):
        return (self._link2_pose[0:2,0],self._link2_pose[0:2,1])

    def inverse_kinematics(self,x_des,y_des):
        ''' Applies inverse kinematics to find the joint angles to achieve the desired x and y positions

        Applies inverse kinematics to find the joint angles q1 and q1 to achieve the 
        desired x and y positions. Sets the joint angles to those angles, and recomputes
        the pose for link1 and link2.
        Equations from: https://robotacademy.net.au/masterclass/inverse-kinematics-and-robot-motion/?lesson=291

        Parameters:
            x_des:
            y_des:

        Returns:
            Nothing
        '''
        q2 = math.acos((x_des**2 + y_des**2 - self.a1**2 - self.a2**2)/(2*self.a1*self.a2))

        # q1 = math.atan(y_des/x_des) - math.atan((self.a2*math.sin(q2)) / (self.a1 + self.a2*math.cos(q2)) )

        q1 = math.atan2(y_des,x_des) - math.atan2((self.a2*math.sin(q2)) , (self.a1 + self.a2*math.cos(q2)) )

        self.q2 = q2
        self.q1 = q1

        # Update pose matrices
        self._link1_pose = htz(self.q1,self.a1,0,0)
        self._link2_pose = self._link1_pose @ htz(self.q2,self.a2,0,0)


    def plot(self,ax):
        """
        Helper function to plot the two bar linkage with coordinate systems for the pose of each link

        Parameters:
            ax: The axes to draw to

        Returns:
            None

        """

        # fig, ax = plt.subplots(1, 1)

        axes_length_scale = 0.25
        linewidth = 3
        # Draw global coordinate axes
        ax.arrow(0,0,1*axes_length_scale,0*axes_length_scale,width=0.01,color='b')
        ax.arrow(0,0,0*axes_length_scale,1*axes_length_scale,width=0.01,color='b')

        # Draw link 1
        link1_end_pos = self.get_link1_end_position()
        ax.plot([0,link1_end_pos[0]],
                [0,link1_end_pos[1]],
                color='k',linewidth=linewidth)

        # Draw link 1 pose axes
        link1_axes = self.get_link1_pose_axes()
        
        ax.arrow(link1_end_pos[0], link1_end_pos[1],
                 link1_axes[0][0]*axes_length_scale, link1_axes[0][1]*axes_length_scale,
                 width=0.01,color='k')
        ax.arrow(link1_end_pos[0], link1_end_pos[1],
                 link1_axes[1][0]*axes_length_scale, link1_axes[1][1]*axes_length_scale,
                 width=0.01,color='k')
        
        # Draw link 2
        link2_end_pos = self.get_link2_end_position()
        ax.plot([link1_end_pos[0],link2_end_pos[0]],
                [link1_end_pos[1],link2_end_pos[1]],
                color='r',linewidth=linewidth)

        # Draw link 2 pose
        link2_axes = self.get_link2_pose_axes()
        ax.arrow(link2_end_pos[0],link2_end_pos[1],
                 link2_axes[0][0]*axes_length_scale, link2_axes[0][1]*axes_length_scale,
                 width=0.01,color='r')
        ax.arrow(link2_end_pos[0],link2_end_pos[1],
                 link2_axes[1][0]*axes_length_scale, link2_axes[1][1]*axes_length_scale,
                 width=0.01,color='r')
        
        ax.axis('scaled')

        # Size axes to capture entire linkage
        buffer = 1
        x_ref_points = [0,link1_end_pos[0],link2_end_pos[0]]
        y_ref_points = [0,link1_end_pos[1],link2_end_pos[1]]


        xmin = min(x_ref_points)
        ymin = min(y_ref_points)
        xmax = max(x_ref_points)
        ymax = max(y_ref_points)

        axmin = min(xmin,ymin)
        axmax = max(xmax,ymax)

        ax.set_xlim(axmin-buffer,axmax+buffer)
        ax.set_ylim(axmin-buffer,axmax+buffer)
        

        return None

    def get_line_data(self):
        """
        Helper function to return endpoint coordinates for to two linkages 

        Parameters:
            None

        Returns:
            A tuple of two np matrices consisting of endpoint coordinates 
            for the linkages. First row are x points, second row are y points 

        """

        # Link 1
        link1_end_pos = self.get_link1_end_position()
        link1 = np.array([ [ 0,link1_end_pos[0] ],
                        [ 0,link1_end_pos[1] ] ])

        
        # Link 2
        link2_end_pos = self.get_link2_end_position()
        link2 = np.array([ [ link1_end_pos[0],link2_end_pos[0] ],
                        [ link1_end_pos[1],link2_end_pos[1] ] ])


        return (link1,link2)
