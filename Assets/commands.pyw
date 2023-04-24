
#? NOTICE
#? This file uses the "Better Comments" extension for Visual Studio Code.



# Import the custom 'variables' module from the 'Assets' directory
from Assets import variables as vars

# Import the 'tkinter' module to create message boxes
from tkinter import messagebox as mbx





# Define the command called when exiting the root window via the exit widget
def Exit_Root_Window():
    if vars.Exit_Confirmation_Bool == True:
        Root_Exit_Query = mbx.askquestion(
            title = "Exit Program",
            message = "Are you sure you would like to exit?",
            default = "no"
        )

        if Root_Exit_Query == "yes":
            exit()
        else:
            pass
    else:
        exit()