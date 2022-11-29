# -*- coding: utf-8 -*-
"""
Created on Sun Jun 12 17:15:18 2022

@author: rlb8
"""


import numpy as np
import pandas as pd
import tkinter as tk
import time
import csv
import yagmail

tic = time.time()
ScriptName = 'Batch File for ImageJ Fusion Macros'

with open('Pilot.txt') as f:
    lines = f.readlines()
    
MainDirectory = lines[0][16:-1] #Main Folder
MainDirectory = MainDirectory.replace("\\","/")
v = lines[1][-2] #Number of Regions (defunct)
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
directory = MainDirectory
path = ImageJMacrosDirectory

n = int(v) #Number of regions


# Folder Path
# path = directory

L1 = '@echo off'

lemon = []

L2 = ['START "My Program" /D "'+'{}'.format(PathtoFiji)+'" ImageJ-win64.exe -macro "'+'{}'.format(path)+'/Align_'+'step{}'.format(n)+'.ijm"']
    
npL1 = np.array(L1)
nplemon = np.array(L2)
Jeepers = pd.Series([npL1])
# orange = []
# for i in range(n,n):
#     Washington = pd.Series([nplemon[i]])
#     orange.append(Washington)
Idaho = pd.DataFrame(Jeepers)    
Oregon = pd.DataFrame(nplemon)
California = pd.concat([Idaho,Oregon])

California.to_csv('{}'.format(BatchFileMacrosDirectory)+'/Image_Alignment.bat', index=False, header=False, sep='\t', quoting=csv.QUOTE_NONE, escapechar = '\t')

