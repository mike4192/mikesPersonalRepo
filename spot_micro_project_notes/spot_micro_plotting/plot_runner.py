#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.axes3d as p3
import matplotlib.animation as animation
from math import pi
from spot_micro_kinematics.spot_micro_stick_figure import SpotMicroStickFigure
from spot_micro_kinematics.utilities import spot_micro_kinematics as smk

d2r = pi/180
r2d = 180/pi

# Attaching 3D axis to the figure
fig = plt.figure()
ax = p3.Axes3D(fig)

ax.set_xlabel('X')
ax.set_ylabel('Z')
ax.set_zlabel('Y')

ax.set_xlim3d([-0.2, 0.2])
ax.set_zlim3d([0, 0.4])
ax.set_ylim3d([-0.2,0.2])

# Set azimtuth and elevation of plot
# ax.view_init(elev=135,azim=0)

# Instantiate spot micro stick figure obeject
sm = SpotMicroStickFigure(phi=10*d2r,theta=10*d2r,psi=20*d2r)

# Try setting each leg to a desired y position
x4 = -.055
y4 = -.18
z4 = 0
(l1,l2,l3) = (sm.hip_length,sm.upper_leg_length,sm.lower_leg_length)
leg12_angs = smk.ikine(x4,y4,z4,l1,l2,l3,legs12 = True)
leg34_angs = smk.ikine(x4,y4,z4,l1,l2,l3,legs12 = False)

# Define absolute position for the legs
l = sm.body_length
w = sm.body_width
l1 = sm.hip_length
l2 = sm.upper_leg_length
l3 = sm.lower_leg_length
desired_p4_points = np.array([ [-l/2,   0,  w/2 + l1],
                               [ l/2 ,  0,  w/2 + l1],
                               [ l/2 ,  0, -w/2 - l1],
                               [-l/2 ,  0, -w/2 - l1] ])

# Get body pose
ht_body = sm.ht_body
leg_angs = smk.ikine_body_pose(ht_body,desired_p4_points,l,w,l1,l2,l3)

print(leg_angs[0][2])
print('Leg angles')
print('q1: %2.1f deg, q2: %2.1f deg, q3: %2.1f deg'%(leg_angs[0][0]*r2d,leg_angs[0][1]*r2d,leg_angs[0][2]*r2d))


sm.set_leg_angles(leg_angs)

# Get leg coordinates
coords = sm.get_leg_coordinates()

# Initialize empty list top hold line objects
lines = []

# Construct the body of 4 lines from the first point of each leg (the four corners of the body)
for i in range(4):
    # For last leg, connect back to first leg point
    if i == 3:
        ind = -1
    else:
        ind = i

    # Due to mplot3d rotation and view limitations, swap y and z to make the stick figure
    # appear oriented better
    x_vals = [coords[ind][0][0], coords[ind+1][0][0]]
    y_vals = [coords[ind][0][1], coords[ind+1][0][1]]
    z_vals = [coords[ind][0][2], coords[ind+1][0][2]]
    lines.append(ax.plot(x_vals,z_vals,y_vals,color='k')[0])


# Plot color order for leg links: (hip, upper leg, lower leg)
plt_colors = ['r','c','b']
for leg in coords:
    for i in range(3):
        
        # Due to mplot3d rotation and view limitations, swap y and z to make the stick figure
        # appear oriented better
        x_vals = [leg[i][0], leg[i+1][0]]
        y_vals = [leg[i][1], leg[i+1][1]]
        z_vals = [leg[i][2], leg[i+1][2]]
        lines.append(ax.plot(x_vals,z_vals,y_vals,color=plt_colors[i])[0])

plt.show()
    