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

for j in range(1,n+1):
    L1 = 'open("'+'{}'.format(directory)+'/r{}'.format(j)+'/BlN/step1'+'r{}'.format(j)+'_DICIncoMV_0_0.BlN_crop.tif");'
    L2 = 'selectWindow("step1'+'r{}'.format(j)+'_DICIncoMV_0_0.BlN_crop.tif");'
    L3 = 'open("'+'{}'.format(directory)+'/r{}'.format(j)+'/BlN/step1'+'r{}'.format(j)+'_DICIncoMV_0_1.BlN_crop.tif");'
    L4 = 'selectWindow("step1'+'r{}'.format(j)+'_DICIncoMV_0_1.BlN_crop.tif");'
    L5 = 'open("'+'{}'.format(directory)+'/r{}'.format(j)+'/BlN/step1'+'r{}'.format(j)+'_DICIncoMV_0_2.BlN_crop.tif");'
    L6 = 'selectWindow("step1'+'r{}'.format(j)+'_DICIncoMV_0_2.BlN_crop.tif");'
    L7 = 'open("'+'{}'.format(directory)+'/r{}'.format(j)+'/BlN/step1'+'r{}'.format(j)+'_DICIncoMV_1_0.BlN_crop.tif");'
    L8 = 'selectWindow("step1'+'r{}'.format(j)+'_DICIncoMV_1_0.BlN_crop.tif");'
    L9 = 'open("'+'{}'.format(directory)+'/r{}'.format(j)+'/BlN/step1'+'r{}'.format(j)+'_DICIncoMV_1_1.BlN_crop.tif");'
    L10 = 'selectWindow("step1'+'r{}'.format(j)+'_DICIncoMV_1_1.BlN_crop.tif");'
    L11 = 'open("'+'{}'.format(directory)+'/r{}'.format(j)+'/BlN/step1'+'r{}'.format(j)+'_DICIncoMV_1_2.BlN_crop.tif");'
    L12 = 'selectWindow("step1'+'r{}'.format(j)+'_DICIncoMV_1_2.BlN_crop.tif");'
    L13 = 'open("'+'{}'.format(directory)+'/r{}'.format(j)+'/BlN/step1'+'r{}'.format(j)+'_DICIncoMV_2_0.BlN_crop.tif");'
    L14 = 'selectWindow("step1'+'r{}'.format(j)+'_DICIncoMV_2_0.BlN_crop.tif");'
    L15 = 'open("'+'{}'.format(directory)+'/r{}'.format(j)+'/BlN/step1'+'r{}'.format(j)+'_DICIncoMV_2_1.BlN_crop.tif");'
    L16 = 'selectWindow("step1'+'r{}'.format(j)+'_DICIncoMV_2_1.BlN_crop.tif");'
    L17 = 'open("'+'{}'.format(directory)+'/r{}'.format(j)+'/BlN/step1'+'r{}'.format(j)+'_DICIncoMV_2_2.BlN_crop.tif");'
    L18 = 'selectWindow("step1'+'r{}'.format(j)+'_DICIncoMV_2_2.BlN_crop.tif");'
    L19 = 'run("Images to Stack", "name=Stack title=[] use");' #Giving Error in Batch
    L20 = '//run("Brightness/Contrast...");'
    L21 = 'run("Enhance Contrast", "saturated=0.35");'
    L22 = 'run("Enhance Contrast", "saturated=0.35");'
    L23 = 'run("Enhance Contrast", "saturated=0.35");'
    L24 = 'run("Enhance Contrast", "saturated=0.35");'
    L25 = 'makeRectangle(24, 24, 1311, 1317);'
    L26 = 'run("Crop");'
    L27 ='run("Image Sequence... ", "select=['+'{}'.format(directory)+'/r{}'.format(j)+'/BlN/Cropped/] dir=['+'{}'.format(directory)+'/r{}'.format(j)+'/BlN/Cropped/] format=TIFF use");'
    L28 = 'run("Grid/Collection stitching", "type=[Positions from file] order=[Defined by TileConfiguration] directory=['+'{}'.format(directory)+'/r{}'.format(j)+'/BlN/Cropped/] layout_file=Postprocessed_'+'r{}'.format(j)+'.txt fusion_method=[Linear Blending] regression_threshold=0.30 max/avg_displacement_threshold=2.50 absolute_displacement_threshold=3.50 computation_parameters=[Save memory (but be slower)] image_output=[Fuse and display]");'
    # L29 = 'run("Rainbow RGB");'
    # L30 = '//run("Brightness/Contrast...");'
    # L31 = 'run("Enhance Contrast", "saturated=0.35");'
    # L32 = 'run("Enhance Contrast", "saturated=0.35");'
    # L33 = 'run("Close");'
    L34 = 'saveAs("Tiff", "'+'{}'.format(directory)+'/r{}'.format(j)+'/BlN/Cropped/Fused_BlN_'+'r{}'.format(j)+'.tif");'
    L35 = 'close();'
    L36 = 'selectWindow("Stack");'
    L37 = 'close();'

    Sad = np.array([L1,L2,L3,L4,L5,L6,L7,L8,L9,L10,L11,L12,L13,L14,L15,L16,L17,L18,L19,L20,L21,L22,L23,L24,L25,L26,L27,L28,L34,L35,L36,L37])
    Happy = pd.Series(Sad)
    Confused = pd.DataFrame(Happy).replace('  ',' ')
    Confused.to_csv(path+'/MakeFuseBlN_'+'r{}'.format(j)+'.ijm', float_format=None, index=False, mode ='w', header=False, sep='\t', quoting=csv.QUOTE_NONE, escapechar = '\t')

yag = yagmail.SMTP('{}'.format(WorkStationEmail), '{}'.format(Password))

contents = ['{} Completed'.format(ScriptName)]

yag.send('{}'.format(SendToEmail), '{}'.format(ProjectName), contents)
    
toc = time.time()

print(toc-tic, 'seconds elapsed')