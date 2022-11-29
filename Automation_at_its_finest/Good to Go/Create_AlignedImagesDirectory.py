# -*- coding: utf-8 -*-
"""
Created on Sat Jun 11 15:17:44 2022

@author: Rephayah
"""

import os
import shutil
import smtplib
import ssl
import yagmail
import time
# Write the name of the directory here,
# that needs to get sorted
# import tkinter as tk
# from tkinter import filedialog
# root = tk.Tk()
# root.withdraw()
# root.attributes("-topmost", True)
# directory = filedialog.askdirectory()
# root.destroy()  
tic = time.time()
ScriptName= 'Aligned Images Directory'
with open('Pilot.txt') as f:
    lines = f.readlines()
    
MainDirectory = lines[0][16:-1] #Main Folder
MainDirectory = MainDirectory.replace("\\","/")
n = lines[1][-2] #Number of Steps
ImageJMacrosDirectory = lines[2][25:-1] #Folder Containing the ImageJ Macros
ImageJMacrosDirectory = ImageJMacrosDirectory.replace("\\","/")
BatchFileMacrosDirectory = lines[3][23:-1] #Folder Containing the Batch Files
BatchFileMacrosDirectory = BatchFileMacrosDirectory.replace("\\","/")
PathtoFiji = lines[4][14:-1] #Path to ImageJ Fiji
SendToEmail = lines[5][12:-1] #Your email
WorkStationEmail = lines[6][23:-1] #Marshawn's Email
Password = lines[7][10:-1] #Password for Marshawn to get to his email
ProjectName = lines[8][14:-1] #Name of the current project
GridCols = lines[9][11:-1] #Number of columns in the grid
GridRows = lines[10][11:-1] #Number of rows in the grid
TileOverlap = lines[11][14:-1] #Percentage of overlap between tiles
PythonScriptsDirectory = lines[12][26:-1] #Python Scripts Directory (Good to Go)
PythonScriptsDirectory = PythonScriptsDirectory.replace("\\","/")
xCorrelDirectory = lines[13][17:] #Path to xCorrel


# Folder Path
path = MainDirectory 
# This will create a properly organized 
# list with all the filename that is
# there in the directory
n = int(n)
# for root, subdirectories, files in os.walk(directory):
for i in range(n,n+1):
    alignedimagesdirectory = '{}/AlignedImages_step{}'.format(path,i)
    if not os.path.exists(alignedimagesdirectory):
        os.makedirs(alignedimagesdirectory)

# yag = yagmail.SMTP('{}'.format(WorkStationEmail), '{}'.format(Password))

# contents = ['{} Completed'.format(ScriptName)]

# yag.send('{}'.format(SendToEmail), '{}'.format(ProjectName), contents)
    
toc = time.time()

print(toc-tic, 'seconds elapsed')
