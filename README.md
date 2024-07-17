# OpenMX Viewer Opener
OpenMX Viewer Opener is a windows batch file combinding with python code  
to visualize some files on the OpenMX Viewer website using google chrome.  
If you are a Windows user, you can set OpenMX Viewer Opener  
to the prescribed application for files such as *.cif  
to visualize the structure file with a double click.  

This is written in Python and Javascript.
The code is evoked by *.bat file for Windows.

## Requirement
- Python
  - selenium
- Google Chrome

## Installation
- Install python
- Install selenium python module
  - When the selenium installed, google chrome and chrome driver are installed automatically.

## How to Use
### For Windows users
- Edit the enviromental variable of path in OpenMX_Viewer_Opener.bat file.
- Drag and drop your files on the OpenMX_Viewer_Opener.bat to visualize on OpenMX Viewer.

### For MacOS and Linux users
- Execute the follwing command with proper enviromental variables.
```
python ${PATH_OpenMX_Viewer_Opener}/src/upload_file.py ${INPUTFILE} ${PATH_OpenMX_Viewer_Opener}
```
