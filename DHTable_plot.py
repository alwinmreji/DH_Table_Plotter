
#from tf import HomogeneousMatrix
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np
from math import radians, sin, cos
import numpy as np


class HomogeneousMatrix(object):
    # Creates a homogeneous matrix.

    def __init__(self):
        # [0,0] - [2,2] rotation
        # [0,3] - [2,3] position
        # [3,0] - [3,2] perspective parameters
        # [3,3] scale factor

        self.matrix = np.identity(4)
        #print(np.identity(4))

    def __getitem__(self, key):
        return self.matrix[key]

    def get(self):
        return self.matrix

    def roll(self, angle_X):
        # Rotates the homogeneous matrix by angle_X by the X axis

        rolled_by = np.identity(4)
        rolled_by[1, 1] = cos(radians(angle_X))
        rolled_by[1, 2] = -(sin(radians(angle_X)))
        rolled_by[2, 1] = sin(radians(angle_X))
        rolled_by[2, 2] = cos(radians(angle_X))

        self.matrix = np.dot(self.matrix, rolled_by)
        #print(self.matrix)

    '''def pitch(self, angle_Y):
        # Rotates the homogeneous matrix by angle_Y by the Y axis

        pitched_by = np.identity(4)
        pitched_by[0, 0] = cos(radians(angle_Y))
        pitched_by[0, 2] = sin(radians(angle_Y))
        pitched_by[2, 0] = -(sin(radians(angle_Y)))
        pitched_by[2, 2] = cos(radians(angle_Y))

        self.matrix = np.dot(self.matrix, pitched_by)
'''
    def yaw(self, angle_Z):
        # Rotates the homogeneous matrix by angle_Z by the Z axis

        yawed_by = np.identity(4)
        yawed_by[0, 0] = cos(radians(angle_Z))
        yawed_by[0, 1] = -(sin(radians(angle_Z)))
        yawed_by[1, 0] = sin(radians(angle_Z))
        yawed_by[1, 1] = cos(radians(angle_Z))

        self.matrix = np.dot(self.matrix, yawed_by)
        #print(self.matrix)

    '''def set_pos(self, posX, posY, posZ):
        # Sets the position of the homogeneous matrix

        self.matrix[0, 3] = posX
        self.matrix[1, 3] = posY
        self.matrix[2, 3] = posZ
'''
    def set_perspective(self, X, Y, Z):
        # Sets the perspective parameter of the homogeneous matrix

        self.matrix[3, 0] = X
        self.matrix[3, 1] = Y
        self.matrix[3, 2] = Z

    '''def set_scale(self, scale):
        # Sets the scale parameter of the homogeneous matrix

        self.matrix[3, 3] = scale
'''
    def set_a(self, a):
        # Sets the 'a' parameter of the DH convention

        self.matrix[0, 3] = a

    def set_alpha(self, alpha):
        # Sets the 'alpha' parameter of the DH convention

        self.roll(alpha)

    def set_d(self, d):
        # Sets the 'd' parameter of the DH convention

        self.matrix[2, 3] = d

    def set_theta(self, theta):
        # Sets the 'theta' parameter of the DH convention

        self.yaw(theta)

    def set_parent(self, parent):
        self.matrix = np.dot(parent, self.matrix)



'''def set_axes_equal(ax):
    Make axes of 3D plot have equal scale so that spheres appear as spheres,
    cubes as cubes, etc..  This is one possible solution to Matplotlib's
    ax.set_aspect('equal') and ax.axis('equal') not working for 3D.
    Input
      ax: a matplotlib axis, e.g., as output from plt.gca().


    x_limits = ax.get_xlim3d()
    y_limits = ax.get_ylim3d()
    z_limits = ax.get_zlim3d()

    x_range = abs(x_limits[1] - x_limits[0])
    x_middle = np.mean(x_limits)
    y_range = abs(y_limits[1] - y_limits[0])
    y_middle = np.mean(y_limits)
    z_range = abs(z_limits[1] - z_limits[0])
    z_middle = np.mean(z_limits)

    # The plot bounding box is a sphere in the sense of the infinity
    # norm, hence I call half the max range the plot radius.
    plot_radius = 0.5*max([x_range, y_range, z_range])

    ax.set_xlim3d([x_middle - plot_radius, x_middle + plot_radius])
    ax.set_ylim3d([y_middle - plot_radius, y_middle + plot_radius])
    ax.set_zlim3d([z_middle - plot_radius, z_middle + plot_radius])
'''

base = HomogeneousMatrix()
joint1 = HomogeneousMatrix()
joint2 = HomogeneousMatrix()
joint3 = HomogeneousMatrix()
joint4 = HomogeneousMatrix()
joint5 = HomogeneousMatrix()
joint6 = HomogeneousMatrix()

# --- Robotic Arm construction ---

#    Joint Angle variables

q1, q2, q3 = 0, 0, 0
q4, q5, q6 = 0, 0, 0

#    ---------------------

joint1.set_d(100)
joint1.set_theta(q1)
joint1.set_a(200)
joint1.set_alpha(90)

joint2.set_d(300)
joint2.set_a(0)
joint2.set_alpha(0)
joint2.set_theta(q2)

'''joint3.set_a(120)
joint3.set_d(135)
joint3.set_theta(q3)
joint3.set_alpha(-90)

#joint4.set_a(250)
joint4.set_d(620)
#joint4.set_theta(-90)
joint4.set_alpha(90)
joint4.set_theta(q4)

joint5.set_alpha(-90)
#joint5.set_theta(90)
joint5.set_theta(q5)

#joint6.set_theta(-90)
#joint6.set_alpha(-90)
joint6.set_d(115)
joint6.set_theta(q6)'''

# ---------------------------------

joint1.set_parent(base.get())

joint2.set_parent(joint1.get())
joint3.set_parent(joint2.get())
joint4.set_parent(joint3.get())
joint5.set_parent(joint4.get())
joint6.set_parent(joint5.get())
#print(joint6)
# Prepare the coordinates for plotting

X = [base[0, 3], joint1[0, 3],
     joint2[0, 3], joint3[0, 3],
     joint4[0, 3], joint5[0, 3],
     joint6[0, 3]]
print( X)
Y = [base[1, 3], joint1[1, 3],
     joint2[1, 3], joint3[1, 3],
     joint4[1, 3], joint5[1, 3],
     joint6[1, 3]]
print( Y)
Z = [base[2, 3], joint1[2, 3],
     joint2[2, 3], joint3[2, 3],
     joint4[2, 3], joint5[2, 3],
     joint6[2, 3]]
print( Z)

# Plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
#ax = plt.axes(projection='3d')
#ax.set_aspect('equal')
#ax.plot3D(X,Z)
ax.plot_wireframe(X,Y,Z)

ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')

#set_axes_equal(ax)
plt.show()

