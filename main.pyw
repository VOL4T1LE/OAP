
#? NOTICE
#? This file uses the "Better Comments" extension for Visual Studio Code.



# Import the custom modules stored in the local 'Assets' directory
from Assets import variables as vars
from Assets import commands as cmds
from Assets import aliases as alss
from Assets import procedures as proc

# Import the 'tkinter' module to facilitate the creation of an application window
import tkinter as tk
from tkinter import *

# Import the 'os' module to handle file-pathing
import os

# Import the 'datetime' module to handle the LIFEPAK 15's clock
from datetime import datetime





# Create a class (Blueprint) for all future instances of the op-aid program
class Root_Window():

    # Define all initialisations of each OAP instance
    def __init__(self, master):

        # Define the __init__ method's parent as 'master'
        self.master = master

        # Configure the properties of the root window
        master.title(f"{vars.Service_Name}  |  {vars.Program_Title}  |  {vars.Program_Version}")
        master.geometry("550x300+5+10")
        master.resizable(False, False)
        master.attributes("-topmost", 1)
        master.configure(background = "#223D29", highlightthickness = 0)

        # Set the focus on the OAP following initialisation
        master.focus

        # Create empty arrays for each set of widgets for future appendment
        self.Current_Page_Widgets = []
        self.Procedure_Page_Widgets = []
        self.Memory_Aids_Page_Widgets = []
        self.LIFEPAK_15_Page_Widgets = []

        # Define all the necessary string variables for the OAP
        self.Procedure_Entry_Field_Variable = StringVar()
        self.Procedure_Entry_Field_Variable.set(" Please enter the name of the desired procedure")
        self.Procedure_Descriptor_One = StringVar()
        self.Procedure_Descriptor_One.set("")
        self.Procedure_Descriptor_Two = StringVar()
        self.Procedure_Descriptor_Two.set("")
        self.Procedure_Descriptor_Three = StringVar()
        self.Procedure_Descriptor_Three.set("")
        self.Memory_Aids_Entry_Field_Variable = StringVar()
        self.Memory_Aids_Entry_Field_Variable.set(" What do you need help with?")
        self.Memory_Aids_Descriptor_Variable = StringVar()
        self.Memory_Aids_Descriptor_Variable.set("")
        self.LIFEPAK_15_Clock_Variable = StringVar()
        self.LIFEPAK_15_Clock_Variable.set("TIME PLACEHOLDER")

        # Call the defined 'Create_Widgets' function to create all of the OAPs widgets
        self.Create_Widgets()

    # Define a function to create all of the OAP's widgets
    def Create_Widgets(self):

        # Define the event function called when a user click's the procedure entry field
        def Procedure_Entry_Field_Click(event):
            self.Procedure_Entry_Field_Variable.set("")

        # Define the event function called when a user modifies their procedure entry input with the Control + Backspace key combination
        def Procedure_Control_Backspace_Event(event):
            End_Index = self.Procedure_Entry_Field.index(tk.INSERT)
            Start_Index = self.Procedure_Entry_Field.get().rfind(" ", None, End_Index)
            self.Procedure_Entry_Field.selection_range(Start_Index, End_Index)

        # Define the event function called when a user submits their procedure entry
        def Procedure_Entry_Submit(event):
            Entry_Input = self.Procedure_Entry_Field_Variable.get()
            if Entry_Input in alss.Procedure_Aliases:
                self.First_Procedure_Desc_Label.config(
                    font = ("Verdana", 11),
                    fg = "White"
                )
                Entry_Alias = alss.Procedure_Aliases[Entry_Input]
                Entry_Filename = proc.Procedure_Details[Entry_Alias]["File"]
                Entry_Type = proc.Procedure_Details[Entry_Alias]["Type"]
                Entry_Clinical_Level = proc.Procedure_Details[Entry_Alias]["Skill"]
                Entry_Procedure_ID = proc.Procedure_Details[Entry_Alias]["Procedure ID"]
                self.Procedure_Descriptor_One.set(f"Type of Procedure:   {Entry_Type}")
                self.Procedure_Descriptor_Two.set(f"Clinical Level:   {Entry_Clinical_Level}")
                self.Procedure_Descriptor_Three.set(f"Procedure ID:   {Entry_Procedure_ID}")
                Current_Directory = os.getcwd()
                if vars.Auto_Access_Procedures == True:
                    os.startfile(f"{Current_Directory}/Procedures/{Entry_Filename}")
                else:
                    pass
            elif Entry_Input in proc.Procedure_IDs:
                self.First_Procedure_Desc_Label.config(
                    font = ("Verdana", 11),
                    fg = "White"
                )
                Procedure_Linked_To_ID = proc.Procedure_IDs[Entry_Input]
                Entry_Filename = proc.Procedure_Details[Procedure_Linked_To_ID]["File"]
                Entry_Type = proc.Procedure_Details[Procedure_Linked_To_ID]["Type"]
                Entry_Clinical_Level = proc.Procedure_Details[Procedure_Linked_To_ID]["Skill"]
                Entry_Procedure_ID = Entry_Input
                self.Procedure_Descriptor_One.set(f"Type of Procedure:   {Entry_Type}")
                self.Procedure_Descriptor_Two.set(f"Clinical Level:   {Entry_Clinical_Level}")
                self.Procedure_Descriptor_Three.set(f"Procedure ID:   {Entry_Procedure_ID}")
                Current_Directory = os.getcwd()
                if vars.Auto_Access_Procedures == True:
                    os.startfile(f"{Current_Directory}/procedures/{Entry_Filename}")
                else:
                    pass
            elif Entry_Input in alss.Memory_Aid_Aliases:
                self.First_Procedure_Desc_Label.config(
                    font = ("Verdana", 10),
                    fg = "White"
                )
                if len(Entry_Input) < 7:
                    self.Procedure_Descriptor_One.set(f"Please try search for '{Entry_Input}' using the 'Memory Aids' search utility instead")
                else:
                    self.Procedure_Descriptor_One.set(f"Please use the 'Memory Aids' search utility to look for:\n\n'{Entry_Input}'")
                self.Procedure_Descriptor_Two.set("")
                self.Procedure_Descriptor_Three.set("")
            else:
                self.First_Procedure_Desc_Label.config(
                    font = ("Verdana Bold", 12),
                    fg = "White"
                )
                self.Procedure_Descriptor_One.set("Procedure Not Found.")
                self.Procedure_Descriptor_Two.set("")
                self.Procedure_Descriptor_Three.set("")

        # Define the event function called when a user click's the memory aids entry field
        def Memory_Aids_Entry_Field_Click(event):
            self.Memory_Aids_Entry_Field_Variable.set("")

        # Define the event function called when a user modifies their memory aids entry input with the Control + Backspace key combination
        def MA_Control_Backspace_Event(event):
            End_Index = self.Memory_Aids_Entry_Field.index(tk.INSERT)
            Start_Index = self.Memory_Aids_Entry_Field.get().rfind(" ", None, End_Index)
            self.Memory_Aids_Entry_Field.selection_range(Start_Index, End_Index)

        # Define the event function called when a user submits their previous entry
        def Memory_Aids_Entry_Submit(event):
            Entry_Input = self.Memory_Aids_Entry_Field_Variable.get()
            if Entry_Input in alss.Memory_Aid_Aliases:
                self.Memory_Aids_Descriptor_Label.config(font = ("Verdana Bold", 12))
                self.Memory_Aids_Descriptor_Variable.set("")
                Entry_Filename = alss.Memory_Aid_Aliases[Entry_Input]
                Current_Directory = os.getcwd()
                os.startfile(f"{Current_Directory}/Memory Aids/{Entry_Filename}")
            elif Entry_Input in alss.Procedure_Aliases:
                self.Memory_Aids_Descriptor_Label.config(font = ("Verdana", 10))
                if len(Entry_Input) < 10:
                    self.Memory_Aids_Descriptor_Variable.set(f"Please search for '{Entry_Input}' using the 'Procedures' search utility instead")
                else:
                    self.Memory_Aids_Descriptor_Variable.set(f"Please use the 'Procedures' search utility to look for:\n'{Entry_Input}'")
            elif Entry_Input in proc.Procedure_IDs:
                self.Memory_Aids_Descriptor_Label.config(font = ("Verdana", 10))
                if len(Entry_Input) < 10:
                    self.Memory_Aids_Descriptor_Variable.set(f"Please search for '{Entry_Input}' using the 'Procedures' search utility instead")
                else:
                    self.Memory_Aids_Descriptor_Variable.set(f"Please use the 'Procedures' search utility to look for:\n\n'{Entry_Input}'")
            else:
                self.Memory_Aids_Descriptor_Label.config(font = ("Verdana Bold", 12))
                self.Memory_Aids_Descriptor_Variable.set("Memory Aid Not Found")

        # Create a custom exit button linked to an exit command, modified by the 'variables' custom module
        self.Window_Exit_Button = Button(
            master = self.master,
            text = "Click to exit",
            font = ("Arial Bold", 11),
            fg = "White",
            bg = "Dark Red",
            activeforeground = "Dark Red",
            activebackground = "White",
            borderwidth = 0,
            padx = 5,
            pady = 3,
            command = cmds.Exit_Root_Window
        )

        # Create a selection button for the 'Procedures' page of the OAP, linked to a page selection command
        self.Procedure_Selection_Button = Button(
            master = self.master,
            text = "Procedures",
            font = ("Arial Bold", 11),
            fg = "White",
            bg = "#162119",
            borderwidth = 0,
            padx = 5,
            pady = 3,
            command = self.Show_Procedure_Page
        )

        # Create a selection button for the 'Memory Aid' page of the OAP, linked to a page selection command
        self.Memory_Aids_Selection_Button = Button(
            master = self.master,
            text = "Memory Aids",
            font = ("Arial Bold", 11),
            fg = "White",
            bg = "#162119",
            borderwidth = 0,
            padx = 5,
            pady = 3,
            command = self.Show_Memory_Aids_Page
        )

        # Create a selection button for the 'LIFEPAK 15' page of the OAP, linked to a page selection command
        self.LIFEPAK_15_Selection_Button = Button(
            master = self.master,
            text = "LIFEPAK 15",
            font = ("Arial Bold", 11),
            fg = "White",
            bg = "#162119",
            borderwidth = 0,
            padx = 5,
            pady = 3,
            command = self.Show_LIFEPAK_15_Page
        )

        # Position the 'Procedures' selection button at the top left of the root window
        self.Procedure_Selection_Button.pack(
            anchor = N,
            side = LEFT
        )

        # Position the 'Memory Aids' selection button to the left of the 'Procedures' button
        self.Memory_Aids_Selection_Button.pack(
            anchor = N,
            side = LEFT
        )

        # Position the 'LIFEPAK 15' selection button to the left of the 'Memory Aids' button
        self.LIFEPAK_15_Selection_Button.pack(
            anchor = N,
            side = LEFT
        )

        # Position the custom exit button at the top left of the root window
        self.Window_Exit_Button.pack(
            anchor = N,
            fill = X
        )

        # Create an entry field for the 'Procedures' page
        self.Procedure_Entry_Field = Entry(
            master = self.master,
            takefocus = False,
            textvariable = self.Procedure_Entry_Field_Variable,
            font = ("Verdana", 11),
            width = 41,
            fg = "#162119",
            bg = "#78BF8B",
            borderwidth = 0
        )

        # Create a submission button for the 'Procedures' page, bound to a command later on
        self.Procedure_Submission_Button = Button(
            master = self.master,
            text = "Submit",
            font = ("Verdana Bold", 10),
            fg = "#162119",
            bg = "#78BF8B",
            borderwidth = 0
        )

        # Create the first (top) descriptor label for the 'Procedures' page
        self.First_Procedure_Desc_Label = Label(
            master = self.master,
            textvariable = self.Procedure_Descriptor_One,
            font = ("Verdana", 11),
            fg = "White",
            bg = "#223D29"
        )

        # Create the second (middle) descriptor label for the 'Procedures' page
        self.Second_Procedure_Desc_Label = Label(
            master = self.master,
            textvariable = self.Procedure_Descriptor_Two,
            font = ("Verdana", 11),
            fg = "White",
            bg = "#223D29"
        )

        # Create the final (bottom) descriptor label for the 'Procedures' page
        self.Third_Procedure_Desc_Label = Label(
            master = self.master,
            textvariable = self.Procedure_Descriptor_Three,
            font = ("Verdana", 11),
            fg = "White",
            bg = "#223D29"
        )

        # Create an entry field for the 'Memory Aids' page
        self.Memory_Aids_Entry_Field = Entry(
            master = self.master,
            takefocus = False,
            textvariable = self.Memory_Aids_Entry_Field_Variable,
            font = ("Verdana", 11),
            width = 41,
            fg = "#162119",
            bg = "#78BF8B",
            borderwidth = 0
        )

        # Create a submission button for the 'Memory Aids' page, bound to a command later on
        self.Memory_Aids_Submission_Button = Button(
            master = self.master,
            text = "Submit",
            font = ("Verdana Bold", 10),
            fg = "#162119",
            bg = "#78BF8B",
            borderwidth = 0
        )

        # Create a descriptor label for the 'Memory Aids' page
        self.Memory_Aids_Descriptor_Label = Label(
            master = self.master,
            textvariable = self.Memory_Aids_Descriptor_Variable,
            font = ("Verdana Bold", 12),
            fg = "White",
            bg = "#223D29"
        )

        # Create a label with a textvariable to act as a clock for the 'LIFEPAK 15' page
        self.LIFEPAK_15_Clock_Label = Label(
            master = self.master,
            textvariable = self.LIFEPAK_15_Clock_Variable,
            font = ("System", 14),
            fg = "#02F78D",
            bg = "#041636",
            pady = 5,
            width = 82
        )


        # Create a 'HR' header label for the 'LIFEPAK 15' page
        self.HR_Header_Label = Label(
            master = self.master,
            text = "HR",
            font = ("Arial Bold", 11),
            fg = "#02F78D",
            bg = "#041636"
        )

        # Create a frame to hold all of the vital sign displays for the 'LIFEPAK 15' page
        self.Vitals_Frame = Frame(
            master = self.master,
            bg = "#041636",
            height = 338,
            width = 170
        )

        # Create a frame to hold the Pulse vital entry field for the 'LIFEPAK 15' page
        self.Pulse_Vitals_Frame = Frame(
            master = self.Vitals_Frame,
            bg = "Black",
            height = 100,
            width = 166
        )

        # Create a 'SpO2' header label for the 'LIFEPAK 15' page
        self.SpO2_Header_Label = Label(
            master = self.Vitals_Frame,
            text = "SpO2",
            font = ("Arial Bold", 11),
            fg = "#03BAFC",
            bg = "#041636"
        )

        # Create a frame to hold the SpO2 vital entry field for the 'LIFEPAK 15' page
        self.SpO2_Vitals_Frame = Frame(
            master = self.Vitals_Frame,
            bg = "Black",
            height = 100,
            width = 166
        )

        # Bind certain procedure entry field key / button actions to commands
        self.Procedure_Entry_Field.bind("<Button-1>", Procedure_Entry_Field_Click)
        self.Procedure_Entry_Field.bind("<FocusIn>", Procedure_Entry_Field_Click)
        self.Procedure_Entry_Field.bind("<Return>", Procedure_Entry_Submit)
        self.Procedure_Entry_Field.bind("<Control-BackSpace>", Procedure_Control_Backspace_Event)
        self.Procedure_Submission_Button.bind("<Button-1>", Procedure_Entry_Submit)
        self.Memory_Aids_Entry_Field.bind("<Button-1>", Memory_Aids_Entry_Field_Click)
        self.Memory_Aids_Entry_Field.bind("<FocusIn>", Memory_Aids_Entry_Field_Click)
        self.Memory_Aids_Entry_Field.bind("<Return>", Memory_Aids_Entry_Submit)
        self.Memory_Aids_Entry_Field.bind("<Control-BackSpace>", MA_Control_Backspace_Event)
        self.Memory_Aids_Submission_Button.bind("<Button-1>", Memory_Aids_Entry_Submit)

        # Append all necessary widgets to their respective arrays
        self.Procedure_Page_Widgets.append(self.Procedure_Entry_Field)
        self.Procedure_Page_Widgets.append(self.Procedure_Submission_Button)
        self.Procedure_Page_Widgets.append(self.First_Procedure_Desc_Label)
        self.Procedure_Page_Widgets.append(self.Second_Procedure_Desc_Label)
        self.Procedure_Page_Widgets.append(self.Third_Procedure_Desc_Label)
        self.Memory_Aids_Page_Widgets.append(self.Memory_Aids_Entry_Field)
        self.Memory_Aids_Page_Widgets.append(self.Memory_Aids_Submission_Button)
        self.Memory_Aids_Page_Widgets.append(self.Memory_Aids_Descriptor_Label)
        self.LIFEPAK_15_Page_Widgets.append(self.LIFEPAK_15_Clock_Label)
        self.LIFEPAK_15_Page_Widgets.append(self.HR_Header_Label)
        self.LIFEPAK_15_Page_Widgets.append(self.Vitals_Frame)
        self.LIFEPAK_15_Page_Widgets.append(self.Pulse_Vitals_Frame)
        self.LIFEPAK_15_Page_Widgets.append(self.SpO2_Header_Label)
        self.LIFEPAK_15_Page_Widgets.append(self.SpO2_Vitals_Frame)

    # Define a custom function to update the LIFEPAK 15's clock widget
    def Update_Clock(self):
        self.Current_Time = datetime.now().strftime("%H : %M : %S")
        self.LIFEPAK_15_Clock_Variable.set(self.Current_Time)
        self.master.after(500, self.Update_Clock)

    # Define the function called when the 'Procedures' page selection button is clicked
    def Show_Procedure_Page(self):

        # Ensure that the correct widgets are displayed in accordance with the user's selection
        if self.Current_Page_Widgets != self.Procedure_Page_Widgets:
            self.Hide_Current_Page_Widgets()
        self.Current_Page_Widgets = self.Procedure_Page_Widgets
        self.Show_Current_Page_Widgets(
            [
            (self.Procedure_Entry_Field, 5, 60),
            (self.Procedure_Submission_Button, 430, 60),
            (self.First_Procedure_Desc_Label, 6, 90),
            (self.Second_Procedure_Desc_Label, 6, 120),
            (self.Third_Procedure_Desc_Label, 6, 150)
            ]
        )

        # Ensure that the window is correctly configured in accordance with the user's selection
        self.master.configure(background = "#223D29")
        self.master.geometry("550x300+5+10")

        # Ensure that the entry field variable is reset
        self.Procedure_Entry_Field_Variable.set(" Please enter the name of the desired procedure")
        self.Procedure_Descriptor_One.set("")
        self.Procedure_Descriptor_Two.set("")
        self.Procedure_Descriptor_Three.set("")

    # Define the function called when the 'Memory Aids' page selection button is clicked
    def Show_Memory_Aids_Page(self):
        if self.Current_Page_Widgets != self.Memory_Aids_Page_Widgets:
            self.Hide_Current_Page_Widgets()
        self.Current_Page_Widgets = self.Memory_Aids_Page_Widgets
        self.Show_Current_Page_Widgets(
            [
            (self.Memory_Aids_Entry_Field, 5, 60),
            (self.Memory_Aids_Submission_Button, 430, 60),
            (self.Memory_Aids_Descriptor_Label, 6, 90)
            ]
        )

        # Ensure that the window is correctly configured in accordance with the user's selection
        self.master.configure(background = "#223D29")
        self.master.geometry("550x300+5+10")

        # Ensure that the entry field variable is reset
        self.Memory_Aids_Entry_Field_Variable.set(" What do you need help with?")

    # Define the function called when the 'LIFEPAK 15' page selection button is clicked
    def Show_LIFEPAK_15_Page(self):
        if self.Current_Page_Widgets != self.LIFEPAK_15_Page_Widgets:
            self.Hide_Current_Page_Widgets()
        self.Current_Page_Widgets = self.LIFEPAK_15_Page_Widgets
        self.Show_Current_Page_Widgets(
            [
            (self.LIFEPAK_15_Clock_Label, 0, 32),
            (self.HR_Header_Label, 2, 36),
            (self.Vitals_Frame, 0, 62),
            (self.Pulse_Vitals_Frame, 2, 0),
            (self.SpO2_Header_Label, 2, 100),
            (self.SpO2_Vitals_Frame, 2, 123)
            ]
        )

        # Ensure that the window is correctly configured in accordance with the user's selection
        self.master.configure(background = "Black")
        self.master.geometry("650x400+5+10")

        # Call the clock update function to update the LIFEPAK 15's current time
        self.Update_Clock()

    # Define the function called to hide all the currently displayed widgets
    def Hide_Current_Page_Widgets(self):
        for widget in self.Current_Page_Widgets:
            widget.place_forget()

    # Define the function called to show all the currently displayed widgets
    def Show_Current_Page_Widgets(self, Widget_Coordinates):
        for widget, x, y in Widget_Coordinates:
            widget.place(x = x, y = y)





#! WARNING
#* Code beyond the application bootstrapping
#* block below will NOT be executed as this
#* is an infinite loop.

if __name__ == "__main__":
    root = tk.Tk()
    Root_Window(root)
    root.mainloop()