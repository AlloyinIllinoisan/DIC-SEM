# -*- coding: utf-8 -*-
"""
Created on Sun Jun 12 15:20:03 2022

@author: Rephayah
"""

import os
import numpy as np
import os
import time
import csv
import pandas as pd
import numpy as np
import re
import smtplib
import time
import ssl
import yagmail
#from skimage.feature import match_template, register_translation
import scipy


#import glob
#import scipy.ndimage
#import scipy.ndimage.interpolation
#import scipy.misc
#import skimage.exposure
#from scipy.optimize import curve_fit
#from shutil import copyfile
#import PIL.Image
np.set_printoptions(suppress=True)
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
#import matplotlib.pyplot as plt
#import matplotlib.image as mpimg
#import skimage
#import scipy.ndimage



# import tkinter as tk
# from tkinter import filedialog
# root = tk.Tk()
# root.withdraw()
# root.attributes("-topmost", True)
# directory = filedialog.askdirectory()
# root.destroy()
import os

tic = time.time()
ScriptName = 'Image Alignment'

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

v = int(v) #Number of regions

n = int(GridCols)
b = int(GridRows)

coords = []
for i in range(1,b+1):
    for j in range(1,n+1):
        coords.append([i,j])
        
# print(coords)
coords = [str(x) for x in coords]
c = []
for p in range(len(coords)):
        q= coords[p].split("[") #Remove closing parenthese
        c.append(q)
f = []
for a in range(len(c)):
    g = c[a][1]
    f.append(g)
    
d = []
for l in range(len(f)):
    t = f[l].split("]")
    d.append(t)
    
e = []
for l in range(len(f)):
    h = d[l][0]
    e.append(h)

z = []
for l in range(len(f)):
    ahhh = e[l].replace(", ", "_")
    z.append(ahhh)

L = []
for j in range(v,v+1):
    for i in range(len(z)):
        L1 = '''open("{}/step0/step0_{}.tif");
open("{}/step{}/step{}_{}.tif");'''.format(directory,z[i],directory,j,j,z[i])
        # L.append(L1)

        L3 = 'run("Images to Stack");'
        L4 = '//setTool("rectangle");'
        L5 = 'makeRectangle(2000, 1152, 2136, 1692);'
        L6 = 'run("Align slices in stack...", "method=5 windowsizex=2136 windowsizey=1692 x0=2000 y0=1152 swindow=0 subpixel=false itpmethod=0 ref.slice=1 show=true");'
        L7 = 'run("Image Sequence... ", "dir='+"{}".format(directory)+'/AlignedImages_step{}/ format=TIFF use");'.format(j)
        L8 = 'run("Close");'
        

        L.append(L1)
        # L.append(L2)
        L.append(L3)
        L.append(L4)
        L.append(L5)
        L.append(L6)
        L.append(L7)
        L.append(L8)
# L.append(L9)
# L.append(L10)
# L.append(L11)
# L.append(L12)
# L.append(L13)
# L.append(L14)
# L.append(L15)
# L.append(L16)
# L.append(L17)
# L.append(L18)
# L.append(L19)

Sad = np.array(L, dtype=object)
Happy = pd.Series(Sad)
Confused = pd.DataFrame(Happy).replace('  ',' ')
Confused.to_csv(path+'/Align_'+'step{}'.format(v)+'.ijm', float_format=None, index=False, mode ='w', header=False, sep='\t', quoting=csv.QUOTE_NONE, escapechar = '\t')

# yag = yagmail.SMTP('{}'.format(WorkStationEmail), '{}'.format(Password))

# contents = ['{} Completed'.format(ScriptName)]

# yag.send('{}'.format(SendToEmail), '{}'.format(ProjectName), contents)
    
toc = time.time()

print(toc-tic, 'seconds elapsed')
