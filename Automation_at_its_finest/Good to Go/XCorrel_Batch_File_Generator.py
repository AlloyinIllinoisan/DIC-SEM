# -*- coding: utf-8 -*-
"""
Created on Wed Jan 19 16:20:31 2022

@author: jcstinv + Rephayah
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
q = lines[1][-2] #Number of Steps
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

v = int(q) #Number of regions

n = int(GridCols)
b = int(GridRows)

newpath = directory + '/AlignedImages_step{}'.format(v)

f = open("C:\\xCorrel\\AMITEX718_step1.bat", "w+") #Change the Name and the directory below
f.write("echo off\n")
f.write("title calculation HDIC\n")
f.write("echo start calcul\n")
f.write("pause\n")
for i in range(1,b+1):
    for j in range(1,n+1):
        f.write("start /wait XCorrel_V9.11a.exe E:\\2023_AMITEX_718_3D\\DIC_Calculation\\Raw_Images\\AlignedImages_step1\\IMAFile_p%s_%s.ima\n" % (i,j))
    print('file done')
f.write("call XCorrel_Finished.bat")
f.close()
