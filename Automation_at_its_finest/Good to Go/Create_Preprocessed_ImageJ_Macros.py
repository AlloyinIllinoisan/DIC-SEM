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
directory = MainDirectory
path = ImageJMacrosDirectory

n = int(n) #Number of regions


PreprocessedMacroLine = []
L1 = 'run("Grid/Collection stitching", "type=[Filename defined position] order=[Defined by filename         ] grid_size_x={}'.format(GridCols) +' grid_size_y={}'.format(GridRows) +' tile_overlap={}'.format(TileOverlap) + ' first_file_index_x=1 first_file_index_y=1 directory=['+'{}'.format(MainDirectory)+'/AlignedImages_step{}'.format(n)+'/tif'+ '] file_names=step0_{y}_{x}.tif output_textfile_name=TileConfiguration_Preprocessed.txt fusion_method=[Linear Blending] regression_threshold=0.30 max/avg_displacement_threshold=2.50 absolute_displacement_threshold=3.50 compute_overlap computation_parameters=[Save memory (but be slower)] image_output=[Fuse and display]");'
L2 ='close();'
PreprocessedMacroLine.append(L1)
PreprocessedMacroLine.append(L2)
SendtoArray_tif = np.array(PreprocessedMacroLine, dtype=object)
SendtoSeries_tif = pd.Series(SendtoArray_tif)
SendtoDataFrame_tif = pd.DataFrame(SendtoSeries_tif).replace('  ',' ')
    # SendtoDataFrame_tif.to_csv(path+'/ImageJ_Macros'+'/PreprocessedMacro_tif_r{}.ijm'.format(j), index=False, header=False, sep=' ', quoting=csv.QUOTE_NONE, escapechar = ' ')
SendtoDataFrame_tif.to_csv('{}'.format(path)+'/PreprocessedMacro_step0.ijm', index=False, header=False, quoting=csv.QUOTE_NONE, escapechar = '\t')

# data = pd.read_table(r'C:\Users\repha\Documents\Grad School\Research\Scripts\Test 2\Macro\Postprocessed_r2.txt',sep="\s+",header= None)

    
yag = yagmail.SMTP('{}'.format(WorkStationEmail), '{}'.format(Password))
contents = ['{} Completed'.format(ScriptName)]
yag.send('{}'.format(SendToEmail), '{}'.format(ProjectName), contents)
    
toc = time.time()

print(toc-tic, 'seconds elapsed')