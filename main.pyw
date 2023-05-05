
#? NOTICE
#? This file uses the "Better Comments" extension for Visual Studio Code.



# Import the custom modules stored in the local 'Assets' directory
from Assets import variables as vars
from Assets import commands as cmds
from Assets import aliases as alss
from Assets import procedures as proc
from ecg_data import nsr_data

# Import the 'tkinter' module to facilitate the creation of an application window
import tkinter as tk
from tkinter import *

# Import the 'os' module to handle file-pathing
import os

# Import the 'datetime' module to handle the LIFEPAK 15's clock
from datetime import datetime

# Import the 'math' and 'random' modules
import math
import random





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
        master.iconbitmap("./Media/LAS Logo.ico")
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
        self.Heart_Rate_Variable = StringVar()
        self.Heart_Rate_Variable.set("---")
        self.SpO2_Variable = StringVar()
        self.SpO2_Variable.set("---")
        self.Systolic_NIBP_Variable = StringVar()
        self.Systolic_NIBP_Variable.set("---")
        self.Diastolic_NIBP_Variable = StringVar()
        self.Diastolic_NIBP_Variable.set("---")
        self.Mean_Arterial_Pressure_Variable = StringVar()
        self.Mean_Arterial_Pressure_Variable.set("")

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

        # Define the event called when a user clicks the Heart Rate entry field
        def Heart_Rate_Entry_Field_Click(event):
            self.Heart_Rate_Variable.set("")

        # Define the event called when a user clicks the SpO2 entry field
        def SpO2_Entry_Field_Click(event):
            self.SpO2_Variable.set("")

        # Define the event called when a user clicks the Systolic NIBP entry field
        def Systolic_NIBP_Entry_Field_Click(event):
            self.Systolic_NIBP_Variable.set("")

        # Define the event called when a user clicks the Diastolic NIBP entry field
        def Diastolic_NIBP_Entry_Field_Click(event):
            self.Diastolic_NIBP_Variable.set("")

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
            pady = 1,
            width = 82
        )

        # Create a 'HR' header label for the 'LIFEPAK 15' page
        self.HR_Header_Label = Label(
            master = self.master,
            text = "HR",
            font = ("Consolas Bold", 11),
            fg = "#02F78D",
            bg = "#041636"
        )

        # Create a frame to hold all of the vital sign displays for the 'LIFEPAK 15' page
        self.Vitals_Frame = Frame(
            master = self.master,
            bg = "#041636",
            height = 349,
            width = 170
        )

        # Create a frame to hold the 'Heart Rate' vitals entry field for the 'LIFEPAK 15' page
        self.Heart_Rate_Vitals_Frame = Frame(
            master = self.Vitals_Frame,
            bg = "Black",
            height = 100,
            width = 164
        )

        # Create a vitals entry field for users to input a 'Heart Rate' value for the 'LIFEPAK 15' page
        self.Heart_Rate_Entry_Field = Entry(
            master = self.Heart_Rate_Vitals_Frame,
            textvariable = self.Heart_Rate_Variable,
            font = ("Consolas Bold", 42),
            fg = "#02F78D",
            bg = "Black",
            borderwidth = 0,
            width = 3,
            justify = "right",
            validate = "key"
        )

        # Create a 'SpO2' header label for the 'LIFEPAK 15' page
        self.SpO2_Header_Label = Label(
            master = self.Vitals_Frame,
            text = "SpO2",
            font = ("Consolas Bold", 11),
            fg = "#02A3FA",
            bg = "#041636"
        )

        # Create a second header detailing the SpO2 reading's unit of measurement for the 'LIFEPAK 15' page
        self.SpO2_Unit_Label = Label(
            master = self.Vitals_Frame,
            text = "%",
            font = ("Consolas", 10),
            fg = "#02A3FA",
            bg = "#041636"
        )

        # Create a frame to hold the SpO2 vital entry field for the 'LIFEPAK 15' page
        self.SpO2_Vitals_Frame = Frame(
            master = self.Vitals_Frame,
            bg = "Black",
            height = 100,
            width = 164
        )

        # Create a vitals entry field for users to input a 'SpO2' value for the 'LIFEPAK 15' page
        self.SpO2_Entry_Field = Entry(
            master = self.SpO2_Vitals_Frame,
            textvariable = self.SpO2_Variable,
            font = ("Consolas Bold", 38),
            fg = "#02A3FA",
            bg = "Black",
            borderwidth = 0,
            width = 3,
            justify = "right",
            validate = "key"
        )

        # Create a 'NIBP' header label for the 'LIFEPAK 15' page
        self.NIBP_Header_Label = Label(
            master = self.Vitals_Frame,
            text = "NIBP",
            font = ("Consolas Bold", 11),
            fg = "#03F4FC",
            bg = "#041636"
        )

        # Create a second header detailing the NIBP reading's unit of measurement for the 'LIFEPAK 15' page
        self.NIBP_Unit_Label = Label(
            master = self.Vitals_Frame,
            text = "mmHg",
            font = ("Consolas", 10),
            fg = "#03F4FC",
            bg = "#041636"
        )

        # Create a frame to hold the NIBP vital entry fields and MAP for the 'LIFEPAK 15' page
        self.NIBP_Vitals_Frame = Frame(
            master = self.Vitals_Frame,
            bg = "Black",
            height = 100,
            width = 164
        )

        # Create a vitals entry field for users to input a 'Systolic NIBP' value for the 'LIFEPAK 15' page
        self.Systolic_NIBP_Entry_Field = Entry(
            master = self.NIBP_Vitals_Frame,
            textvariable = self.Systolic_NIBP_Variable,
            font = ("Consolas Bold", 32),
            fg = "#03F4FC",
            bg = "Black",
            borderwidth = 0,
            width = 3,
            justify = "right",
            validate = "key"
        )

        # Create a vitals entry field for users to input a 'Diastolic NIBP' value for the 'LIFEPAK 15' page
        self.Diastolic_NIBP_Entry_Field = Entry(
            master = self.NIBP_Vitals_Frame,
            textvariable = self.Diastolic_NIBP_Variable,
            font = ("Consolas Bold", 32),
            fg = "#03F4FC",
            bg = "Black",
            borderwidth = 0,
            width = 3,
            justify = "right",
            validate = "key"
        )

        # Create a label to display the calculated Mean Arterial Pressure on the 'LIFEPAK 15' page
        self.Calculated_MAP_Display_Label = Label(
            master = self.NIBP_Vitals_Frame,
            textvariable = self.Mean_Arterial_Pressure_Variable,
            font = ("Consolas Bold", 18),
            fg = "#03F4FC",
            bg = "Black"
        )

        # Create a canvas widget to facilitate the graphical plotting of an ECG tracing on the 'LIFEPAK 15' page
        self.ECG_Tracing_Canvas = Canvas(
            self.master,
            width = 475,
            height = 95,
            background = "Black",
            borderwidth = 0,
            highlightbackground = "Yellow",
            highlightthickness = 0
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
        self.Heart_Rate_Entry_Field.bind("<Button-1>", Heart_Rate_Entry_Field_Click)
        self.SpO2_Entry_Field.bind("<Button-1>", SpO2_Entry_Field_Click)
        self.Systolic_NIBP_Entry_Field.bind("<Button-1>", Systolic_NIBP_Entry_Field_Click)
        self.Diastolic_NIBP_Entry_Field.bind("<Button-1>", Diastolic_NIBP_Entry_Field_Click)

        # Associate certain entry fields to their respective validate commands
        self.Heart_Rate_Entry_Field.configure(validatecommand = (self.master.register(self.Validate_Heart_Rate_Input), "%P"))
        self.SpO2_Entry_Field.configure(validatecommand = (self.master.register(self.Validate_SpO2_Input), "%P"))
        self.Systolic_NIBP_Entry_Field.configure(validatecommand = (self.master.register(self.Validate_Systolic_Input), "%P"))
        self.Diastolic_NIBP_Entry_Field.configure(validatecommand = (self.master.register(self.Validate_Diastolic_Input), "%P"))

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
        self.LIFEPAK_15_Page_Widgets.append(self.Heart_Rate_Vitals_Frame)
        self.LIFEPAK_15_Page_Widgets.append(self.Heart_Rate_Entry_Field)
        self.LIFEPAK_15_Page_Widgets.append(self.SpO2_Header_Label)
        self.LIFEPAK_15_Page_Widgets.append(self.SpO2_Unit_Label)
        self.LIFEPAK_15_Page_Widgets.append(self.SpO2_Vitals_Frame)
        self.LIFEPAK_15_Page_Widgets.append(self.SpO2_Entry_Field)
        self.LIFEPAK_15_Page_Widgets.append(self.NIBP_Header_Label)
        self.LIFEPAK_15_Page_Widgets.append(self.NIBP_Unit_Label)
        self.LIFEPAK_15_Page_Widgets.append(self.NIBP_Vitals_Frame)
        self.LIFEPAK_15_Page_Widgets.append(self.Systolic_NIBP_Entry_Field)
        self.LIFEPAK_15_Page_Widgets.append(self.Diastolic_NIBP_Entry_Field)
        self.LIFEPAK_15_Page_Widgets.append(self.Calculated_MAP_Display_Label)
        self.LIFEPAK_15_Page_Widgets.append(self.ECG_Tracing_Canvas)

    # Define a custom function to handle ECG tracing updates
    def Update_ECG_Tracing(self):

        # Clear any previous ECG tracings
        self.ECG_Tracing_Canvas.delete("all")

        # Get the current value input into the Heart Rate vitals entry field
        Heart_Rate = self.Heart_Rate_Entry_Field.get()
        
        # Specify canvas dimensions
        Canvas_Length = 475
        Canvas_Centre_Height = 47.5

        # Draw a flat isoelectric line under relevant conditions
        if not Heart_Rate or Heart_Rate == "---" or int(Heart_Rate) == 0:

            # Draw a flat isoelectric line on the ECG tracing canvas widget
            self.ECG_Tracing_Canvas.create_line(0, Canvas_Centre_Height, Canvas_Length, Canvas_Centre_Height, fill = "Yellow")
        else:

            # Specify initial tracing coordinates
            x = random.uniform(0, 60)
            y = 47.5

            # Clear any previous ECG tracings
            self.ECG_Tracing_Canvas.delete("all")

            # Create an array to store the final coordinates of each PQRST complex
            Final_Coords = [(x, y)]

            # Calculate the number of PQRST complexes to be displayed
            Number_Of_Complexes = int(Heart_Rate) // 6

            # Create for loop to iterate through heart rate and create appropriate amount of ECG complexes
            if Number_Of_Complexes == 0:
                self.ECG_Tracing_Canvas.delete("all")
                self.ECG_Tracing_Canvas.create_line(0, Canvas_Centre_Height, Canvas_Length, Canvas_Centre_Height, fill = "Yellow")
            else:
                for i in range(Number_Of_Complexes):

                    # Define a random uniform length for each TP interval
                    TPL = random.uniform(60, 100)

                    if i == 0:
                        pass
                    else:

                        # Define a random length for each TP interval
                        if i == 0:
                            TPL = random.uniform(60, 100)
                        else:
                            TPL = random.uniform(60, 120)

                        if i == 0:
                            # Prevent gap at start of ECG trace
                            x += TPL
                        else:
                            # Set starting coordinates to end of next PQRST complex
                            x, y = Final_Coords[- 1]

                        # Create PQRST data array
                        ECG_Deflection_Data = []

                        # Construct P wave and a PR segment
                        ECG_Deflection_Data.append(
                            [
                                x + 0, y - 0,       # End of TP interval
                                x + 7, y - 0,       # Start of P wave deflection
                                x + 9, y - 2,
                                x + 11, y - 3,      # Peak of P wave deflection
                                x + 13, y - 2,
                                x + 15, y - 0,      # End of P wave deflection, beginning of PR segment
                                x + 19, y - 0       # End of PR segment
                            ]
                        )

                        # Construct a QRS complex followed by a T wave
                        ECG_Deflection_Data.append(
                            [
                                x + 22, y + 8,      # Q deflection
                                x + 25, y - 29,     # R deflection
                                x + 27, y + 14,     # S deflection
                                x + 30, y + 1,      # J point
                                x + 35, y - 1,      # ST segment
                                x + 37, y - 4,
                                x + 40, y - 6,      # Peak of T wave deflection
                                x + 43, y - 4,
                                x + 45, y - 0,      # End of T wave deflection, beginning of TP interval
                                x + TPL, y - 0,     # End of PQRST complex (TP interval included)
                            ]
                        )

                        # Create ECG tracing using wave deflection data provided
                        self.ECG_Tracing_Canvas.create_line(ECG_Deflection_Data, fill = "Yellow", width = 1)
                        
                        # Append final coords to appropriate array, to be used as starting point of next complex
                        Final_Coords.append((x + 45, y))

        # Begin an infinite loop, facilitating constant updating of the ECG tracing
        self.master.after(500, self.Update_ECG_Tracing)

    # Define a custom function to update the LIFEPAK 15's clock widget
    def Update_Clock(self):
        self.Current_Time = datetime.now().strftime("%H : %M : %S")
        self.LIFEPAK_15_Clock_Variable.set(self.Current_Time)
        self.master.after(500, self.Update_Clock)

    # Define a custom function to calculate and update the MAP value displayed on the 'LIFEPAK 15' page
    def Calculate_MAP(self):
        try:
            Systolic_Value = int(self.Systolic_NIBP_Entry_Field.get())
            Diastolic_Value = int(self.Diastolic_NIBP_Entry_Field.get())
            self.Calculated_MAP_Value = ((Systolic_Value + (2 * Diastolic_Value)) // 3)
            self.Mean_Arterial_Pressure_Variable.set(self.Calculated_MAP_Value)
        except:
            pass
        self.master.after(4000, self.Calculate_MAP)

    # Define a custom validation function to ensure numeric user inputs
    def Validate_Heart_Rate_Input(self, Proposed_Value):
        if Proposed_Value.strip() == "":
            return True
        if "." in Proposed_Value:
            return False
        if len(self.Heart_Rate_Entry_Field.get()) >= 3:
            return False
        try:
            X = float(Proposed_Value)
            if X > 600:
                return False
            else:
                return True
        except ValueError:
            return False
        
    # Define a custom validation function to ensure numeric user inputs
    def Validate_SpO2_Input(self, Proposed_Value):
        if Proposed_Value.strip() == "":
            return True
        if "." in Proposed_Value:
            return False
        if len(self.SpO2_Entry_Field.get()) >= 3:
            return False
        try:
            X = float(Proposed_Value)
            if X > 100:
                return False
            else:
                return True
        except ValueError:
            return False
        
    # Define a custom validation function to ensure numeric user inputs
    def Validate_Systolic_Input(self, Proposed_Value):
        if Proposed_Value.strip() == "":
            return True
        if "." in Proposed_Value:
            return False
        if len(self.Systolic_NIBP_Entry_Field.get()) >= 3:
            return False
        try:
            X = float(Proposed_Value)
            if X > 370:
                return False
            else:
                return True
        except ValueError:
            return False
    
    # Define a custom validation function to ensure numeric user inputs
    def Validate_Diastolic_Input(self, Proposed_Value):
        if Proposed_Value.strip() == "":
            return True
        if "." in Proposed_Value:
            return False
        if len(self.Diastolic_NIBP_Entry_Field.get()) >= 3:
            return False
        try:
            X = float(Proposed_Value)
            if X > 360:
                return False
            else:
                return True
        except ValueError:
            return False

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
        self.master.geometry("550x300")
        self.master.iconbitmap("./Media/LAS Logo.ico")
        self.master.configure(background = "#223D29")

        # Ensure that the entry field variable is reset
        self.Procedure_Entry_Field_Variable.set(" Please enter the name of the desired procedure")
        self.Procedure_Descriptor_One.set("")
        self.Procedure_Descriptor_Two.set("")
        self.Procedure_Descriptor_Three.set("")

    # Define the function called when the 'Memory Aids' page selection button is clicked
    def Show_Memory_Aids_Page(self):

        # Ensure that the correct widgets are displayed in accordance with the user's selection
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
        self.master.geometry("550x300")
        self.master.iconbitmap("./Media/LAS Logo.ico")
        self.master.configure(background = "#223D29")

        # Ensure that the entry field variable is reset
        self.Memory_Aids_Entry_Field_Variable.set(" What do you need help with?")

    # Define the function called when the 'LIFEPAK 15' page selection button is clicked
    def Show_LIFEPAK_15_Page(self):

        # Ensure that the correct widgets are displayed in accordance with the user's selection
        if self.Current_Page_Widgets != self.LIFEPAK_15_Page_Widgets:
            self.Hide_Current_Page_Widgets()
        self.Current_Page_Widgets = self.LIFEPAK_15_Page_Widgets
        self.Show_Current_Page_Widgets(
            [
            (self.LIFEPAK_15_Clock_Label, 0, 32),
            (self.HR_Header_Label, 2, 32),
            (self.Vitals_Frame, 0, 54),
            (self.Heart_Rate_Vitals_Frame, 3, 0),
            (self.Heart_Rate_Entry_Field, 62, 0),
            (self.SpO2_Header_Label, 2, 100),
            (self.SpO2_Unit_Label, 155, 101),
            (self.SpO2_Vitals_Frame, 3, 123),
            (self.SpO2_Entry_Field, 70, 0),
            (self.NIBP_Header_Label, 2, 223),
            (self.NIBP_Unit_Label, 135, 223),
            (self.NIBP_Vitals_Frame, 3, 245),
            (self.Systolic_NIBP_Entry_Field, 85, 0),
            (self.Diastolic_NIBP_Entry_Field, 85, 45),
            (self.Calculated_MAP_Display_Label, 5, 60),
            (self.ECG_Tracing_Canvas, 171, 55)
            ]
        )

        # Ensure that the window is correctly configured in accordance with the user's selection
        self.master.geometry("650x403")
        self.master.iconbitmap("./Media/PhysioControl Logo.ico")
        self.master.configure(background = "Black")

        # Call the clock update function to update the LIFEPAK 15's current time
        self.Update_Clock()

        # Call the function in charge of calculating and updating the MAP strign variable
        self.Calculate_MAP()

        # Call the ECG trace update function to draw a flat isoelectric line and begin an update loop
        self.Update_ECG_Tracing()

        # Correct any blank entry fields to display their appropriate strings
        if self.Heart_Rate_Entry_Field.get() == "":
            self.Heart_Rate_Variable.set("---")
        if self.SpO2_Entry_Field.get() == "":
            self.SpO2_Variable.set("---")
        if self.Systolic_NIBP_Entry_Field.get() == "":
            self.Systolic_NIBP_Variable.set("---")
        if self.Diastolic_NIBP_Entry_Field.get() == "":
            self.Diastolic_NIBP_Variable.set("---")

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