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
#     #open folder 
# from tkinter import filedialog
# root = tk.Tk()
# root.withdraw()
# root.attributes("-topmost", True)
# directory = filedialog.askdirectory()
# root.destroy()

with open('Pilot.txt') as f:
    lines = f.readlines()
    
MainDirectory = lines[0][16:-1]
MainDirectory = MainDirectory.replace("\\","/")
n = lines[1][-2]
n = int(n)
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

#This is the number of regions in the folder

for i in range(1,n+1):
    grxdirectory = '{}/r{}/GrX'.format(path,i)
    blndirectory = '{}/r{}/BlN'.format(path,i)
    lrtdirectory = '{}/r{}/LRt'.format(path,i)
    bladirectory = '{}/r{}/BlA'.format(path,i)
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
    grxdirectory = '{}/r{}/GrX'.format(path,j)
    blndirectory = '{}/r{}/BlN'.format(path,j)
    lrtdirectory = '{}/r{}/LRt'.format(path,j)
    bladirectory = '{}/r{}/BlA'.format(path,j)
    cropped = '/Cropped'
    newdirectorygrx = '{}/{}'.format(grxdirectory,cropped)
    newdirectorybln = '{}/{}'.format(blndirectory,cropped)
    newdirectorybla = '{}/{}'.format(bladirectory,cropped)
    newdirectorylrt = '{}/{}'.format(lrtdirectory,cropped)
    #Read in text file
    data = pd.read_table('{}/r{}/tif'.format(path,j)+"/TileConfiguration_Preprocessed.registered.txt",sep="\s+",header= None)

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
    col3extrctddata = column3[3:12]
    a = col3extrctddata.values
    
    #Populate Dummy Matrix w/ Divided Numbers from Column 3
    b= []

    for i in range(len(a)):
        c= a[i].split(")") #Remove closing parenthese
        b.append(float(c[0])/subsampling) #Append all values into list

    #Extract Data from x-Column of text file
    col2extrcteddata = column2[3:12]
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
    ll = np.array(l)

    #Separate Filler Rows & Divided Rows
    na0 = cc2r03[0]
    na1 = cc2r03[1]
    na2 = cc2r03[2]
    na3 = ll[0]
    na4 = ll[1]
    na5 = ll[2]
    na6 = ll[3]
    na7 = ll[4]
    na8 = ll[5]
    na9 = ll[6]
    na10 = ll[7]
    na11 = ll[8]

    #Append Filler Rows & Divided Rows, convert to Series
    newcol2 = pd.Series([na0, na1, na2, na3, na4, na5, na6, na7, na8, na9, na10,na11])

    #Convert Lists to Arrays for y-Column
    cc3r03 = np.array(c3r03)
    ww = np.array(w)
    #Separate Filler Rows & Divided Rows
    nb0 = cc3r03[0]
    nb1 = cc3r03[1]
    nb2 = cc3r03[2]
    nb3 = ww[0]
    nb4 = ww[1]
    nb5 = ww[2]
    nb6 = ww[3]
    nb7 = ww[4]
    nb8 = ww[5]
    nb9 = ww[6]
    nb10 = ww[7]
    nb11 = ww[8]
    
    #Append Filler Rows & Divided Rows, convert to Series
    newcol3 = pd.Series([nb0, nb1,nb2, nb3,nb4,nb5,nb6,nb7,nb8,nb9,nb10,nb11])
    
    #Concatenate All Columns & Convert to Data Frame
    newtextfile = pd.DataFrame([column0,column1,newcol2,newcol3,column4,column5,column6,column7,column8,column9])
    finalproduct = newtextfile.T #Transpose Data Frame

    #Export Data Frame as Text File
    # finalproduct.to_csv(path+'/Postprocessed.txt', header=None, index=None, sep=' ', mode='a')

    col0extrcteddata = column0[3:12]
    q = col0extrcteddata.values
    
    cc0r03 = np.array(c0r03)
    #Populate Dummy Matrix w/ Divided Numbers from Column 0
    
    # for i in d:
        #     e.append(i.strip(',').strip('(')) 

    s= []
    
    for i in q:
        s.append(i.strip('step0r{}'.format(j)).strip('.tif;')) #Append all values into list

    z = []
    for i in range(len(s)):
        z.append('step1r{}'.format(j)+str(s[i])+'.GrX_crop.tif;')
    
    k = []
    for i in range(len(s)):
        k.append('step1r{}'.format(j)+str(s[i])+'.BlA_crop.tif;')
    
    r = []
    for i in range(len(s)):
        r.append('step1r{}'.format(j)+str(s[i])+'.BlN_crop.tif;')
        
    p = []
    for i in range(len(s)):
        p.append('step1r{}'.format(j)+str(s[i])+'.LRt_crop.tif;')
        
    pp = np.array(p) #LRt
    zz = np.array(z) #GrX
    rr = np.array(r) #BlN
    kk = np.array(k) #BlA
    
    np0 = cc0r03[0]
    np1 = cc0r03[1]
    np2 = cc0r03[2]
    np3 = pp[0]
    np4 = pp[1]
    np5 = pp[2]
    np6 = pp[3]
    np7 = pp[4]
    np8 = pp[5]
    np9 = pp[6]
    np10 = pp[7]
    np11 = pp[8]
    
    newcol0_LRt = pd.Series([np0,np1,np2,np3,np4,np5,np6,np7,np8,np9,np10,np11])
    #Concatenate All Columns & Convert to Data Frame
    newtextfile_LRt = pd.DataFrame([newcol0_LRt,column1,newcol2,newcol3,column4,column5,column6,column7,column8,column9])
    finalproduct_LRt = newtextfile_LRt.T #Transpose Data Frame
    
    nz0 = cc0r03[0]
    nz1 = cc0r03[1]
    nz2 = cc0r03[2]
    nz3 = zz[0]
    nz4 = zz[1]
    nz5 = zz[2]
    nz6 = zz[3]
    nz7 = zz[4]
    nz8 = zz[5]
    nz9 = zz[6]
    nz10 = zz[7]
    nz11 = zz[8]
    
    newcol0_GrX = pd.Series([nz0, nz1,nz2, nz3,nz4,nz5,nz6,nz7,nz8,nz9,nz10,nz11])
    
    #Concatenate All Columns & Convert to Data Frame
    newtextfile_GrX = pd.DataFrame([newcol0_GrX,column1,newcol2,newcol3,column4,column5,column6,column7,column8,column9])
    finalproduct_GrX = newtextfile_GrX.T #Transpose Data Frame
    
    nr0 = cc0r03[0]
    nr1 = cc0r03[1]
    nr2 = cc0r03[2]
    nr3 = rr[0]
    nr4 = rr[1]
    nr5 = rr[2]
    nr6 = rr[3]
    nr7 = rr[4]
    nr8 = rr[5]
    nr9 = rr[6]
    nr10 = rr[7]
    nr11 = rr[8]
    
    newcol0_BlN = pd.Series([nr0, nr1,nr2, nr3,nr4,nr5,nr6,nr7,nr8,nr9,nr10,nr11])

    #Concatenate All Columns & Convert to Data Frame
    newtextfile_BlN = pd.DataFrame([newcol0_BlN,column1,newcol2,newcol3,column4,column5,column6,column7,column8,column9])
    finalproduct_BlN = newtextfile_BlN.T #Transpose Data Frame
   
    nk0 = cc0r03[0]
    nk1 = cc0r03[1]
    nk2 = cc0r03[2]
    nk3 = kk[0]
    nk4 = kk[1]
    nk5 = kk[2]
    nk6 = kk[3]
    nk7 = kk[4]
    nk8 = kk[5]
    nk9 = kk[6]
    nk10 = kk[7]
    nk11 = kk[8]

    newcol0_BlA = pd.Series([nk0, nk1,nk2, nk3,nk4,nk5,nk6,nk7,nk8,nk9,nk10,nk11])

    #Concatenate All Columns & Convert to Data Frame
    newtextfile_BlA = pd.DataFrame([newcol0_BlA,column1,newcol2,newcol3,column4,column5,column6,column7,column8,column9])
    finalproduct_BlA = newtextfile_BlA.T #Transpose Data Frame
    
    finalproduct_GrX.to_csv(newdirectorygrx+'/Postprocessed_r{}.txt'.format(j), header=None, index=None, sep=' ', mode='w')
    finalproduct_BlN.to_csv(newdirectorybln+'/Postprocessed_r{}.txt'.format(j), header=None, index=None, sep=' ', mode='w')
    finalproduct_LRt.to_csv(newdirectorylrt+'/Postprocessed_r{}.txt'.format(j), header=None, index=None, sep=' ', mode='w')
    finalproduct_BlA.to_csv(newdirectorybla+'/Postprocessed_r{}.txt'.format(j), header=None, index=None, sep=' ', mode='w')
    finalproduct.to_csv(path+'/r{}'.format(j)+'/Postprocessed_r{}.txt'.format(j), header=None, index=None, sep=' ', mode='w')
    
yag = yagmail.SMTP('{}'.format(WorkStationEmail), '{}'.format(Password))

contents = ['{} completed'.format(ScriptName)]

yag.send('{}'.format(SendToEmail), '{}'.format(ProjectName), contents)

toc = time.time()

print(toc-tic, 'seconds elapsed')