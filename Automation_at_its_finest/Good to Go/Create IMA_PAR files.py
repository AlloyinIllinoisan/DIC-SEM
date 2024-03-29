# -*- coding: utf-8 -*-
"""
Created on Wed Sep 27 13:35:51 2017

@author: Pollo
"""


# import tkinter as tk
# from tkinter import filedialog
# #     #open folder 
# # from tkinter import filedialog
# root = tk.Tk()
# root.withdraw()
# root.attributes("-topmost", True)
# directory = filedialog.askdirectory()
# root.destroy()


import time
import csv
import pandas as pd
import numpy as np
import re
import smtplib
import time
import ssl
import yagmail

tic = time.time()
ScriptName = 'Macros for BlN Fusion in ImageJ'

with open('Pilot.txt') as f:
    lines = f.readlines()
    
MainDirectory = lines[0][16:-1] #Main Folder
MainDirectory = MainDirectory.replace("\\","/")
q = lines[1][-2] #Number of Steps
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
xCorrelDirectory = lines[13][17:-1] #Path to xCorrel
directory = MainDirectory
path = ImageJMacrosDirectory

v = int(q) #Number of regions

n = int(GridCols)
b = int(GridRows)

newpath = directory + '/AlignedImages_step{}'.format(v)
for j in range(1,n+1):
    for i in range(1,b+1):
       # f=  open("C:\\Users\\Pollo\\Desktop\\H-DIC on C\\Patrick CALLAHAN\\Titanium_Project\\Ti7_Insitu_HDIC\\P%s_%s\\Align\\IMAFile_step1to7.ima" % (i,j), "w+")
        f = open(newpath + '/IMAFile_P%s_%s.ima' % (i,j) , "w+")       
        f.write("step0_%s_%s.tif\n" % (i,j))
        f.write("step%s_%s_%s.tif\n" % (v,i,j)) #Change this number to the current step number
        f.write("\n")
       
     
        f.close()
       # d= open("C:\\Users\\Pollo\\Desktop\\H-DIC on C\\Patrick CALLAHAN\\Titanium_Project\\Ti7_Insitu_HDIC\\P%s_%s\\Align\\IMAFile_step1to7.PAR" % (i,j), "w+")
        d = open(newpath + '/IMAFile_P%s_%s.PAR' % (i,j) , "w+") #Change these to the ima.ima parameters
        d.write("0 0 6143 4095\n") 
        d.write("0 0 0 60 60 60 60\n")
        d.write("45 45 3 3\n")
        d.write("3 1.000000 1 3 0 0 0 0\n")
        d.write("1.0 0\n")
        d.write("1 1 0.000000 8 1\n")
        d.write("4 4\n")
    print('file done')
    
