import numpy as np
import pandas as pd
import tkinter as tk
import csv

# -*- coding: utf-8 -*-
"""
Created on Sun Mar  6 16:53:39 2022

@author: Rephayah
"""

import time
import csv
import pandas as pd
import numpy as np
import re
import smtplib
import time
import ssl
import yagmail

#     #open folder 
# from tkinter import filedialog
# root = tk.Tk()
# root.withdraw()
# root.attributes("-topmost", True)
# directory = filedialog.askdirectory()
# root.destroy()

tic = time.time()
ScriptName = 'Make Create Aligned Image Directory Batch File'

with open('Pilot.txt') as f:
    lines = f.readlines()
    
MainDirectory = lines[0][16:-1] #Main Folder
MainDirectory = MainDirectory.replace("\\","/")
n = lines[1][-2]
ImageJMacrosDirectory = lines[2][25:-1] #Directory to ImageJ Macros
ImageJMacrosDirectory = ImageJMacrosDirectory.replace("\\","/")
BatchFileMacrosDirectory = lines[3][23:-1] #Directory to Batch File Macros
BatchFileMacrosDirectory = BatchFileMacrosDirectory.replace("\\","/")
PathtoFiji = lines[4][14:-1] #Path to ImageJ
SendToEmail = lines[5][12:-1] #Your email
WorkStationEmail = lines[6][23:-1] #Marshawn's email
Password = lines[7][10:-1] #Password to Marshawn's email
ProjectName = lines[8][14:-1] #Name of the project
GridCols = lines[9][11:-1] #Number of columns in grid
GridRows = lines[10][11:-1] #Number of rows in grid
TileOverlap = lines[11][14:-1] #Percentage of overlap between tiles
PythonScriptsDirectory = lines[12][26:] #Directory of the Aligned Images
# PythonScriptsDirectory = PythonScriptsDirectory.replace("\\","/")
# Folder Path
path = MainDirectory

L1 = '''@echo off
setlocal'''
n = int(n)

lemon = []


L2 = '''call C:\\ProgramData\\Anaconda3\\condabin\\activate.bat
cd "{}"
python Create_AlignedImagesDirectory.py'''.format(PythonScriptsDirectory)
lemon.append(L2)
    
npL1 = np.array(L1)
nplemon = np.array(lemon)
Jeepers = pd.Series([npL1])

Idaho = pd.DataFrame(Jeepers)    
Oregon = pd.DataFrame(nplemon)
California = pd.concat([Idaho,Oregon])

California.to_csv(BatchFileMacrosDirectory+'/Create_AlignedImagesDirectory_Batch.bat', index=False, header=False, sep='\t', quoting=csv.QUOTE_NONE, escapechar = '\t')

# yag = yagmail.SMTP('{}'.format(WorkStationEmail), '{}'.format(Password))

# contents = ['{} Completed'.format(ScriptName)]

# yag.send('{}'.format(SendToEmail), '{}'.format(ProjectName), contents)
    
toc = time.time()

print(toc-tic, 'seconds elapsed')