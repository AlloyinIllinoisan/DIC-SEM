# -*- coding: utf-8 -*-
"""
Created on Sun Mar  6 11:56:43 2022

@author: repha
"""

import pandas as pd
import numpy as np
import re
import os
import tkinter as tk
import time
import yagmail
import csv

tic = time.time()
ScriptName = 'Macros for Creating Preprocessed Text Files'

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
    PreprocessedMacroLine = 'run("Grid/Collection stitching", "type=[Filename defined position] order=[Defined by filename         ] grid_size_x=3 grid_size_y=3 tile_overlap=15 first_file_index_x=0 first_file_index_y=0 directory=['+'{}'.format(MainDirectory)+'/r{}'.format(j)+'/tif'+ '] file_names=step0'+'r{}'.format(j)+'_DICIncoMV_{x}_{y}.tif output_textfile_name=TileConfiguration_Preprocessed.txt fusion_method=[Linear Blending] regression_threshold=0.30 max/avg_displacement_threshold=2.50 absolute_displacement_threshold=3.50 compute_overlap computation_parameters=[Save memory (but be slower)] image_output=[Fuse and display]");'
    SendtoArray_BlN = np.array(PreprocessedMacroLine)
    SendtoSeries_BlN = pd.Series(SendtoArray_BlN)
    SendtoDataFrame_BlN = pd.DataFrame(SendtoSeries_BlN).replace('  ',' ')
    # SendtoDataFrame_BlN.to_csv(path+'/ImageJ_Macros'+'/PreprocessedMacro_BlN_r{}.ijm'.format(j), index=False, header=False, sep=' ', quoting=csv.QUOTE_NONE, escapechar = ' ')
    SendtoDataFrame_BlN.to_csv('{}'.format(path)+'/PreprocessedMacro_BlN_r{}.ijm'.format(j), index=False, header=False, quoting=csv.QUOTE_NONE, escapechar = '\t')

# data = pd.read_table(r'C:\Users\repha\Documents\Grad School\Research\Scripts\Test 2\Macro\Postprocessed_r2.txt',sep="\s+",header= None)

    
yag = yagmail.SMTP('{}'.format(WorkStationEmail), '{}'.format(Password))

contents = ['{} Completed'.format(ScriptName)]

yag.send('{}'.format(SendToEmail), '{}'.format(ProjectName), contents)
    
toc = time.time()

print(toc-tic, 'seconds elapsed')