# -*- coding: utf-8 -*-
"""
Created on Tue Jan 18 17:00:52 2022

@author: Moose
"""

import os
import shutil
import smtplib
import ssl
import yagmail
   
# Write the name of the directory here,
# that needs to get sorted
# import tkinter as tk
# from tkinter import filedialog
# root = tk.Tk()
# root.withdraw()
# root.attributes("-topmost", True)
# directory = filedialog.askdirectory()
# root.destroy()  
ScriptName= 'File sorting'
with open('Pilot.txt') as f:
    lines = f.readlines()
    
MainDirectory = lines[0][16:-1]
MainDirectory = MainDirectory.replace("\\","/")
n = lines[1][-2]
ImageJMacrosDirectory = lines[2][25:-1]
ImageJMacrosDirectory = ImageJMacrosDirectory.replace("\\","/")
BatchFileMacrosDirectory = lines[3][23:-1]
BatchFileMacrosDirectory = BatchFileMacrosDirectory.replace("\\","/")
PathtoFiji = lines[4][14:-1]
SendToEmail = lines[5][12:-1]
WorkStationEmail = lines[6][23:-1]
Password = lines[7][10:-1]
ProjectName = lines[8][14:]

# Folder Path
path = MainDirectory 
# This will create a properly organized 
# list with all the filename that is
# there in the directory
n = int(n)
# for root, subdirectories, files in os.walk(directory):
# This will go through each and every file
for j in range(1,n+1):
    newpath = path+'/r{}'.format(j)
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
            
yag = yagmail.SMTP('{}'.format(WorkStationEmail), '{}'.format(Password))
contents = ['{} completed'.format(ScriptName)]
yag.send('{}'.format(SendToEmail), '{}'.format(ProjectName), contents)