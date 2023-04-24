
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





class Root_Window():
    def __init__(self, master):
        self.master = master

        # Configure the program's root window
        master.title(f"{vars.Service_Name}  |  {vars.Program_Title}  |  {vars.Program_Version}")
        master.geometry("550x300+5+10")
        master.resizable(False, False)
        master.attributes("-topmost", 1)
        master.configure(background = "#223D29", highlightthickness = 0)
        # master.iconbitmap("./Assets/logo.ico")
        self.Create_Widgets()
        self.Position_Widgets()
        master.focus

    def Create_Widgets(self):
        # Create an exit button for the root window of the program, linked to a specific exit command
        self.Exit_Button = Button(
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

        # Create the 'procedure' selection button for the root window of the program
        self.Procedure_Selection_Button = Button(
            master = self.master,
            text = "Procedures",
            font = ("Arial Bold", 11),
            fg = "White",
            bg = "#162119",
            borderwidth = 0,
            padx = 5,
            pady = 3,
            command = self.Create_Procedure_Entry_Field
        )

        # Create the 'Memory Aids' selection button for the root window of the program
        self.Memory_Aid_Selection_Button = Button(
            master = self.master,
            text = "Memory Aids",
            font = ("Arial Bold", 11),
            fg = "White",
            bg = "#162119",
            borderwidth = 0,
            padx = 5,
            pady = 3,
            command = self.Create_MA_Entry_Field
        )
    
        # Create the 'LIFEPAK 15' selection button for the root window of the program
        self.LIFEPAK_Selection_Button = Button(
            master = self.master,
            text = "LIFEPAK 15",
            font = ("Arial Bold", 11),
            fg = "White",
            bg = "#162119",
            borderwidth = 0,
            padx = 5,
            pady = 3,
            command = self.Create_LIFEPAK_15_Window
        )

    def Position_Widgets(self):
        # Position the 'Procedure' selection button aligned with the other selection buttons
        self.Procedure_Selection_Button.pack(
            anchor = N,
            side = LEFT
        )

        # Position the 'Memory Aids' selection button aligned with the other selection buttons
        self.Memory_Aid_Selection_Button.pack(
            anchor = N,
            side = LEFT
        )

        # Position the 'LIFEPAK 15' selection button aligned with the other selection buttons
        self.LIFEPAK_Selection_Button.pack(
            anchor = N,
            side = LEFT
        )

        # Position the root window's exit button aligned with the selection buttons at the top of the root window
        self.Exit_Button.pack(
            fill = X,
            side = TOP
        )

    def Create_Procedure_Entry_Field(self):
        cmds.Select_Procedures()
        try:
            self.MA_Entry_Field.place_forget()
            self.MA_Submission_Button.place_forget()
            self.MemDesc_Label.place_forget()
            self.LIFEPAK_Clock_Label.place_forget()
            self.Vitals_Frame.place_forget()
        except:
            pass
        else:
            pass
        self.master.configure(background = "#223D29")
        self.master.geometry("550x300+5+10")

        # Create the procedure entry field variable, to be used later on
        Procedure_Entry_Field_Variable = StringVar()
        Procedure_Entry_Field_Variable.set(" Enter the name of the procedure")
        Procedure_Descriptor_One = StringVar()
        Procedure_Descriptor_One.set("")
        Procedure_Descriptor_Two = StringVar()
        Procedure_Descriptor_Two.set("")
        Procedure_Descriptor_Three = StringVar()
        Procedure_Descriptor_Three.set("")

        # Set the procedure entry field variable to nothing each time the entry field is clicked
        def On_Procedure_Entry_Field_Click(event):
            Procedure_Entry_Field_Variable.set("")

        # Define the control backspace event when modifying the text inside the procedure entry field
        def Control_Backspace_Event(event):
            End_Index = self.Procedure_Entry_Field.index(tk.INSERT)
            Start_Index = self.Procedure_Entry_Field.get().rfind(" ", None, End_Index)
            self.Procedure_Entry_Field.selection_range(Start_Index, End_Index)

        # Define the procedure submission event
        def On_Procedure_Submission(event):
            Entry_Input = Procedure_Entry_Field_Variable.get()
            if Entry_Input in alss.Procedure_Aliases:
                self.First_ProcDesc_Label.config(
                    font = ("Verdana", 11),
                    fg = "White"
                )
                Entry_Alias = alss.Procedure_Aliases[Entry_Input]
                Entry_Filename = proc.Procedure_Details[Entry_Alias]["File"]
                Entry_Type = proc.Procedure_Details[Entry_Alias]["Type"]
                Entry_Clinical_Level = proc.Procedure_Details[Entry_Alias]["Skill"]
                Entry_Procedure_ID = proc.Procedure_Details[Entry_Alias]["Procedure ID"]
                Procedure_Descriptor_One.set(f"Type of Procedure:   {Entry_Type}")
                Procedure_Descriptor_Two.set(f"Clinical Level:   {Entry_Clinical_Level}")
                Procedure_Descriptor_Three.set(f"Procedure ID:   {Entry_Procedure_ID}")
                Current_Directory = os.getcwd()
                if vars.Auto_Access_Procedures == True:
                    os.startfile(f"{Current_Directory}/Procedures/{Entry_Filename}")
                else:
                    pass
            elif Entry_Input in proc.Procedure_IDs:
                self.First_ProcDesc_Label.config(
                    font = ("Verdana", 11),
                    fg = "White"
                )
                Procedure_Linked_To_ID = proc.Procedure_IDs[Entry_Input]
                Entry_Filename = proc.Procedure_Details[Procedure_Linked_To_ID]["File"]
                Entry_Type = proc.Procedure_Details[Procedure_Linked_To_ID]["Type"]
                Entry_Clinical_Level = proc.Procedure_Details[Procedure_Linked_To_ID]["Skill"]
                Entry_Procedure_ID = Entry_Input
                Procedure_Descriptor_One.set(f"Type of Procedure:   {Entry_Type}")
                Procedure_Descriptor_Two.set(f"Clinical Level:   {Entry_Clinical_Level}")
                Procedure_Descriptor_Three.set(f"Procedure ID:   {Entry_Procedure_ID}")
                Current_Directory = os.getcwd()
                if vars.Auto_Access_Procedures == True:
                    os.startfile(f"{Current_Directory}/procedures/{Entry_Filename}")
                else:
                    pass
            elif Entry_Input in alss.Memory_Aid_Aliases:
                self.First_ProcDesc_Label.config(
                    font = ("Verdana", 10),
                    fg = "White"
                )
                if len(Entry_Input) < 7:
                    Procedure_Descriptor_One.set(f"Please try search for '{Entry_Input}' using the 'Memory Aids' search utility instead")
                else:
                    Procedure_Descriptor_One.set(f"Please use the 'Memory Aids' search utility to look for:\n\n'{Entry_Input}'")
                Procedure_Descriptor_Two.set("")
                Procedure_Descriptor_Three.set("")
            else:
                self.First_ProcDesc_Label.config(
                    font = ("Verdana Bold", 12),
                    fg = "White"
                )
                Procedure_Descriptor_One.set("Procedure Not Found.")
                Procedure_Descriptor_Two.set("")
                Procedure_Descriptor_Three.set("")

        # Create the procedure entry field for the root window, with a specific textvariable
        self.Procedure_Entry_Field = Entry(
            master = self.master,
            takefocus = False,
            textvariable = Procedure_Entry_Field_Variable,
            font = ("Verdana", 11),
            width = 41,
            fg = "#162119",
            bg = "#78BF8B",
            borderwidth = 0
        )

        # Create the procedure submission button for the root window
        self.Procedure_Submission_Button = Button(
            master = self.master,
            text = "Submit",
            font = ("Verdana Bold", 10),
            fg = "#162119",
            bg = "#78BF8B",
            borderwidth = 0
        )

        # Create the first procedure descriptor label for the root window
        self.First_ProcDesc_Label = Label(
            master = self.master,
            textvariable = Procedure_Descriptor_One,
            font = ("Verdana", 11),
            fg = "White",
            bg = "#223D29"
        )

        # Create the second procedure descriptor label for the root window
        self.Second_ProcDesc_Label = Label(
            master = self.master,
            textvariable = Procedure_Descriptor_Two,
            font = ("Verdana", 11),
            fg = "White",
            bg = "#223D29"
        )

        # Create the third procedure descriptor label for the root window
        self.Third_ProcDesc_Label = Label(
            master = self.master,
            textvariable = Procedure_Descriptor_Three,
            font = ("Verdana", 11),
            fg = "White",
            bg = "#223D29"
        )

        # Bind certain procedure entry field button presses / button combinations to specific methods
        self.Procedure_Entry_Field.bind("<Button-1>", On_Procedure_Entry_Field_Click)
        self.Procedure_Entry_Field.bind("<Control-BackSpace>", Control_Backspace_Event)
        self.Procedure_Entry_Field.bind("<Return>", On_Procedure_Submission)
        self.Procedure_Submission_Button.bind("<Button-1>", On_Procedure_Submission)

        # Position widgets associated with the 'Procedures' selection
        self.Procedure_Entry_Field.place(
            x = 5,
            y = 60
        )
        self.Procedure_Submission_Button.place(
            x = 430,
            y = 60
        )
        self.First_ProcDesc_Label.place(
            x = 6,
            y = 90
        )
        self.Second_ProcDesc_Label.place(
            x = 6,
            y = 120
        )
        self.Third_ProcDesc_Label.place(
            x = 6,
            y = 150
        )

    def Create_MA_Entry_Field(self):
        cmds.Select_Memory_Aids()
        try:
            self.Procedure_Entry_Field.place_forget()
            self.Procedure_Submission_Button.place_forget()
            self.First_ProcDesc_Label.place_forget()
            self.Second_ProcDesc_Label.place_forget()
            self.Third_ProcDesc_Label.place_forget()
            self.LIFEPAK_Clock_Label.place_forget()
            self.Vitals_Frame.place_forget()
        except:
            pass
        else:
            pass
        self.master.configure(background = "#223D29")
        self.master.geometry("550x300+5+10")
        MA_Entry_Field_Variable = StringVar()
        MA_Entry_Field_Variable.set(" What do you need help with?")
        Mem_Descriptor_One = StringVar()
        Mem_Descriptor_One.set("")

        # Set the procedure entry field variable to nothing each time the entry field is clicked
        def On_MA_Entry_Field_Click(event):
            MA_Entry_Field_Variable.set("")

        # Define the control backspace event when modifying the text inside the procedure entry field
        def Control_Backspace_Event(event):
            End_Index = self.MA_Entry_Field.index(tk.INSERT)
            Start_Index = self.MA_Entry_Field.get().rfind(" ", None, End_Index)
            self.MA_Entry_Field.selection_range(Start_Index, End_Index)

        def On_MA_Entry_Submission(event):
            Entry_Input = MA_Entry_Field_Variable.get()
            if Entry_Input in alss.Memory_Aid_Aliases:
                self.MemDesc_Label.config(font = ("Verdana Bold", 12))
                Mem_Descriptor_One.set("")
                Entry_Filename = alss.Memory_Aid_Aliases[Entry_Input]
                Current_Directory = os.getcwd()
                os.startfile(f"{Current_Directory}/Memory Aids/{Entry_Filename}")
            elif Entry_Input in alss.Procedure_Aliases:
                self.MemDesc_Label.config(font = ("Verdana", 10))
                if len(Entry_Input) < 10:
                    Mem_Descriptor_One.set(f"Please search for '{Entry_Input}' using the 'Procedures' search utility instead")
                else:
                    Mem_Descriptor_One.set(f"Please use the 'Procedures' search utility to look for:\n'{Entry_Input}'")
            elif Entry_Input in proc.Procedure_IDs:
                self.MemDesc_Label.config(font = ("Verdana", 10))
                if len(Entry_Input) < 10:
                    Mem_Descriptor_One.set(f"Please search for '{Entry_Input}' using the 'Procedures' search utility instead")
                else:
                    Mem_Descriptor_One.set(f"Please use the 'Procedures' search utility to look for:\n\n'{Entry_Input}'")
            else:
                self.MemDesc_Label.config(font = ("Verdana Bold", 12))
                Mem_Descriptor_One.set("Memory Aid Not Found")

        # Create the memory aid entry field for the root window, with a specific textvariable
        self.MA_Entry_Field = Entry(
            master = self.master,
            takefocus = False,
            textvariable = MA_Entry_Field_Variable,
            font = ("Verdana", 11),
            width = 41,
            fg = "#162119",
            bg = "#78BF8B",
            borderwidth = 0
        )
        self.MA_Submission_Button = Button(
            master = self.master,
            text = "Submit",
            font = ("Verdana Bold", 10),
            fg = "#162119",
            bg = "#78BF8B",
            borderwidth = 0
        )
        self.MemDesc_Label = Label(
            master = self.master,
            textvariable = Mem_Descriptor_One,
            font = ("Verdana Bold", 12),
            fg = "White",
            bg = "#223D29"
        )

        # Bind certain memory aid entry field button presses / button combinations to specific methods
        self.MA_Entry_Field.bind("<Button-1>", On_MA_Entry_Field_Click)
        self.MA_Entry_Field.bind("<Control-BackSpace>", Control_Backspace_Event)
        self.MA_Entry_Field.bind("<Return>", On_MA_Entry_Submission)
        self.MA_Submission_Button.bind("<Button-1>", On_MA_Entry_Submission)

        # Position the widgets associated with the 'Memory Aids' selection
        self.MA_Entry_Field.place(
            x = 5,
            y = 60
        )
        self.MemDesc_Label.place(
            x = 6,
            y = 90
        )
        self.MA_Submission_Button.place(
            x = 430,
            y = 60
        )

    def Create_LIFEPAK_15_Window(self):
        cmds.Select_LIFEPAK_15()
        try:
            self.Procedure_Entry_Field.place_forget()
            self.Procedure_Submission_Button.place_forget()
            self.First_ProcDesc_Label.place_forget()
            self.Second_ProcDesc_Label.place_forget()
            self.Third_ProcDesc_Label.place_forget()
            self.MA_Entry_Field.place_forget()
            self.MA_Submission_Button.place_forget()
            self.MemDesc_Label.place_forget()
        except:
            pass
        else:
            pass

        # Configure the main window
        self.master.configure(background = "Black")
        self.master.geometry("650x400+5+10")

        # Creation of the LIFEPAK clock variable
        LIFEPAK_Clock_Variable = StringVar()
        LIFEPAK_Clock_Variable.set("TIME")

        # Define the clock update function
        def Update_Clock():
            Current_Time = datetime.now().strftime("%H : %M : %S")
            LIFEPAK_Clock_Variable.set(Current_Time)
            self.master.after(500, Update_Clock)

        # Create a label for the LIFEPAK 15's clock string variable
        self.LIFEPAK_Clock_Label = Label(
            master = self.master,
            textvariable = LIFEPAK_Clock_Variable,
            font = ("System", 14),
            fg = "#02F78D",
            bg = "#303030",
            pady = 5,
            width = 82
        )
        self.LIFEPAK_Clock_Label.place(
            x = 0,
            y = 32
        )

        # Call the clock update function to update the LIFEPAK 15's current time
        Update_Clock()

        # Create the 'HR' label on the LIFEPAK 15 display
        self.Vitals_Frame = Frame(
            master = self.master,
            bg = "#0A0A0A",
            height = 338,
            width = 190
        )
        self.Vitals_Frame.place(
            x = 0,
            y = 62
        )





#! WARNING
#* Code beyond the application bootstrapping
#* block below will NOT be executed as this
#* is an infinite loop.

if __name__ == "__main__":
    root = tk.Tk()
    Root_Window(root)
    root.mainloop()