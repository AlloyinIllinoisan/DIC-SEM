# -*- coding: utf-8 -*-
"""
Created on Tue Jan 18 20:06:33 2022

@authors: Moose + Pollock
"""

# importing the module
import os
import numpy as np
import os
#from skimage.feature import match_template, register_translation
import scipy
import time
import yagmail
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
tic = time.time()
ScriptName = 'Generating Tiffs from Raw Data'

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
# giving directory name
# directory = r'C:\Users\repha\Documents\Grad School\Research\Fiddling\r1_0_0'
 
# giving file extensions
ext = ('.BlN', '.GrX', '.LRt', '.BlA')
 
# iterating over directory and subdirectory to get desired result
for root, subdirectories, files in os.walk(directory):
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
    
for root, subdirectories, files in os.walk(directory):
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
    
for root, subdirectories, files in os.walk(directory):
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
            
for root, subdirectories, files in os.walk(directory):
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
            
yag = yagmail.SMTP('{}'.format(WorkStationEmail), '{}'.format(Password))

contents = ['{} Completed'.format(ScriptName)]

yag.send('{}'.format(SendToEmail), '{}'.format(ProjectName), contents)
    
toc = time.time()

print(toc-tic, 'seconds elapsed')
