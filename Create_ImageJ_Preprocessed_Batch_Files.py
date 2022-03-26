# -*- coding: utf-8 -*-
"""
Created on Mon Mar  7 00:37:58 2022

@author: repha
"""

import numpy as np
import pandas as pd
import tkinter as tk
import csv

# -*- coding: utf-8 -*-
"""
Created on Sun Mar  6 16:53:39 2022

@author: repha
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
ScriptName = 'Make ImageJ Preprocessed Batch File'

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


L1 = '@echo off'
n = int(n)

lemon = []

for j in range(1,n+1):
    L2 = 'START "My Program" /D "'+'{}'.format(PathtoFiji)+'" ImageJ-win64.exe -macro "'+'{}'.format(ImageJMacrosDirectory)+'/PreprocessedMacro_BlN_'+'r{}'.format(j)+'.ijm"\nTIMEOUT /T 20'
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

California.to_csv(BatchFileMacrosDirectory+'/ImageJ_Preprocessed.bat', index=False, header=False, sep='\t', quoting=csv.QUOTE_NONE, escapechar = '\t')

yag = yagmail.SMTP('{}'.format(WorkStationEmail), '{}'.format(Password))

contents = ['{} Completed'.format(ScriptName)]

yag.send('{}'.format(SendToEmail), '{}'.format(ProjectName), contents)
    
toc = time.time()

print(toc-tic, 'seconds elapsed')