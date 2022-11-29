# -*- coding: utf-8 -*-
"""
Created on Thu Jun  9 10:11:38 2022

@author: Rephayah
"""
import numpy as np

v=1
gridcols = 8
gridrows = 7
n = gridcols
b = gridrows

coords = []
for i in range(1,b+1):
    for j in range(1, n+1):
        coords.append([i,j])
        
print(coords)
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


# z = z[gridcols+2:]
# print(z)
# with open('Pilot.txt') as f:
#     lines = f.readlines()
    
# MainDirectory = lines[0][16:-1]
# MainDirectory = MainDirectory.replace("\\","/")
# n = lines[1][-2]
# ImageJMacrosDirectory = lines[2][25:-1]
# ImageJMacrosDirectory = ImageJMacrosDirectory.replace("\\","/")
# BatchFileMacrosDirectory = lines[3][23:-1]
# BatchFileMacrosDirectory = BatchFileMacrosDirectory.replace("\\","/")
# PathtoFiji = lines[4][14:-1]
# SendToEmail = lines[5][12:-1]
# WorkStationEmail = lines[6][23:-1]
# Password = lines[7][10:-1]
# ProjectName = lines[8][14:-1]
# # gridsize = lines[9][10:]

# directory = MainDirectory
# path = ImageJMacrosDirectory
# print(z)
# n = gridsize #Number of regions
import pandas as pd
import csv
# for j in range(1,n+1):
#     PreprocessedMacroLine = 'run("Grid/Collection stitching", "type=[Filename defined position] order=[Defined by filename         ] grid_size_x=3 grid_size_y=3 tile_overlap=10 first_file_index_x=0 first_file_index_y=0 directory=['+'{}'.format(MainDirectory)+'/tif'+ '] file_names=step0_{y}_{x}.tif output_textfile_name=TileConfiguration_Preprocessed.txt fusion_method=[Linear Blending] regression_threshold=0.30 max/avg_displacement_threshold=2.50 absolute_displacement_threshold=3.50 compute_overlap computation_parameters=[Save memory (but be slower)] image_output=[Fuse and display]");'
    
L2 = []
for j in range(1,v+1):
    for i in range(len(z)):
        L1 = '''open("/BlN/step{}_{}.BlN_crop.tif");'
            'selectWindow("step{}_{}.BlN_crop.tif");'''.format(j,z[i],j,z[i])
        L2.append(L1)

# path = r'C:\Users\repha\Documents\Grad School\Research\Scripts\SEM-DIC\Works on Marshawn'
L19 = 'run("Images to Stack", "name=Stack title=[] use");' #Giving Error in Batch

L20 = '//run("Brightness/Contrast...");'
L2.append(L19)
L2.append(L20)
Sad = np.array(L2, dtype=object)
Happy = pd.Series(Sad)
Confused = pd.DataFrame(Happy).replace('  ',' ')
# Confused.to_csv(path+'/Test.ijm', float_format=None, index=False, mode ='w', header=False, sep='\t', quoting=csv.QUOTE_NONE, escapechar = '\t')
