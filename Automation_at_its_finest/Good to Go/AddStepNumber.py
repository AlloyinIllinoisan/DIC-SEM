# -*- coding: utf-8 -*-
"""
Created on Sun Jun 12 13:56:15 2022

@author: Rephayah
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
import os

tic = time.time()
ScriptName = 'Add Step Number'

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
xCorrelDirectory = lines[13][17:] #Path to xCorrel
directory = MainDirectory
path = ImageJMacrosDirectory

v = int(v)

newpathstep0 = directory + '/step0'
newpathstep1 = directory + '/step1'
newpath = directory + '/step{}'.format(v)

if (v == 1):
    for root, dirs, files in os.walk(newpathstep0):
        if not files:
            continue
        prefix = os.path.basename(root)
        for f in files:
            os.rename(os.path.join(root, f), os.path.join(root, "{}_{}".format(prefix, f)))
            
    for root, dirs, files in os.walk(newpathstep1):
        if not files:
            continue
        prefix = os.path.basename(root)
        for f in files:
            os.rename(os.path.join(root, f), os.path.join(root, "{}_{}".format(prefix, f)))
else:
    for root, dirs, files in os.walk(newpath):
        if not files:
            continue
        prefix = os.path.basename(root)
        for f in files:
            os.rename(os.path.join(root, f), os.path.join(root, "{}_{}".format(prefix, f)))
