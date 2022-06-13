# -*- coding: utf-8 -*-
"""
Created on Sat Mar  5 22:55:57 2022

@author: repha
"""

# -*- coding: utf-8 -*-
"""
Created on Sat Oct 30 15:44:25 2021

@author: Moose
"""

import pandas as pd
import numpy as np
import re
import os
import tkinter as tk
import time
import smtplib
import ssl
import yagmail

tic = time.time()
ScriptName = 'Make Cropped Folders and Post-processed text files'


with open('Pilot.txt') as f:
    lines = f.readlines()#     #open folder 
# from tkinter import filedialog
# root = tk.Tk()
# root.withdraw()
# root.attributes("-topmost", True)
# directory = filedialog.askdirectory()
# root.destroy()
    
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

n = int(n)
# Folder Path
path = MainDirectory

#This is the number of regions in the folder

for i in range(1,n+1):
    grxdirectory = '{}/AlignedImages_step{}/GrX'.format(path,i)
    blndirectory = '{}/AlignedImages_step{}/BlN'.format(path,i)
    lrtdirectory = '{}/AlignedImages_step{}/LRt'.format(path,i)
    bladirectory = '{}/AlignedImages_step{}/BlA'.format(path,i)
    cropped = '/Cropped'
    newdirectorygrx = '{}/{}'.format(grxdirectory,cropped)
    if not os.path.exists(newdirectorygrx):
        os.makedirs(newdirectorygrx)
    newdirectorybln = '{}/{}'.format(blndirectory,cropped)
    if not os.path.exists(newdirectorybln):
        os.makedirs(newdirectorybln)
    newdirectorylrt = '{}/{}'.format(lrtdirectory,cropped)
    if not os.path.exists(newdirectorylrt):
        os.makedirs(newdirectorylrt)
    newdirectorybla = '{}/{}'.format(bladirectory,cropped)
    if not os.path.exists(newdirectorybla):
        os.makedirs(newdirectorybla)
        
for j in range(1,n+1):
    grxdirectory = '{}/AlignedImages_step{}/GrX'.format(path,j)
    blndirectory = '{}/AlignedImages_step{}/BlN'.format(path,j)
    lrtdirectory = '{}/AlignedImages_step{}/LRt'.format(path,j)
    bladirectory = '{}/AlignedImages_step{}/BlA'.format(path,j)
    cropped = '/Cropped'
    newdirectorygrx = '{}/{}'.format(grxdirectory,cropped)
    newdirectorybln = '{}/{}'.format(blndirectory,cropped)
    newdirectorybla = '{}/{}'.format(bladirectory,cropped)
    newdirectorylrt = '{}/{}'.format(lrtdirectory,cropped)
    #Read in text file
    data = pd.read_table('{}/AlignedImages_step1/tif'.format(path)+"/TileConfiguration_Preprocessed.registered.txt",sep="\s+",header= None)

#Insert Subsampling Size
    subsampling = 3

    #Extract each column
    column0 = data[0][:]
    column1 = data[1][:]
    column2 = data[2][:]
    column3 = data[3][:]
    column4 = data[4][:]
    column5 = data[5][:]
    column6 = data[6][:]
    column7 = data[7][:]
    column8 = data[8][:]
    column9 = data[9][:]
    
    #Extract filler data
    c2r03 = data[2][0:3]
    c3r03 = data[3][0:3]
    c0r03 = data[0][0:3]

    #Extract Data from y-Column of text file
    col3extrctddata = column3[3:]
    a = col3extrctddata.values
    
    #Populate Dummy Matrix w/ Divided Numbers from Column 3
    b= []

    for i in range(len(a)):
        c= a[i].split(")") #Remove closing parenthese
        b.append(float(c[0])/subsampling) #Append all values into list

    #Extract Data from x-Column of text file
    col2extrcteddata = column2[3:]
    d = col2extrcteddata.values

    #Populate Dummy Matrix w/ Stripped Values from Column 2
    e = []

    for i in d:
        e.append(i.strip(',').strip('(')) 
    
    f  = pd.Series(e, dtype='float64') #Convert values to float64 for mathematical manipulation
    g = f/subsampling

    #Populate Dummy Matrix with parenthese and comma re-attached for x-Column
    l = []
    
    for i in range(len(g)):
        l.append('('+str(g[i])+',')

    #Populate Dummy Matrix with parenthese re-attached for y-Column
    w = []
    for i in range(len(b)):
        w.append(str(b[i])+')')

    #Convert Lists to Arrays for x-Column
    cc2r03 = np.array(c2r03)
    aa = np.array(l)

    #Separate Filler Rows & Divided Rows

    naarray = np.append(cc2r03,aa)


    #Append Filler Rows & Divided Rows, convert to Series
    newcol2 = pd.Series(naarray)

    #Convert Lists to Arrays for y-Column
    cc3r03 = np.array(c3r03)
    bb = np.array(w)
    #Separate Filler Rows & Divided Rows

    nbarray = np.append(cc3r03,bb)

    
    #Append Filler Rows & Divided Rows, convert to Series
    newcol3 = pd.Series(nbarray)
    
    #Concatenate All Columns & Convert to Data Frame
    newtextfile = pd.DataFrame([column0,column1,newcol2,newcol3,column4,column5,column6,column7,column8,column9])
    finalproduct = newtextfile.T #Transpose Data Frame

    #Export Data Frame as Text File
    # finalproduct.to_csv(path+'/Postprocessed.txt', header=None, index=None, sep=' ', mode='a')

    col0extrcteddata = column0[3:]
    q = col0extrcteddata.values
    
    cc0r03 = np.array(c0r03)
    #Populate Dummy Matrix w/ Divided Numbers from Column 0
    
    # for i in d:
        #     e.append(i.strip(',').strip('(')) 

    s= []
    
    for i in q:
        s.append(i.strip('step0'.format(j)).strip('.tif;')) #Append all values into list

    z = []
    for i in range(len(s)):
        z.append('step{}'.format(j)+str(s[i])+'.GrX_crop.tif;')
    
    k = []
    for i in range(len(s)):
        k.append('step{}'.format(j)+str(s[i])+'.BlA_crop.tif;')
    
    r = []
    for i in range(len(s)):
        r.append('step{}'.format(j)+str(s[i])+'.BlN_crop.tif;')
        
    p = []
    for i in range(len(s)):
        p.append('step{}'.format(j)+str(s[i])+'.LRt_crop.tif;')
        
    pp = np.array(p) #LRt
    zz = np.array(z) #GrX
    rr = np.array(r) #BlN
    kk = np.array(k) #BlA
    

    nparray = np.append(cc0r03,pp)

    
    newcol0_LRt = pd.Series(nparray)
    #Concatenate All Columns & Convert to Data Frame
    newtextfile_LRt = pd.DataFrame([newcol0_LRt,column1,newcol2,newcol3,column4,column5,column6,column7,column8,column9])
    finalproduct_LRt = newtextfile_LRt.T #Transpose Data Frame
    

    nzarray = np.append(cc0r03,zz)

    
    newcol0_GrX = pd.Series(nzarray)
    
    #Concatenate All Columns & Convert to Data Frame
    newtextfile_GrX = pd.DataFrame([newcol0_GrX,column1,newcol2,newcol3,column4,column5,column6,column7,column8,column9])
    finalproduct_GrX = newtextfile_GrX.T #Transpose Data Frame
    

    nrarray = np.append(cc0r03,rr)

    
    newcol0_BlN = pd.Series(nrarray)

    #Concatenate All Columns & Convert to Data Frame
    newtextfile_BlN = pd.DataFrame([newcol0_BlN,column1,newcol2,newcol3,column4,column5,column6,column7,column8,column9])
    finalproduct_BlN = newtextfile_BlN.T #Transpose Data Frame

    nkarray = np.append(cc0r03,kk)
    newcol0_BlA = pd.Series(nkarray)
 
    #Concatenate All Columns & Convert to Data Frame
    newtextfile_BlA = pd.DataFrame([newcol0_BlA,column1,newcol2,newcol3,column4,column5,column6,column7,column8,column9])
    finalproduct_BlA = newtextfile_BlA.T #Transpose Data Frame
    
    finalproduct_GrX.to_csv(newdirectorygrx+'/Postprocessed_GrX_step{}.txt'.format(j), header=None, index=None, sep=' ', mode='w')
    finalproduct_BlN.to_csv(newdirectorybln+'/Postprocessed_BlN_step{}.txt'.format(j), header=None, index=None, sep=' ', mode='w')
    finalproduct_LRt.to_csv(newdirectorylrt+'/Postprocessed_LRt_step{}.txt'.format(j), header=None, index=None, sep=' ', mode='w')
    finalproduct_BlA.to_csv(newdirectorybla+'/Postprocessed_BlA_step{}.txt'.format(j), header=None, index=None, sep=' ', mode='w')
    finalproduct.to_csv(path+'/AlignedImages_step{}'.format(j)+'/Postprocessed_step{}.txt'.format(j), header=None, index=None, sep=' ', mode='w')
    
yag = yagmail.SMTP('{}'.format(WorkStationEmail), '{}'.format(Password))

contents = ['{} completed'.format(ScriptName)]

yag.send('{}'.format(SendToEmail), '{}'.format(ProjectName), contents)

toc = time.time()

print(toc-tic, 'seconds elapsed')