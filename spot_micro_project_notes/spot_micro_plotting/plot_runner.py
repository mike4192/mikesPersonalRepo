#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.axes3d as p3
import matplotlib.animation as animation
from spot_micro_kinematics.spot_micro_stick_figure import SpotMicroStickFigure


# Instantiate spot micro stick figure obeject
sm = SpotMicroStickFigure()


# Attaching 3D axis to the figure
fig = plt.figure()
ax = p3.Axes3D(fig)

ax.set_xlabel('X')
ax.set_ylabel('Z')
ax.set_zlabel('Y')

ax.set_xlim3d([-0.25, 0.25])
ax.set_zlim3d([-0.4, 0.1])
ax.set_ylim3d([-0.25,0.25])

# ax.view_init(elev=135,azim=0)


# Get leg coordinates
coords = sm.get_leg_coordinates()


# Initialize empty list top hold line objects
lines = []

# Construct the body of 4 lines from the first point of each leg (the four corners of the body)
for i in range(4):
     

    if i == 3:
        ind = -1
    else:
        ind = i

    # Due to mplot3d rotation and view limitations, swap y and z to make the stick figure
    # appear oriented better
    x_vals = [coords[ind][0][0], coords[ind+1][0][0]]
    y_vals = [coords[ind][0][1], coords[ind+1][0][1]]
    z_vals = [coords[ind][0][2], coords[ind+1][0][2]]

    lines.append(ax.plot(x_vals,z_vals,y_vals)[0])

for leg in coords:
    for i in range(3):
        
        # Due to mplot3d rotation and view limitations, swap y and z to make the stick figure
        # appear oriented better
        x_vals = [leg[i][0], leg[i+1][0]]
        y_vals = [leg[i][1], leg[i+1][1]]
        z_vals = [leg[i][2], leg[i+1][2]]

        lines.append(ax.plot(x_vals,z_vals,y_vals)[0])



plt.show()
    