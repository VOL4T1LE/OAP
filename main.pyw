
#! WARNING
#* This file uses the "Better Comments" extension for Visual Studio Code.


#* Import necessary modules
import tkinter as tk
from tkinter import *
import procDictionary as pCD
import os

#* Declaration of global variables
appVersion = "V1.0.3a"
appTitle = "Operational Aid Program"
serviceName = "London Ambulance Service"

#* Create the root tkinter window as a class
class rootWindow():
    def __init__(self, master):

        #* Declaration of class variables - these may be accessed using dot notation ;)
        self.master = master

        #* Configure the root tkinter window's attributes
        master.title(f"{serviceName}  |  {appTitle}  |  {appVersion}")
        master.geometry("600x250+10+10")
        master.resizable(False, False)
        master.attributes("-topmost", 1)
        master.configure(background = "Black", highlightthickness = 0)
        master.iconbitmap("./assets/logo.ico")
        master.focus

        #* Declaration of string variables
        entryFieldVariable = StringVar()
        entryFieldVariable.set(" Enter the name of the procedure")
        procDescOne = StringVar()
        procDescOne.set("")
        procDescTwo = StringVar()
        procDescTwo.set("")

        #* Definition of "on-click" commands
        def onProcedureEntryFieldClick(event):
            entryFieldVariable.set("")

        def controlBackspaceEvent(event):
            endIndex = self.procedureEntryField.index(tk.INSERT)
            startIndex = self.procedureEntryField.get().rfind(" ", None, endIndex)
            self.procedureEntryField.selection_range(startIndex, endIndex)

        def onSubmitProcedureEntryClick(event):
            entryInput = entryFieldVariable.get()
            if entryInput in pCD.procedures:
                procFile = pCD.procedures[entryInput]['file']
                currentDir = os.getcwd()
                self.procedureDescOne.config(
                    font = ("Verdana", 11),
                    fg = "White"
                )
                setProcDescOne = pCD.procedures[entryInput]['type']
                setProcDescTwo = pCD.procedures[entryInput]['skill']
                procDescOne.set(f" Type of Procedure:   {setProcDescOne}")
                procDescTwo.set(f" Clinical Level:   {setProcDescTwo}")
                os.startfile(f"{currentDir}/assets/procedures/{procFile}")
            else:
                self.procedureDescOne.config(
                    font = ("Verdana Bold", 14),
                    fg = "Dark Red"
                )
                procDescOne.set("Procedure Not Found")
                procDescTwo.set("")


        self.rootFrame = Frame(
            master,
            bg = "Sea Green"
        )

        self.headerFrame = Frame(
            self.rootFrame, 
            bg = "Brown4",
            height = 200
        )

        self.headerLabel = Label(
            self.headerFrame,
            text = f"{appTitle}",
            font = ("Verdana Bold", 17),
            fg = "White",
            bg = "Brown4"
        )

        self.procedureEntryLabel = Label(
            self.rootFrame,
            text = "Desired Procedure",
            font = ("Verdana Bold", 12),
            fg = "White",
            bg = "Sea Green"
        )

        self.procedureEntryField = Entry(
            self.rootFrame,
            takefocus = False,
            textvariable = entryFieldVariable,
            font = ("Verdana", 11),
            width = 41,
            fg = "Coral1",
            bg = "Brown4"
        )
        self.procedureEntryField.bind("<Button-1>", onProcedureEntryFieldClick)
        self.procedureEntryField.bind("<Return>", onSubmitProcedureEntryClick)
        self.procedureEntryField.bind("<Control-BackSpace>", controlBackspaceEvent)

        self.submitProcedureEntry = Button(
            text = "Submit",
            font = ("Verdana Bold", 10),
            fg = "Dark Sea Green",
            bg = "Brown4"
        )
        self.submitProcedureEntry.bind("<Button-1>", onSubmitProcedureEntryClick)

        self.procedureDescOne = Label(
            self.rootFrame,
            textvariable = procDescOne,
            font = ("Verdana", 11),
            fg = "White",
            bg = "Sea Green"
        )

        self.procedureDescTwo = Label(
            self.rootFrame,
            textvariable = procDescTwo,
            font = ("Verdana", 11),
            fg = "White",
            bg = "Sea Green"
        )

        #* Place the rootFrame followed by any widgets under it
        self.rootFrame.pack(
            expand = TRUE,
            fill = BOTH
        )
        self.headerFrame.pack(
            side = TOP,
            fill = X
        )
        self.headerLabel.pack(
            side = LEFT,
            padx = 5
        )
        self.procedureEntryLabel.place(
            x = 5,
            y = 40
        )
        self.procedureEntryField.place(
            x = 10,
            y = 65
        )
        self.submitProcedureEntry.place(
            x = 430,
            y = 63
        )
        self.procedureDescOne.place(
            x = 5,
            y = 100
        )
        self.procedureDescTwo.place(
            x = 5,
            y = 130
        )

#! WARNING
#* Code beyond the application bootstrapping
#* block below will NOT be executed as this
#* is an infinite loop.

def main():
    root = tk.Tk()
    app = rootWindow(root)
    root.mainloop()

if __name__ == "__main__":
    main()
