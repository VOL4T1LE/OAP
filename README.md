
# DISCLAIMERS
1. Users are required to have at least [Version 3.11.1 of Python](https://www.python.org/ftp/python/3.11.1/python-3.11.1-amd64.exe) already installed to facilitate the successful execution of the python files that make up the program.
2. This program was created and is being maintained by a single inexperienced person, therefore the dates of updates and patches may vary significantly.
3. This program has only been tested on a computer using the Microsoft Windows 10 Operating System
4. Any tampering with the file structure or the files themselves may likely result in undesired behaviour

# Aim
The aim of the Operational Aid Program (OAP) is to provide pre-hospital emergency medicine practitioners with a quick and easy way of accessing various procedural aids by way of a graphical user interface.

# Method
The OAP consists of a a directory of procedural aids cotnaiend in text files, a python dictionary that may be accessed by the main python file as a custom module, and finally the main python file, which codes for a graphical user interface using the Tkinter module.

# Usage & Installation
The master branch of the OAP should be installed as-is into one folder. To start the OAP, users should double click (start) the "start.bat" batch file contained within the OAP's root directory - this batch file will start execute the "main.pyw" python fiel that acts as the centre of the OAP.

# Function(s)
Upon clicking the entry field, a user may input the name or abbreviation of a procedure then choose to either hit the "Enter" key on their keyboard or click the "Submit" button situated to the right of the entry field. This action will fetch the associated procedural aid text file and display it in the defualt location set by your text editor's last position.

Clicking the entry field with the "Left Mouse Button" will automatically clear the entry field's contents. In addition to this, users may choose to use the "Control" and "Backspace" key combination to delete the previous word, as opposed to the previous character by just using the "Backspace" key.

# Objectives
Listed below are a few optional but desired objectives for the OAP:
- [ ] Modify GUI to be more visually appealing
- [ ] Replace python files and batch file with a Microsoft Windows Executable via PyInstaller
- [ ] Complete all procedural aid text files
- [ ] Add additional aliases to the procedure dictionary python file
