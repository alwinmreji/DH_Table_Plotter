# A graphical user interface get data for plotting a Denavit-Hartenberg parameters and plot it in 3D graph
# only using python

# tkinter module is the standard Python interface to the GUI toolkit
import tkinter as tkr

# Declaring global variables
get_data = []
no_of_rows = 0

# Defing 'save_data' a method for saving inserted data from table
def save_data():

    # variables 'DH_Parameters' will contain the values of angel about z, displacement about z, angel about x and displacement along x.
    # in four lists.
    DH_Parameters = []

    # 'get_data' is mapped to every rows and coloumns of the table
    # 'values' represent each coloumns of the table
    for values in get_data:

        # 'parameter' will be storing all values of a particular parameter at each iteration
        parameter = []

        # 'individual_slot' points to the individual slots of the table
        for individual_slot in values:

            # 'individual_slot.get()' method returns the value entered in the slot
            parameter.append(float(individual_slot.get()))

        # now 'parameter' contains all values of a particular parameter entered in the table form GUI
        DH_Parameters.append(parameter)

        # 'plot_dh' is method which takes DH Parameters as input and convert it to 3D coordinates, that is x, y, and z points and plot it in a 3D graph
        plot_dh(DH_Parameters)

# # Defing 'add_row' to add a new row for DH Parameters everytime user presses '+' button
# def add_row():
#
#     # Delete the button already present beside every row, that is '+' and 'save' buttons
#     add.destroy()
#     save.destroy()
#
#     no_of_rows += 1
