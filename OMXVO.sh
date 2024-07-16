#!/bin/bash

filePath="$1"

#pythonPath="/usr/local/bin/python3"

Path_OpenMX_Viewer_Opener="/Users/apps/openmx_viewer_opener"

Path_py_script="$Path_OpenMX_Viewer_Opener/src/upload_file.py"

python3 "$Path_py_script" "$filePath" "$Path_OpenMX_Viewer_Opener"
#"$pythonPath" "$Path_py_script" "$filePath" "$Path_OpenMX_Viewer_Opener"
