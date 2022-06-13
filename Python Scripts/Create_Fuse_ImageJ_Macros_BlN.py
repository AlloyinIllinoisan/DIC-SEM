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

tic = time.time()
ScriptName = 'Macros for BlN Fusion in ImageJ'

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

L2 = []
for j in range(v,v+1):
    for i in range(len(z)):
        L1 = '''open("{}/AlignedImages_step{}/BlN/step{}_{}.BlN_crop.tif");
selectWindow("step{}_{}.BlN_crop.tif");'''.format(directory,j,j,z[i],j,z[i])
        L2.append(L1)
    L19 = 'run("Images to Stack", "name=Stack title=[] use");' #Giving Error in Batch
    L20 = '//run("Brightness/Contrast...");'
    L21 = 'run("Enhance Contrast", "saturated=0.35");'
    L22 = 'run("Enhance Contrast", "saturated=0.35");'
    L23 = 'run("Enhance Contrast", "saturated=0.35");'
    L24 = 'run("Enhance Contrast", "saturated=0.35");'
    L25 = 'makeRectangle(20, 18, 2008, 1328);'
    L26 = 'run("Crop");'
    L27 ='run("Image Sequence... ", "select=['+'{}'.format(directory)+'/AlignedImages_step{}'.format(j)+'/BlN/Cropped/] dir=['+'{}'.format(directory)+'/AlignedImages_step{}'.format(j)+'/BlN/Cropped/] format=TIFF use");'
    L28 = 'run("Grid/Collection stitching", "type=[Positions from file] order=[Defined by TileConfiguration] directory=['+'{}'.format(directory)+'/AlignedImages_step{}'.format(j)+'/BlN/Cropped/] layout_file=Postprocessed_BlN_'+'step{}'.format(j)+'.txt fusion_method=[Linear Blending] regression_threshold=0.30 max/avg_displacement_threshold=2.50 absolute_displacement_threshold=3.50 computation_parameters=[Save memory (but be slower)] image_output=[Fuse and display]");'
    L29 = 'saveAs("Tiff", "'+'{}'.format(directory)+'/AlignedImages_step{}'.format(j)+'/BlN/Cropped/Fused_BlN_'+'step{}'.format(j)+'.tif");'
    L30 = 'close();'
    L31 = 'selectWindow("Stack");'
    L32 = 'close();'
    L2.append(L19)
    L2.append(L20)
    L2.append(L21)
    L2.append(L22)
    L2.append(L23)
    L2.append(L24)
    L2.append(L25)
    L2.append(L26)
    L2.append(L27)
    L2.append(L28)
    L2.append(L29)
    L2.append(L30)
    L2.append(L31)
    L2.append(L32)
    Sad = np.array(L2, dtype=object)
    Happy = pd.Series(Sad)
    Confused = pd.DataFrame(Happy).replace('  ',' ')
    Confused.to_csv(path+'/MakeFuseBlN_'+'step{}'.format(j)+'.ijm', float_format=None, index=False, mode ='w', header=False, sep='\t', quoting=csv.QUOTE_NONE, escapechar = '\t')

yag = yagmail.SMTP('{}'.format(WorkStationEmail), '{}'.format(Password))

contents = ['{} Completed'.format(ScriptName)]

yag.send('{}'.format(SendToEmail), '{}'.format(ProjectName), contents)
    
toc = time.time()

print(toc-tic, 'seconds elapsed')
