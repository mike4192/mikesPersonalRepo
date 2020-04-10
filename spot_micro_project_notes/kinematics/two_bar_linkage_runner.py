#!/usr/bin/env python

from two_bar_linkage import TwoBarLinkage
import matplotlib.pyplot as plt
from math import pi




tbl = TwoBarLinkage(2,2,50*pi/180,-20*pi/180)

tbl.plot()


print('test2')
# Rotation test:
# tbl.rotate_link1(45*pi/180)


# Inverse Kinematic Test
tbl.inverse_kinematics(1.5,3)



# fig.clear()
# plt.show()

# ax.cla()

tbl.plot()
# fig.show()
# plt.pause(1)
# print('test3')
# fig.show()