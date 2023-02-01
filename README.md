
# DISCLAIMERS
1. Users are required to have at least [Version 3.11.1 of Python](https://www.python.org/ftp/python/3.11.1/python-3.11.1-amd64.exe) already installed to facilitate the successful execution of the python scripts that make up the program.
2. This program was created and is being maintained by a single inexperienced person, therefore the dates of updates and patches may vary significantly.
3. This program is only compatible with the Microsoft Windows 10 Operating System
4. Any tampering with the file structure or the files themselves may likely result in undesired behaviour

# Aim
The aim of the Operational Aid Program (OAP) is to provide pre-hospital emergency medicine practitioners with a quick and easy way of accessing various procedural aids by way of a graphical user interface.

# Method
The OAP consists of a directory of procedural aids contained in text files, a python dictionary that may be accessed by the main python script as a custom module, and finally the main python script, which codes for a graphical user interface using the Tkinter module. The main python 

# Usage & Installation
The master branch of the OAP should be installed as-is into one folder. To start the OAP, users should double click (start) the "start.bat" batch file contained within the OAP's root directory - this batch file will start execute the "main.pyw" python script that acts as the centre of the OAP.

# Function(s)
Upon clicking the entry field, a user may input the name or abbreviation of a procedure then choose to either hit the "Enter" key on their keyboard or click the "Submit" button situated to the right of the entry field. This action will fetch the associated procedural aid text file and display it in the default location set by your text editor's last position.

Clicking the entry field with the "Left Mouse Button" will automatically clear the entry field's contents. In addition to this, users may choose to use the "Control" and "Backspace" key combination to delete the previous word, as opposed to the previous character by just using the "Backspace" key.

# Contact Details
To report a bug/issue, raise a concern, or suggest a feature/edit to the OAP, feel free to contact me via either of the following contact details:
Email: paul.carglass.nl@gmail.com
Discord: _yuri#1623

# Objectives
Listed below are a few optional but desired objectives for the OAP:
- [ ] Modify GUI to be more visually appealing
- [ ] Replace python scripts and batch start file with a Microsoft Windows Executable via PyInstaller
- [ ] Complete all procedural aid text files
- [ ] Review procedural aid text files and ensure all meet an analogous format
- [x] ~~Add additional aliases to the procedure dictionary python file~~ (Completed as of 1 Feb 2023)