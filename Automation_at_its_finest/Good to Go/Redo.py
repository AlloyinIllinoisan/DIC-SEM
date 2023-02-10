# -*- coding: utf-8 -*-
"""
Created on Thu Feb  9 11:28:50 2023

@author: rlb8
"""

import os
import pandas as pd
import numpy as np
import time
import glob
import tkinter as tk
import re
import csv
import shutil

tic = time.time()
ScriptName = 'Redo'

#Input step number

with open('Pilot.txt') as f:
    lines = f.readlines()#     #open folder 

# MainDirectory = lines[0][16:-1] #Main Folder
# MainDirectory = MainDirectory.replace("\\","/")
# q = lines[1][-2] #Number of Steps
# ImageJMacrosDirectory = lines[2][25:-1] #Folder Containing the ImageJ Macros
# ImageJMacrosDirectory = ImageJMacrosDirectory.replace("\\","/")
# BatchFileMacrosDirectory = lines[3][23:-1] #Folder Containing the Batch Files
# BatchFileMacrosDirectory = BatchFileMacrosDirectory.replace("\\","/")
PathtoFiji = lines[4][14:-1] #Path to ImageJ Fiji
SendToEmail = lines[5][12:-1] #Your email
WorkStationEmail = lines[6][23:-1] #Marshawn's Email
Password = lines[7][10:-1] #Password for Marshawn to get to his email
ProjectName = lines[8][14:-1] #Name of the current project
# GridCols = lines[9][11:-1] #Number of columns in the grid
# GridRows = lines[10][11:-1] #Number of rows in the grid
# TileOverlap = lines[11][14:-1] #Percentage of overlap between tiles
PythonScriptsDirectory = lines[12][26:-1] #Python Scripts Directory (Good to Go)
PythonScriptsDirectory = PythonScriptsDirectory.replace("\\","/")
xCorrelDirectory = lines[13][17:-1] #Path to xCorrel


#Select the Aligned Images Directory
from tkinter import filedialog
root = tk.Tk()
root.withdraw()
root.attributes("-topmost", True)
directory = filedialog.askdirectory()
root.destroy()

#Select the ima files of the sections you want recalculated
root = tk.Tk()
root.withdraw()
root.attributes("-topmost", True)
filestoredo = filedialog.askopenfilenames()
root.destroy()

#Extracts the section numbers
a = []
for i in range(len(filestoredo)):    
    gravy = filestoredo[i][-7:-4]
    a.append(gravy)

#Creates Recalculation Directory
recalculationdirectory = '{}/Recalculation'.format(directory)
if not os.path.exists(recalculationdirectory):
    os.makedirs(recalculationdirectory)
stepnumber = filestoredo[0][-22:-21]
# yes = '{}'.format(a[0])
ext = ('BlN', 'GrX', 'LRt', 'BlA', 'DpX', 'DpY', 'BlL', 'BlT','ima','tif','PAR')
grxdirectory = directory+'/'+ext[1]
blndirectory = directory+'/'+ext[0]
lrtdirectory = directory+'/'+ext[2]
bladirectory = directory+'/'+ext[3]
dpxdirectory = directory+'/'+ext[4]
dpydirectory = directory+'/'+ext[5]
blldirectory = directory+'/'+ext[6]
bltdirectory = directory+'/'+ext[7]
tifdirectory = directory+'/'+ext[9]
pardirectory = directory+'/'+ext[10]

for j in range(len(a)):
    newpath = directory
    list_ = os.listdir(newpath)
    shutil.move(filestoredo[j], recalculationdirectory)
    # shutil.move(directory)
    shutil.move(tifdirectory+'/step0_{}.tif'.format(a[j]),recalculationdirectory)
    shutil.move(tifdirectory+'/step{}'.format(stepnumber)+'_{}.tif'.format(a[j]),recalculationdirectory)
    shutil.move(pardirectory+'/IMAFile_P{}.PAR'.format(a[j]),recalculationdirectory)

#Matrix for Row
b = []
#Matrix for Column
c = []   

for i in range(len(a)): #Populates above matrices
    d = a[i][0]
    b.append(d)
    e = a[i][2]
    c.append(e)        
    
for i in range(len(a)):
       d = open(recalculationdirectory + '/IMAFile_P%s_%s.PAR' % (b[i],c[i]) , "w+") #Change these to the ima.ima parameters
       d.write("0 0 6143 4095\n") 
       d.write("0 0 0 50 50 50 50\n")
       d.write("31 31 3 3\n")
       d.write("3 1.000000 1 3 0 0 0 0\n")
       d.write("1.0 0\n")
       d.write("1 1 0.000000 8 1\n")
       d.write("10 10\n")
       d.close()
print('file done')    
   
f = open("C:\\xCorrel\\%s_step%s_%s.bat" % (ProjectName, stepnumber,'Redo'), "w+") #Change the Name and the directory below
f.write("echo off\n")
f.write("title calculation HDIC\n")
f.write("echo start calcul\n")
f.write("pause\n")
for i in range(len(a)):
    f.write("start /wait XCorrel_V9.11a.exe %s/IMAFile_p%s_%s.ima\n" % (recalculationdirectory,b[i],c[i]))
print('file done')
f.write("call XCorrel_Finished_%s.bat" % (ProjectName))
f.close()   