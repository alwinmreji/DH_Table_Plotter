# A graphical user interface to get data of a Denavit-Hartenberg parameters using python

# tkinter module is the standard Python interface to the GUI toolkit
import tkinter as tkin
import DHTable_plot as plt
# Declaring global variables
get_data = []
no_of_rows = 0
width_of_slot = 8
font_data = 12

# Defining a method for invalid inputs from user
def error_handel(window,screen):

    # once ok button is pressed in error window it is destroyed
    window.destroy()

    # the main window is brought back
    screen.deiconify()


# Defing 'save_data' a method for saving inserted data from table
def save_data(screen):

    # variables 'DH_Parameters' will contain the values of angel about z, displacement about z, angel about x and displacement along x.
    # in four lists.
    DH_Parameters = []

    # 'get_data' is mapped to every rows and columns of the table
    # 'values' represent each columns of the table
    for values in get_data:

        # 'parameter' will be storing all values of a particular parameter at each iteration
        parameter = []

        # 'individual_slot' points to the individual slots of the table
        for individual_slot in values:
            try:
                # 'individual_slot.get()' method returns the value entered in the slot
                parameter.append(float(individual_slot.get()))

            # exception for invalid values entered
            except ValueError:

                # another GUI window is defined 'error'
                error = tkin.Tk()
                error.title("ERROR")
                error.geometry("+100+100")

                # hiding the main window until the ok Button is pressed in exception window
                screen.withdraw()

                # displaying the error message
                tkin.Label(error, text = "Enter a valid parameter value", font = font_data).grid(row = 0, column =0)
                ok_button = tkin.Button(error, text = "ok",font = font_data,bg="red", width = 3)

                # passing the exception window variable as val
                ok_button ['command'] = lambda val = error:error_handel(val,screen)
                ok_button.grid(row = 1, column = 0)
                error.mainloop()

        # now 'parameter' contains all values of a particular parameter entered in the table form GUI
        DH_Parameters.append(parameter)
        # screen.destroy()

    # 'plot_dh' is method which takes DH Parameters as input and convert it to 3D coordinates, that is x, y, and z points and plot it in a 3D graph
    # [[90.0, 10.0, 0.0, 0.0], [0.0, 0.0, 10.0, 90.0], [0.0, 10.0, 0.0, 0.0], [90.0, 0.0, 10.0, 0.0]]
    print(DH_Parameters)
    plt.PlotDH(DH_Parameters)


# Defining 'add_row' to add a new row for DH Parameters everytime user presses '+' button
def add_row(add,save,screen):
    global no_of_rows

    # Delete the button already present beside every row, that is '+' and 'save' buttons
    add.destroy()
    save.destroy()

    # keep count number of rows
    no_of_rows += 1

    # serail number is auto generated using the following method
    tkin.Label(screen, text = str(no_of_rows)+".", width = width_of_slot, font = font_data).grid(row = no_of_rows, column = 0)

    # 'mapping' is a variable used to map the individual slot and then it is appended to 'get_data' list
    mapping = []

    # for loop for four columns of every row
    for individual_slot in range(0,4):

        # method to create slots to enter variables
        mapping.append(tkin.Entry(screen, width = width_of_slot, font = font_data))

        # setting default values as '0'
        mapping[individual_slot].insert(0,"0")

        # positoning of the slot
        mapping[individual_slot].grid(row = no_of_rows, column = 1+individual_slot)
    get_data.append(mapping)

    # defining the deleted buttons in a new positon
    save = tkin.Button(screen, text = "Plot",font = font_data,bg="lightgreen", width = 3)
    save['command'] = lambda scr = screen:save_data(scr)
    save.grid(row = no_of_rows, column = 6)
    add = tkin.Button(screen, text = "+",font = font_data,bg="lightblue", width = 3,command = add_row)
    add['command'] = lambda but1 = add, but2 = save :add_row(but1,but2,screen)
    add.grid(row = no_of_rows, column = 5)


# main function
def DH_Plotter_main():
    # defining a master variable for tkinter gui methode
    screen = tkin.Tk()

    # positon of the window of GUI
    screen.geometry("+0+10")

    # title of the window
    screen.title("DH Table Convertor")

    # initial lables of the GUI
    tkin.Label(screen,text = "Enter The values ")
    tkin.Label(screen,text = "Link No.",width=width_of_slot,font = font_data).grid(row = 0, column = 0)
    tkin.Label(screen,text = "Theta",width=width_of_slot,font = font_data).grid(row = 0, column = 1)
    tkin.Label(screen,text = "Z_dis",width=width_of_slot,font = font_data).grid(row = 0, column = 2)
    tkin.Label(screen,text = "X_dis",width=width_of_slot,font = font_data).grid(row = 0, column = 3)
    tkin.Label(screen,text = "Alpha",width=width_of_slot,font = font_data).grid(row = 0, column = 4)

    # defining both buttons for the first time
    save = tkin.Button(screen, text = "Plot",font = font_data, bg="lightgreen", width = 3, command = save_data)
    save.grid(row = no_of_rows, column = 6)
    add = tkin.Button(screen, text = "+", font = font_data, width = 3, bg="lightblue")
    add['command'] = lambda but1 = add, but2 = save :add_row(but1,but2,screen)
    add.grid(row = no_of_rows, column = 5)

    # calling mainloop
    screen.mainloop()
