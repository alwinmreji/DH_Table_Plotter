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

    def yaw(self, angle_Z):
        # Rotates the homogeneous matrix by angle_Z by the Z axis

        yawed_by = np.identity(4)
        yawed_by[0, 0] = cos(radians(angle_Z))
        yawed_by[0, 1] = -(sin(radians(angle_Z)))
        yawed_by[1, 0] = sin(radians(angle_Z))
        yawed_by[1, 1] = cos(radians(angle_Z))

        self.matrix = np.dot(self.matrix, yawed_by)
        #print(self.matrix)

    def set_perspective(self, X, Y, Z):
        # Sets the perspective parameter of the homogeneous matrix

        self.matrix[3, 0] = X
        self.matrix[3, 1] = Y
        self.matrix[3, 2] = Z

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

def PlotDH(DH_Parameter):
    base = HomogeneousMatrix()
    # joint1 = HomogeneousMatrix()
    # joint2 = HomogeneousMatrix()
    # joint3 = HomogeneousMatrix()
    # joint4 = HomogeneousMatrix()
    # joint5 = HomogeneousMatrix()
    # joint6 = HomogeneousMatrix()
    List_of_Joints = []
    List_of_Joints.append(base)
    for val in DH_Parameter:
        joint = HomogeneousMatrix()
        joint.set_d(val[0])
        joint.set_theta(val[1])
        joint.set_a(val[2])
        joint.set_alpha(val[3])
        joint.set_parent(List_of_Joints[-1].get())
        List_of_Joints.append(joint)
    # --- Robotic Arm construction ---

    # #    Joint Angle variables
    #
    # q1, q2, q3 = 0, 0, 0
    # q4, q5, q6 = 0, 0, 0
    #
    # #    ---------------------
    #
    # joint1.set_d(100)
    # joint1.set_theta(q1)
    # joint1.set_a(200)
    # joint1.set_alpha(90)
    #
    # joint2.set_d(300)
    # joint2.set_theta(q2)
    # joint2.set_a(0)
    # joint2.set_alpha(0)
    #
    # joint3.set_d(135)
    # joint3.set_theta(q3)
    # '''joint3.set_a(120)
    # joint3.set_alpha(-90)
    #
    # joint4.set_d(620)
    # #joint4.set_theta(-90)
    # #joint4.set_a(250)
    # joint4.set_alpha(90)
    # joint4.set_theta(q4)
    #
    # joint5.set_alpha(-90)
    # #joint5.set_theta(90)
    # joint5.set_theta(q5)
    #
    # #joint6.set_theta(-90)
    # #joint6.set_alpha(-90)
    # joint6.set_d(115)
    # joint6.set_theta(q6)'''
    #
    # # ---------------------------------

    # joint1.set_parent(base.get())
    #
    # joint2.set_parent(joint1.get())
    # joint3.set_parent(joint2.get())
    # joint4.set_parent(joint3.get())
    # joint5.set_parent(joint4.get())
    # joint6.set_parent(joint5.get())
    #print(joint6)
    # Prepare the coordinates for plotting
    X,Y,Z = [],[],[]
    for coordinates in List_of_Joints:
        X.append(coordinates[0, 3])
        Y.append(coordinates[1, 3])
        Z.append(coordinates[2, 3])
    # X = [base[0, 3], joint1[0, 3],
    # joint2[0, 3], joint3[0, 3],
    # joint4[0, 3], joint5[0, 3],
    # joint6[0, 3]]
    print( X)
    # Y = [base[1, 3], joint1[1, 3],
    # joint2[1, 3], joint3[1, 3],
    # joint4[1, 3], joint5[1, 3],
    # joint6[1, 3]]
    print( Y)
    # Z = [base[2, 3], joint1[2, 3],
    # joint2[2, 3], joint3[2, 3],
    # joint4[2, 3], joint5[2, 3],
    # joint6[2, 3]]
    print( Z)
    # Plot
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    #ax = plt.axes(projection='3d')
    #ax.set_aspect('equal')
    #ax.plot3D(X,Z)
    ax.plot(X,Y,Z)

    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')

    #set_axes_equal(ax)
    plt.show()
PlotDH([[100,0,0,0],[0,0,100,0],[100,0,0,0],[0,0,100,0]])
