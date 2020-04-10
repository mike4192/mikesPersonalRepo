#!/usr/bin/env python

import numpy as np # for numpy
from two_bar_linkage import TwoBarLinkage # for two bar linkage
from matplotlib.animation import FuncAnimation  # For animation stuff
import matplotlib.pyplot as plt # for plotting
from math import pi, sin, cos # for math function



# # Angle set
# tbl = TwoBarLinkage(2,2,50*pi/180,-20*pi/180)

# tbl.plot()


# # Inverse Kinematic Test
# tbl.inverse_kinematics(1.5,3)

# tbl.plot()


# Animation Example

# Create a two bar linkage object
tbl = TwoBarLinkage(2,2,45*pi/180,45*pi/180)

# Initialize a figure
fig = plt.figure()
ax = plt.axes(xlim=(-4,4), ylim=(-4,4))

# Set axis stuff
ax.set_title('Two Bar Linkage Inverse Kinematics \n Joint Angles to Follow Green Dot')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.axis('scaled')

# Initializeand save handles for line (and point) objects
line1, = ax.plot([],[],linewidth=3,color='b')
line2, = ax.plot([],[],linewidth=3,color='r')
dot, = ax.plot([],[],'go')

# Create data for desired point for two bar linkage to follow via inverse kinematics
# In this case, a cosine curve. No protections against going outside feasible 
# solution, program will crash if attempted
x = np.linspace(-3,3,100)
x_track = []
y_track = []

for i in x:
    x_track.append(i)
    y_track.append(2.5*cos(i) + 1)


# Define init function for animation, probably not needed in this case
def init():
    line1.set_data([],[])
    line2.set_data([],[])
    dot.set_data([],[])
    return line1,line2 

# Define animate function.
def animate(i,x,y):

    # Get the command point from the inputted data
    x_point = x_track[i]
    y_point = y_track[i]

    # Call inverse kinematic method on the command point
    tbl.inverse_kinematics(x_point,y_point)

    # Get link endpoint coordinates
    (link1,link2) = tbl.get_line_data()

    # Update lines and point for plot
    line1.set_data(link1[0],link1[1])
    line2.set_data(link2[0],link2[1])
    dot.set_data(x[i],y[i])

    return (line1,line2,dot)

# Create animation object, will run for 100 frames at 40ms between frames
anim = FuncAnimation(fig, animate, fargs=(x_track,y_track,), init_func=init, 
							frames=100, interval=40, blit=True) 
                            
# Show the plot, will loop indefinitely
plt.show()
