# -*- coding: utf-8 -*-
"""
Created on Mon Mar  7 00:37:58 2022

@author: Rephayah
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
xCorrelDirectory = lines[13][17:-1] #Path to xCorrel
directory = MainDirectory
path = ImageJMacrosDirectory

n = int(n) #Number of regions


# Folder Path
# path = directory

L1 = '@echo off'

lemon = []

for j in range(n,n+1):
    L2 = 'START "My Program" /D "'+'{}'.format(PathtoFiji)+'" ImageJ-win64.exe -macro "'+'{}'.format(path)+'/MakeFuseBlN_'+'step{}'.format(j)+'.ijm"\nTIMEOUT /T 75'
    lemon.append(L2)
    
npL1 = np.array(L1)
nplemon = np.array(lemon)
Jeepers = pd.Series([npL1])
orange = []
Washington = pd.Series(nplemon)
orange.append(Washington)
Idaho = pd.DataFrame(Jeepers)    
Oregon = pd.DataFrame(orange)
California = pd.concat([Idaho,Oregon])

California.to_csv('{}'.format(BatchFileMacrosDirectory)+'/ImageJ_Fusion_BlN.bat', index=False, header=False, sep='\t', quoting=csv.QUOTE_NONE, escapechar = '\t')

apple = []
for k in range(n,n+1):
    L3 = 'START "My Program" /D "'+'{}'.format(PathtoFiji)+'" ImageJ-win64.exe -macro "'+'{}'.format(path)+'/MakeFuseBlA_'+'step{}'.format(k)+'.ijm"\nTIMEOUT /T 75'
    apple.append(L3)

npL3 = np.array(L3)
npapple = np.array(apple)
Japple = pd.Series([npL3])
emptyapple = []
Applepopulation = pd.Series(npapple)
emptyapple.append(Applepopulation)
JappleDF = pd.DataFrame(Japple)
EmptyAppleDF = pd.DataFrame(emptyapple)
AppleConcat = pd.concat([Idaho,EmptyAppleDF])
AppleConcat.to_csv('{}'.format(BatchFileMacrosDirectory)+'/ImageJ_Fusion_BlA.bat', index=False, header=False, sep='\t', quoting=csv.QUOTE_NONE, escapechar = '\t')
    
strawberry = []
for m in range(n,n+1):
    L4 = 'START "My Program" /D "'+'{}'.format(PathtoFiji)+'" ImageJ-win64.exe -macro "'+'{}'.format(path)+'/MakeFuseGrX_'+'step{}'.format(m)+'.ijm"\nTIMEOUT /T 75'
    strawberry.append(L4)

npL4 = np.array(L4)
npstrawberry = np.array(strawberry)
Jstrawberry = pd.Series([npL4])
emptystrawberry = []
strawberrypopulation = pd.Series(npstrawberry)
emptystrawberry.append(strawberrypopulation)
JstrawberryDF = pd.DataFrame(Jstrawberry)
EmptystrawberryDF = pd.DataFrame(emptystrawberry)
strawberryConcat = pd.concat([Idaho,EmptystrawberryDF])
strawberryConcat.to_csv('{}'.format(BatchFileMacrosDirectory)+'/ImageJ_Fusion_GrX.bat', index=False, header=False, sep='\t', quoting=csv.QUOTE_NONE, escapechar = '\t')

blueberry = []
for p in range(n,n+1):
    L5 = 'START "My Program" /D "'+'{}'.format(PathtoFiji)+'" ImageJ-win64.exe -macro "'+'{}'.format(path)+'/MakeFuseLRt_'+'step{}'.format(p)+'.ijm"\nTIMEOUT /T 75'
    blueberry.append(L5)
    
npL5 = np.array(L5) 
npblueberry = np.array(blueberry)
Jblueberry = pd.Series([npL5])
emptyblueberry = []
blueberrypopulation = pd.Series(npblueberry)
emptyblueberry.append(blueberrypopulation)
JblueberryDF = pd.DataFrame(Jblueberry)
EmptyblueberryDF = pd.DataFrame(emptyblueberry)
blueberryConcat = pd.concat([Idaho,EmptyblueberryDF])
blueberryConcat.to_csv('{}'.format(BatchFileMacrosDirectory)+'/ImageJ_Fusion_LRt.bat', index=False, header=False, sep='\t', quoting=csv.QUOTE_NONE, escapechar = '\t')

# yag = yagmail.SMTP('{}'.format(WorkStationEmail), '{}'.format(Password))

# contents = ['{} Completed'.format(ScriptName)]

# yag.send('{}'.format(SendToEmail), '{}'.format(ProjectName), contents)
    
toc = time.time()

print(toc-tic, 'seconds elapsed')
