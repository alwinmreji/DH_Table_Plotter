from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np
from math import radians, sin, cos

class cognateMatrix(object):
    # Creates a homogeneous matrix.
    def __init__(self):
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

    def yaw(self, angle_Z):
        # Rotates the homogeneous matrix by angle_Z by the Z axis
        yawed_by = np.identity(4)
        yawed_by[0, 0] = cos(radians(angle_Z))
        yawed_by[0, 1] = -(sin(radians(angle_Z)))
        yawed_by[1, 0] = sin(radians(angle_Z))
        yawed_by[1, 1] = cos(radians(angle_Z))
        self.matrix = np.dot(self.matrix, yawed_by)

    def set_perspective(self, X, Y, Z):
        # Sets the perspective parameter of the homogeneous matrix
        self.matrix[3, 0] = X
        self.matrix[3, 1] = Y
        self.matrix[3, 2] = Z

    def set_a(self, a):
        # Sets the 'a' parameter of the DH convention
        v = np.identity(4)
        v[0,3] = a
        self.matrix = np.dot(self.matrix, v)

    def set_d(self, d):
        # Sets the 'd' parameter of the DH convention
        self.matrix[2, 3] = d

    def set_parent(self, parent):
        self.matrix = np.dot(parent, self.matrix)

# Function to plot the readed DH_Parameter
def PlotDH(DH_Parameter):
    base = cognateMatrix()
    List_of_Joints = []
    List_of_Joints.append(base)
    # --- Robotic Arm construction ---
    for val in DH_Parameter:
        joint = cognateMatrix()
        joint.yaw(val[0])
        joint.set_d(val[1])
        joint.set_a(val[2])
        joint.roll(val[3])
        joint.set_parent(List_of_Joints[-1].get())
        List_of_Joints.append(joint)
    X,Y,Z = [],[],[]
    for coordinates in List_of_Joints:
        X.append(coordinates[0, 3])
        Y.append(coordinates[1, 3])
        Z.append(coordinates[2, 3])
    # Plot
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot(X,Y,Z)
    for x,y,z in zip(X,Y,Z):
        print("(",round(x,1),round(y,1),round(z,1),")")
        k = ("("+str(int(round(x,1)))+","+str(int(round(y,1)))+","+str(int(round(z,1)))+")")
        ax.scatter(x,y,z,marker = "$"+k+"$", s = 1000, color ='red')
    ax.scatter(X[-1],Y[-1],Z[-1], marker = "1", s =100, color = 'blue')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')
    print(List_of_Joints)
    plt.show()
