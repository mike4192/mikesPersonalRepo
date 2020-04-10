#!/usr/bin/env python

# Import 3d support for matplotlib
from mpl_toolkits import mplot3d

import math
from math import pi
import numpy as np
import matplotlib.pyplot as plt
import transformations


# fig = plt.figure()
# ax = plt.axes(projection='3d')

# x = np.array([0, 1, 1, 1])
# y = np.array([0, 0, 1, 1])
# z = np.array([0, 0, 0, 1])

# ax.plot3D(x,y,z)

# ax.set_xlabel('x')
# ax.set_ylabel('y')
# ax.set_zlabel('z')

#plt.show(block=False)
#plt.pause(1)

#print('hello')

# Start 2d pose example 

fig1 = plt.figure(1)
plt.axis([0,3,0,3])
plt.axis('scaled')
plt.grid(True)

point_in_B_axes = np.array([1,1])
B_axes_translation_from_A = [2,1]
B_axes_rotation_from_A = 30*pi/180

rotz = transformations.rotz(B_axes_rotation_from_A)

basis_vectors_B_axes = rotz[0:2,0:2]
basis_vectors_A_axes = np.array([[0,1],[1,0]])
print(basis_vectors_B_axes)

# Plot A and B axes

# A axes, X arrow
plt.arrow(0,0,
    basis_vectors_A_axes[0,0],basis_vectors_A_axes[0,1],color='b',width=0.01)
# A axes, Y arrow
plt.arrow(0,0,
    basis_vectors_A_axes[1,0],basis_vectors_A_axes[1,1],color='b',width=0.01)

# B axes, X arrow
plt.arrow(B_axes_translation_from_A[0],B_axes_translation_from_A[1],
    basis_vectors_B_axes[0,0],basis_vectors_B_axes[1,0],color='r',width=0.01)
# B axes, Y arrow
plt.arrow(B_axes_translation_from_A[0],B_axes_translation_from_A[1],
    basis_vectors_B_axes[0,1],basis_vectors_B_axes[1,1],color='r',width=0.01)

# Plot point
point_in_A_axes = rotz[0:2,0:2].dot(point_in_B_axes) + B_axes_translation_from_A
 
print(point_in_A_axes)
plt.plot(point_in_A_axes[0],point_in_A_axes[1],'ro')
plt.plot([0,point_in_A_axes[0]],[0,point_in_A_axes[1]],'b--')
print("Point in A axes: ", point_in_A_axes)

plt.xlabel('X axis')
plt.ylabel('Y axis')





# Same example but using homegeneous form
fig2 = plt.figure(2)
plt.axis([0,3,0,3])
plt.axis('scaled')
plt.grid(True)

p_B = np.array([1,1,0])

translation_B_from_A = np.array([1,1,0])

# X, Y, Z rotation angles of coordinate system B relative to coordinate system A
rotations_B_from_A = np.array([0,0,45*pi/180]) 

rotx = transformations.rotx(rotations_B_from_A[0])
roty = transformations.roty(rotations_B_from_A[1])
rotz = transformations.rotz(rotations_B_from_A[2])

# Matrix multiplication via '@' symbol
rot_xyz = rotx @ roty @ rotz

# Construct Homogeneous transform
ht_B_from_A = np.block([[rot_xyz, p_B.reshape(-1,1)],[0,0,0,1]])

# Plot A axes
plt.arrow(0,0,1,0,color='b',width=0.01)
plt.arrow(0,0,0,1,color='b',width=0.01)

# Plot B axes
plt.arrow(translation_B_from_A[0],translation_B_from_A[1],
        ht_B_from_A[0,0],ht_B_from_A[1,0],
        color='r',width=0.01)
plt.arrow(translation_B_from_A[0],translation_B_from_A[1],
        ht_B_from_A[0,1],ht_B_from_A[1,1],
        color='r',width=0.01)

# Calculate point B in A axes using homegenous transform
p_B_tilde = np.block([p_B, 1])
print(p_B_tilde)
p_B_A = ht_B_from_A @ p_B_tilde.transpose()

print('point B in A axes: ',p_B_A)

# Plot point B
plt.plot(p_B_A[0],p_B_A[1],'ro')

# Plot vector of point B in A axes
plt.plot([0, p_B_A[0]],[0, p_B_A[1]],'b--')



plt.show()
