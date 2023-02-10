# -*- coding: utf-8 -*-
"""
Created on Thu Feb  9 17:57:44 2023

@author: rlb8
"""

import os
import pandas as pd
import numpy as np
import time
import glob
import tkinter as tk
import re
import csv
import shutil
from PIL import Image

tic = time.time()
ScriptName = 'Redo'

#Input step number

with open('Pilot.txt') as f:
    lines = f.readlines()#     #open folder 

# MainDirectory = lines[0][16:-1] #Main Folder
# MainDirectory = MainDirectory.replace("\\","/")
# q = lines[1][-2] #Number of Steps
# ImageJMacrosDirectory = lines[2][25:-1] #Folder Containing the ImageJ Macros
# ImageJMacrosDirectory = ImageJMacrosDirectory.replace("\\","/")
# BatchFileMacrosDirectory = lines[3][23:-1] #Folder Containing the Batch Files
# BatchFileMacrosDirectory = BatchFileMacrosDirectory.replace("\\","/")
PathtoFiji = lines[4][14:-1] #Path to ImageJ Fiji
SendToEmail = lines[5][12:-1] #Your email
WorkStationEmail = lines[6][23:-1] #Marshawn's Email
Password = lines[7][10:-1] #Password for Marshawn to get to his email
ProjectName = lines[8][14:-1] #Name of the current project
# GridCols = lines[9][11:-1] #Number of columns in the grid
# GridRows = lines[10][11:-1] #Number of rows in the grid
# TileOverlap = lines[11][14:-1] #Percentage of overlap between tiles
PythonScriptsDirectory = lines[12][26:-1] #Python Scripts Directory (Good to Go)
PythonScriptsDirectory = PythonScriptsDirectory.replace("\\","/")
xCorrelDirectory = lines[13][17:-1] #Path to xCorrel


#Select the Aligned Images Directory
from tkinter import filedialog
root = tk.Tk()
root.withdraw()
root.attributes("-topmost", True)
directory = filedialog.askdirectory()
root.destroy()

#Select the ima files of the sections you want recalculated
root = tk.Tk()
root.withdraw()
root.attributes("-topmost", True)
filestoredo = filedialog.askopenfilenames()
root.destroy()
recalculationdirectory = '{}/Recalculation'.format(directory)

# import os
# for files in os.listdir(recalculationdirectory):
#     if files.endswith(".ima"):
#         hay = os.path.join(recalculationdirectory,files)
#         # filestoredo = print(x)
# # Extracts the section numbers
# filestoredo = np.array(filestoredo)
# filestoredo = list([hay])
a = []
for i in range(len(filestoredo)):    
    gravy = filestoredo[i][-7:-4]
    a.append(gravy)

#Creates Recalculation Directory
recalculationcroppeddirectory = '{}/Recalculation/Cropped'.format(directory)
if not os.path.exists(recalculationcroppeddirectory):
    os.makedirs(recalculationcroppeddirectory)
recalculationdirectory = '{}/Recalculation'.format(directory)
stepnumber =filestoredo[0][-32:-31]
# yes = '{}'.format(a[0])
extt = ('BlN', 'GrX', 'LRt', 'BlA', 'DpX', 'DpY', 'BlL', 'BlT','ima','tif','PAR')
grxdirectory = directory+'/'+extt[1]
blndirectory = directory+'/'+extt[0]
lrtdirectory = directory+'/'+extt[2]
bladirectory = directory+'/'+extt[3]
dpxdirectory = directory+'/'+extt[4]
dpydirectory = directory+'/'+extt[5]
blldirectory = directory+'/'+extt[6]
bltdirectory = directory+'/'+extt[7]
tifdirectory = directory+'/'+extt[9]
pardirectory = directory+'/'+extt[10]
grxcroppeddirectory = grxdirectory + '/Cropped'
blncroppeddirectory = blndirectory + '/Cropped'
lrtcroppeddirectory = lrtdirectory + '/Cropped'
blacroppeddirectory = bladirectory + '/Cropped'
dpxcroppeddirectory = dpxdirectory + '/Cropped'
dpycroppeddirectory = dpydirectory + '/Cropped'
bllcroppeddirectory = blldirectory + '/Cropped'
bltcroppeddirectory = bltdirectory + '/Cropped'
#If LRT exists
# extdirectories = (blndirectory,grxdirectory,lrtdirectory,bladirectory,dpxdirectory,dpydirectory,blldirectory,bltdirectory)
# croppeddirectories = (blncroppeddirectory,grxcroppeddirectory,lrtcroppeddirectory,blacroppeddirectory,dpxcroppeddirectory,dpycroppeddirectory,bllcroppeddirectory,bltcroppeddirectory)

#If LRT Does Not Exist
extdirectories = (blndirectory,grxdirectory,bladirectory,dpxdirectory,dpydirectory,blldirectory,bltdirectory)
croppeddirectories = (blncroppeddirectory,grxcroppeddirectory,blacroppeddirectory,dpxcroppeddirectory,dpycroppeddirectory,bllcroppeddirectory,bltcroppeddirectory)

#Matrix for Row
b = []
#Matrix for Column
c = []   

for i in range(len(a)): #Populates above matrices
    d = a[i][0]
    b.append(d)
    e = a[i][2]
    c.append(e)
    
ext = ('.BlN', '.GrX', '.LRt', '.BlA', '.DpX', '.DpY', '.BlL', '.BlT')
 
# iterating over directory and subdirectory to get desired result
for root, subdirectories, files in os.walk(recalculationdirectory):
    for file in files:
        if file.endswith(ext[0]):
            # ## name is the path of a given file
            name = os.path.join(root, file) 
            ## Write Data from file in a array
            data = np.loadtxt(name)      
            ## Extract the 3 columns oif the array
            X = data[:,0]
            Y = data[:,1]
            Value = data[:,2]
            ## Extract the number of points
            nColumns = int(X[-1])+1
            nRows = int(Y[-1])+1
            ## Reshape the array of the Values 
            Value = Value.reshape((nRows,nColumns))
            ##apply Max threshold on Value
            Value[Value >20] = 0
            Value[Value <0] = 0
            ## Write a tiff image 
            img = Image.fromarray(Value)
            #img.save(name + '.tif')
            print('Image generated')
            ## Crop image - enter the croped region dimension
            X_top_left = int(0)
            Y_top_left = int(0)
            X_bottom_right = nColumns - X_top_left
            Y_bottom_right = nRows - Y_top_left
            crop_img = img.crop((X_top_left, Y_top_left, X_bottom_right, Y_bottom_right))
            crop_img.save(name + '_crop' + '.tif')
    
for root, subdirectories, files in os.walk(recalculationdirectory):
    for file in files:
        if file.endswith(ext[1]):
            # ## name is the path of a given file
            name = os.path.join(root, file)
            ## Write Data from file in a array
            data = np.loadtxt(name)      
            ## Extract the 3 columns oif the array
            X = data[:,0]
            Y = data[:,1]
            Value = data[:,2]
            ## Extract the number of points
            nColumns = int(X[-1])+1
            nRows = int(Y[-1])+1
            ## Reshape the array of the Values 
            Value = Value.reshape((nRows,nColumns))
            ##apply Max threshold on Value
            Value[Value >1] = 0
            Value[Value <-1] = 0
            ## Write a tiff image 
            img = Image.fromarray(Value)
            #img.save(name + '.tif')
            print('Image generated')
            ## Crop image - enter the croped region dimension
            X_top_left = int(0)
            Y_top_left = int(0)
            X_bottom_right = nColumns - X_top_left
            Y_bottom_right = nRows - Y_top_left
            crop_img = img.crop((X_top_left, Y_top_left, X_bottom_right, Y_bottom_right))
            crop_img.save(name + '_crop' + '.tif')
    
for root, subdirectories, files in os.walk(recalculationdirectory):
    for file in files:
        if file.endswith(ext[2]):
            # ## name is the path of a given file
            name = os.path.join(root, file) 
            ## Write Data from file in a array
            data = np.loadtxt(name)      
            ## Extract the 3 columns oif the array
            X = data[:,0]
            Y = data[:,1]
            Value = data[:,2]
            ## Extract the number of points
            nColumns = int(X[-1])+1
            nRows = int(Y[-1])+1
            ## Reshape the array of the Values 
            Value = Value.reshape((nRows,nColumns))
            ##apply Max threshold on Value
            Value[Value >4] = 0
            Value[Value <-4] = 0
            ## Write a tiff image 
            img = Image.fromarray(Value)
            #img.save(name + '.tif')
            print('Image generated')
            ## Crop image - enter the croped region dimension
            X_top_left = int(0)
            Y_top_left = int(0)
            X_bottom_right = nColumns - X_top_left
            Y_bottom_right = nRows - Y_top_left
            crop_img = img.crop((X_top_left, Y_top_left, X_bottom_right, Y_bottom_right))
            crop_img.save(name + '_crop' + '.tif')
            
for root, subdirectories, files in os.walk(recalculationdirectory):
    for file in files:
        if file.endswith(ext[3]):
            # ## name is the path of a given file
            name = os.path.join(root, file) 
            ## Write Data from file in a array
            data = np.loadtxt(name)      
            ## Extract the 3 columns oif the array
            X = data[:,0]
            Y = data[:,1]
            Value = data[:,2]
            ## Extract the number of points
            nColumns = int(X[-1])+1
            nRows = int(Y[-1])+1
            ## Reshape the array of the Values 
            Value = Value.reshape((nRows,nColumns))
            ##apply Max threshold on Value
            Value[Value >4] = 0
            Value[Value <-4] = 0
            ## Write a tiff image 
            img = Image.fromarray(Value)
            #img.save(name + '.tif')
            print('Image generated')
            ## Crop image - enter the croped region dimension
            X_top_left = int(0)
            Y_top_left = int(0)
            X_bottom_right = nColumns - X_top_left
            Y_bottom_right = nRows - Y_top_left
            crop_img = img.crop((X_top_left, Y_top_left, X_bottom_right, Y_bottom_right))
            crop_img.save(name + '_crop' + '.tif')
            
for root, subdirectories, files in os.walk(recalculationdirectory):
    for file in files:
        if file.endswith(ext[4]):
            # ## name is the path of a given file
            name = os.path.join(root, file) 
            ## Write Data from file in a array
            data = np.loadtxt(name)      
            ## Extract the 3 columns oif the array
            X = data[:,0]
            Y = data[:,1]
            Value = data[:,2]
            ## Extract the number of points
            nColumns = int(X[-1])+1
            nRows = int(Y[-1])+1
            ## Reshape the array of the Values 
            Value = Value.reshape((nRows,nColumns))
            ##apply Max threshold on Value
            Value[Value >100] = 0
            Value[Value <-100] = 0
            ## Write a tiff image 
            img = Image.fromarray(Value)
            #img.save(name + '.tif')
            print('Image generated')
            ## Crop image - enter the croped region dimension
            X_top_left = int(0)
            Y_top_left = int(0)
            X_bottom_right = nColumns - X_top_left
            Y_bottom_right = nRows - Y_top_left
            crop_img = img.crop((X_top_left, Y_top_left, X_bottom_right, Y_bottom_right))
            crop_img.save(name + '_crop' + '.tif')

for root, subdirectories, files in os.walk(recalculationdirectory):
    for file in files:
        if file.endswith(ext[5]):
            # ## name is the path of a given file
            name = os.path.join(root, file) 
            ## Write Data from file in a array
            data = np.loadtxt(name)      
            ## Extract the 3 columns oif the array
            X = data[:,0]
            Y = data[:,1]
            Value = data[:,2]
            ## Extract the number of points
            nColumns = int(X[-1])+1
            nRows = int(Y[-1])+1
            ## Reshape the array of the Values 
            Value = Value.reshape((nRows,nColumns))
            ##apply Max threshold on Value
            Value[Value >100] = 0
            Value[Value <-100] = 0
            ## Write a tiff image 
            img = Image.fromarray(Value)
            #img.save(name + '.tif')
            print('Image generated')
            ## Crop image - enter the croped region dimension
            X_top_left = int(0)
            Y_top_left = int(0)
            X_bottom_right = nColumns - X_top_left
            Y_bottom_right = nRows - Y_top_left
            crop_img = img.crop((X_top_left, Y_top_left, X_bottom_right, Y_bottom_right))
            crop_img.save(name + '_crop' + '.tif')            

for root, subdirectories, files in os.walk(recalculationdirectory):
    for file in files:
        if file.endswith(ext[6]):
            # ## name is the path of a given file
            name = os.path.join(root, file) 
            ## Write Data from file in a array
            data = np.loadtxt(name)      
            ## Extract the 3 columns oif the array
            X = data[:,0]
            Y = data[:,1]
            Value = data[:,2]
            ## Extract the number of points
            nColumns = int(X[-1])+1
            nRows = int(Y[-1])+1
            ## Reshape the array of the Values 
            Value = Value.reshape((nRows,nColumns))
            ##apply Max threshold on Value
            Value[Value >20] = 0
            Value[Value <0] = 0
            ## Write a tiff image 
            img = Image.fromarray(Value)
            #img.save(name + '.tif')
            print('Image generated')
            ## Crop image - enter the croped region dimension
            X_top_left = int(0)
            Y_top_left = int(0)
            X_bottom_right = nColumns - X_top_left
            Y_bottom_right = nRows - Y_top_left
            crop_img = img.crop((X_top_left, Y_top_left, X_bottom_right, Y_bottom_right))
            crop_img.save(name + '_crop' + '.tif')
    
for root, subdirectories, files in os.walk(recalculationdirectory):
    for file in files:
        if file.endswith(ext[7]):
            # ## name is the path of a given file
            name = os.path.join(root, file)
            ## Write Data from file in a array
            data = np.loadtxt(name)      
            ## Extract the 3 columns oif the array
            X = data[:,0]
            Y = data[:,1]
            Value = data[:,2]
            ## Extract the number of points
            nColumns = int(X[-1])+1
            nRows = int(Y[-1])+1
            ## Reshape the array of the Values 
            Value = Value.reshape((nRows,nColumns))
            ##apply Max threshold on Value
            Value[Value >20] = 0
            Value[Value <0] = 0
            ## Write a tiff image 
            img = Image.fromarray(Value)
            #img.save(name + '.tif')
            print('Image generated')
            ## Crop image - enter the croped region dimension
            X_top_left = int(0)
            Y_top_left = int(0)
            X_bottom_right = nColumns - X_top_left
            Y_bottom_right = nRows - Y_top_left
            crop_img = img.crop((X_top_left, Y_top_left, X_bottom_right, Y_bottom_right))
            crop_img.save(name + '_crop' + '.tif')
              
#Cropping the images
for j in range(len(croppeddirectories)):
               for i in range(len(a)):
                   if os.path.exists('{}/step{}_{}{}_crop.tif'.format(recalculationdirectory,stepnumber,a[i],ext[j])):
                       im = Image.open('{}/step{}_{}{}_crop.tif'.format(recalculationdirectory,stepnumber,a[i],ext[j]))
                       imbln = im.crop((21, 21, 2028, 1346))
                       imbln.save('{}/step{}_{}{}_crop.tif'.format(recalculationcroppeddirectory,stepnumber,a[i],ext[j]))
                       print('{} Image Cropped'.format(ext[j]))
                   else:
                       print('File Does Not Exist')

#Move Cropped Images
sourcefolder = recalculationcroppeddirectory
for j in range(len(croppeddirectories)):
    for i in range(len(a)):
        destination = ('{}'.format(croppeddirectories[j])+'/'+'step{}_{}{}_crop.tif'.format(stepnumber,a[i],ext[j]))
        source = ('{}/step{}_{}{}_crop.tif'.format(sourcefolder,stepnumber,a[i],ext[j]))
        if os.path.exists(destination):
            os.remove(destination)
            shutil.move(source, destination)
        else:
            pass

# Move Uncropped Generated Images
othersourcefolder=recalculationdirectory
for j in range(len(croppeddirectories)):
    for i in range(len(a)):
        destination2 = ('{}'.format(extdirectories[j])+'/'+'step{}_{}{}_crop.tif'.format(stepnumber,a[i],ext[j]))
        source2 = ('{}/step{}_{}{}_crop.tif'.format(othersourcefolder,stepnumber,a[i],ext[j]))
        if os.path.exists(destination2):
            os.remove(destination2)
            shutil.move(source2, destination2)
        else:
            pass

#Build BlN and GrX ImageJ Macro and Batch File (Put them in same macro)

exec(open("Create_Fuse_ImageJ_Macros_BlN_Redo.py").read())
exec(open("Create_Fuse_and_Blur_ImageJ_Macros_GrX_Redo.py").read())
exec(open("Create_ImageJ_MakeFuse_Redo_Batch_Files.py").read())

root = tk.Tk()
root.withdraw()
root.attributes("-topmost", True)
directory = filedialog.askdirectory()
root.destroy()
recalculationdirectory = '{}/Recalculation'.format(directory)

source3 = recalculationdirectory
destination3 = directory
newpath = directory
allfiles = os.listdir(source3)
for f in allfiles:
    source = recalculationdirectory
    destination = directory
    src_path = os.path.join(source3, f)
    dst_path = os.path.join(destination3, f)
    os.rename(src_path, dst_path)
    
list_ = os.listdir(newpath)
for file_ in list_:
    name, ext = os.path.splitext(file_)
  
    # This is going to store the extension type
    ext = ext[1:]
  
    # This forces the next iteration,
    # if it is the directory
    if ext == '':
        continue
  
    # This will move the file to the directory
    # where the name 'ext' already exists
    if os.path.exists(newpath+'/'+ext):
        shutil.move(newpath+'/'+file_, newpath+'/'+ext+'/'+file_)
  
    # This will create a new directory,
    # if the directory does not already exist
    else:
        os.makedirs(newpath+'/'+ext)
        shutil.move(newpath+'/'+file_, newpath+'/'+ext+'/'+file_)

toc = time.time()

print(toc-tic, 'seconds elapsed')














