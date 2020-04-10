#!/usr/bin/env python

import numpy as np
from two_bar_linkage import TwoBarLinkage
from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt
from math import pi, sin, cos



fig, ax = plt.subplots(1,1)

link1_angle = 50
link2_angle = -20

# Create a two bar linkage object and plot it
tbl = TwoBarLinkage(2,2,link1_angle*pi/180,link2_angle*pi/180)

tbl.plot(ax)
ax.set_title("Two Bar Linkage With Link Angles Set \
             \n Link 1: %1.1f deg, Link 2: %1.1f deg"%(link1_angle,link2_angle))


# Plot inverse kinematic example
fig2, ax2 = plt.subplots(1,1)
x_pos, y_pos = 1.5, 3

tbl.inverse_kinematics(x_pos,y_pos)

# Make plot
tbl.plot(ax2)

# Plot green dot for desired pos
plt.plot(x_pos,y_pos,'go')

ax2.set_title("Two Bar Linkage Positioned at (%1.1f,%1.1f) via Inverse Kinematics \
             \n Link 1: %1.1f deg, Link 2: %1.1f deg"%(x_pos,y_pos,tbl.q1*180/pi,tbl.q2*180/pi))

# Plot both plots
plt.show()
