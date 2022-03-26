# -*- coding: utf-8 -*-
"""
Created on Mon Mar  7 00:37:58 2022

@author: repha
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
directory = MainDirectory
path = ImageJMacrosDirectory

n = int(n) #Number of regions


# Folder Path
# path = directory

L1 = '@echo off'

lemon = []

for j in range(1,n+1):
    L2 = 'START "My Program" /D "'+'{}'.format(PathtoFiji)+'" ImageJ-win64.exe -macro "'+'{}'.format(path)+'/MakeFuseBlN_'+'r{}'.format(j)+'.ijm"\nTIMEOUT /T 20'
    lemon.append(L2)
    
npL1 = np.array(L1)
nplemon = np.array(lemon)
Jeepers = pd.Series([npL1])
orange = []
for i in range(0,n):
    Washington = pd.Series([nplemon[i]])
    orange.append(Washington)
Idaho = pd.DataFrame(Jeepers)    
Oregon = pd.DataFrame(orange)
California = pd.concat([Idaho,Oregon])

California.to_csv('{}'.format(BatchFileMacrosDirectory)+'/ImageJ_Fusion_BlN.bat', index=False, header=False, sep='\t', quoting=csv.QUOTE_NONE, escapechar = '\t')

apple = []
for k in range(1,n+1):
    L3 = 'START "My Program" /D "'+'{}'.format(PathtoFiji)+'" ImageJ-win64.exe -macro "'+'{}'.format(path)+'/MakeFuseBlA_'+'r{}'.format(k)+'.ijm"\nTIMEOUT /T 20'
    apple.append(L3)

npL3 = np.array(L3)
npapple = np.array(apple)
Japple = pd.Series([npL3])
emptyapple = []
for l in range(0,n):
    Applepopulation = pd.Series([npapple[i]])
    emptyapple.append(Applepopulation)
JappleDF = pd.DataFrame(Japple)
EmptyAppleDF = pd.DataFrame(emptyapple)
AppleConcat = pd.concat([Idaho,EmptyAppleDF])
AppleConcat.to_csv('{}'.format(BatchFileMacrosDirectory)+'/ImageJ_Fusion_BlA.bat', index=False, header=False, sep='\t', quoting=csv.QUOTE_NONE, escapechar = '\t')
    
strawberry = []
for m in range(1,n+1):
    L4 = 'START "My Program" /D "'+'{}'.format(PathtoFiji)+'" ImageJ-win64.exe -macro "'+'{}'.format(path)+'/MakeFuseGrX_'+'r{}'.format(m)+'.ijm"\nTIMEOUT /T 20'
    strawberry.append(L4)

npL4 = np.array(L4)
npstrawberry = np.array(strawberry)
Jstrawberry = pd.Series([npL4])
emptystrawberry = []
for o in range(0,n):
    strawberrypopulation = pd.Series([npstrawberry[o]])
    emptystrawberry.append(strawberrypopulation)
JstrawberryDF = pd.DataFrame(Jstrawberry)
EmptystrawberryDF = pd.DataFrame(emptystrawberry)
strawberryConcat = pd.concat([Idaho,EmptystrawberryDF])
strawberryConcat.to_csv('{}'.format(BatchFileMacrosDirectory)+'/ImageJ_Fusion_GrX.bat', index=False, header=False, sep='\t', quoting=csv.QUOTE_NONE, escapechar = '\t')

blueberry = []
for p in range(1,n+1):
    L5 = 'START "My Program" /D "'+'{}'.format(PathtoFiji)+'" ImageJ-win64.exe -macro "'+'{}'.format(path)+'/MakeFuseLRt_'+'r{}'.format(p)+'.ijm"\nTIMEOUT /T 20'
    blueberry.append(L5)
    
npL5 = np.array(L5)
npblueberry = np.array(blueberry)
Jblueberry = pd.Series([npL5])
emptyblueberry = []
for y in range(0,n):
    blueberrypopulation = pd.Series([npblueberry[y]])
    emptyblueberry.append(blueberrypopulation)
JblueberryDF = pd.DataFrame(Jblueberry)
EmptyblueberryDF = pd.DataFrame(emptyblueberry)
blueberryConcat = pd.concat([Idaho,EmptyblueberryDF])
blueberryConcat.to_csv('{}'.format(BatchFileMacrosDirectory)+'/ImageJ_Fusion_LRt.bat', index=False, header=False, sep='\t', quoting=csv.QUOTE_NONE, escapechar = '\t')

yag = yagmail.SMTP('{}'.format(WorkStationEmail), '{}'.format(Password))

contents = ['{} Completed'.format(ScriptName)]

yag.send('{}'.format(SendToEmail), '{}'.format(ProjectName), contents)
    
toc = time.time()

print(toc-tic, 'seconds elapsed')