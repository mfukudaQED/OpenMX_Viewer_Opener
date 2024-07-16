@echo off
set filePath=%1

REM --- path of OpenMX_Viewer_Opener ---
set Path_OpenMX_Viewer_Opener="C:\Users\mfuku\OneDrive - The University of Tokyo\apps\openmx_viewer_opener"

REM --- path of Python ---
REM set pythonPath="C:\Python310\python.exe"

set Path_OpenMX_Viewer_Opener=%Path_OpenMX_Viewer_Opener:"=%
set Path_OpenMX_Viewer_Opener="%Path_OpenMX_Viewer_Opener%"
set Path_py_script=%Path_OpenMX_Viewer_Opener%\src\upload_file.py

REM --- execute python script ---
python %Path_py_script% %filePath% %Path_OpenMX_Viewer_Opener%
REM %pythonPath% %Path_py_script% %filePath% %Path_OpenMX_Viewer_Opener%

REM pause
