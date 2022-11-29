# -*- coding: utf-8 -*-
"""
Created on Tue Jan 18 17:00:52 2022

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
ScriptName= 'File sorting'
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

# Folder Path
path = MainDirectory 
# This will create a properly organized 
# list with all the filename that is
# there in the directory
n = int(n)
# This will go through each and every file
for j in range(n,n+1):
    newpath = path+'/AlignedImages_step{}'.format(j)
    list_ = os.listdir(newpath)
    for file_ in list_:
        name, ext = os.path.splitext(file_)
  
    # This is going to store the extension type
        ext = ext[1:]
  
    # This forces the next iteration,
    # if it is the directory
        if ext == '':
            continue
  
    # This will move the file to the directory
    # where the name 'ext' already exists
        if os.path.exists(newpath+'/'+ext):
            shutil.move(newpath+'/'+file_, newpath+'/'+ext+'/'+file_)
  
    # This will create a new directory,
    # if the directory does not already exist
        else:
            os.makedirs(newpath+'/'+ext)
            shutil.move(newpath+'/'+file_, newpath+'/'+ext+'/'+file_)
            
# yag = yagmail.SMTP('{}'.format(WorkStationEmail), '{}'.format(Password))
# contents = ['{} completed'.format(ScriptName)]
# yag.send('{}'.format(SendToEmail), '{}'.format(ProjectName), contents)

toc = time.time()

print(toc-tic, 'seconds elapsed')