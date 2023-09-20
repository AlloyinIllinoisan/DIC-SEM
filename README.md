# DIC-SEM
Processes DIC/SEM Data

Go to the <>Code button and download the zip folder.

Once both have been downloaded, please place in a location not in the directory you are running the DIC calculations on.

You will also need to have a version of Anaconda downloaded in your C:/Users/(insert name) folder inside a folder that you name "Anaconda".

Go into the "Good to Go" folder and edit the "Pilot.txt" file to assign the:
_________________________________________________________________________________________________________________________________________________________________
Main Directory: Where the main folder is that will house all of the data for your DIC project.

Number of steps: This is the step number you are on. Don't use 0, but if you are on step 1, use 1, step 2, 2, etc.

Image J Macros Directory: This is the directory you created "ImageJ_Macros"

Batch Files Directory: This is the directory you downloaded

Path to Fiji: This shouldn't be changed if using Marshawn.

Your Email: If you would like emails to alert you when a step has completed, put your email in here and activate it in the specific files you wish by uncommenting the three lines above the "toc" function. If you don't want emails, then either have Marshawn email itself.

GPU Workstation Email: Don't change if using Marshawn.

Password: Don't change.

Project Name: Change this at your leisure. It will just announce to you the project that Marshawn is working on.

Grid Cols: This is the number of columns in your DIC set.

Grid Rows: This is the number of rows in your DIC set.

Tile Overlap: This is the percent overlap between images. This is for the ImageJ macros.

Python Scripts Directory: The directory that the Pilot.txt and Python scripts are in.

xCorrel Directory: The path to xCorrel.

Python Directory: The path to your Anaconda installation.

END (DO NOT DELETE THIS)
_________________________________________________________________________________________________________________________________________________________________

CAUTION!!! THE PILOT TEXT FILE IS SPECIFIC DOWN TO THE SPACE, SO REPLACE THE NUMBER, ADDRESS, ETC. WITHOUT ADDING OR REMOVING SPACES.

!!!!!PLEASE MAKE SURE YAGMAIL IS INSTALLED ON YOUR VERSION OF ANACONDA!!!!!

Once "Pilot.txt" has been edited, you may run it in the "Pilot.py" script to make sure that everything is displayed correctly. This is important, because all of the subsequent scripts read from this text file for certain inputs.

After you are satisfied with the Pilot.txt file, you may continue to the next step. If something is not displaying correctly in the "Pilot.py" variable explorer, you must change it and then enter every single Python script in the "Good to Go" folder in order to make sure no mistakes occur.

_Note: # means an arbitrary number that is the step number_

Now, place both the step0 and step# folders, with images, in your Main Directory. Then go to the "Good to Go" folder and click the "Executor_(INITIALS).bat" that corresponds to your initials. This will add the step number to all of the step# folder images, create the Aligned Images Directory, create the necessary batch files in the Batch Files directory, and create the necessary ImageJ Macros.

Next, go into the "Batch Files" directory and double-click "Image Alignment.bat". Once the image alignment has completed, you need to check that you have the correct number of images in the Aligned Images Directory - there should be the sum of the step0 and step# images. If there are not enough images, run the "Image Alignment.bat" again. If some images have regions that are too cropped, rerun those by hand using the Template Matching tool in ImageJ.

You will need to proceed with the next step by hand. You need to make a text file in Notepad that is "ima.ima", replacing the .txt with .ima. You will then put "step0_1_1.tif" and "step# . . ." in this .ima file, with them on different lines. Save this in the Aligned Images Directory.

Once saved, open a random image from the most recent step in ImageJ and select a rectangle that includes the necessary number of particles. That will be your subset size. Start with a scanning zone of 40x40x40x40 and a subsampling of 3x3. Select the "Translation" mode for determining the parameters. Once no fuzz is apparent in the image (after proper setting of parameters), switch the calculation mode to "H1DIC + Translation" (or whatever is relevant to you), the jump to an appropriate value (which can be assessed in ImageJ by measuring the slip band width), and then check the "Jump in locale base" box in the Post-Processing section and increase the width to 8 pixels.

Run XCorrel and quit right after. You only need the ima.PAR file to save the parameters.

Open the ima.PAR file in Notepad and then open "Create IMA_PAR files.py". You no longer need to change the value in line 68. Input the values from ima.PAR into the labelled section (lines 75-81), and change anything else that indicates it should be changed. Run this script TWICE after all necessary changes have been made.

After making the .PAR and .ima files, close Spyder. You will get an error when running Double_Click_Me.bat otherwise.

You no longer have to adjust the XCorrel_Batch_File_Generator.py file. You will see a batch file appear in the C://XCorrel folder that is consistent with the parameters you placed in the Pilot.txt file. The XCorrel .bat file will be named after your ProjectName and the step number.

This will create a file in C://xCorrel, so you will need to go there and double-click on your batch file there. It will run every image in your "AlignedImages_step#" directory.

Once completed, you will receive an email from Marshawn, and then you need to get back on Marshawn and go to your "Batch Files" folder again. Go to the batch file "Double_Click_Me.bat" and double-click it. It is a difficult instruction, but I have complete confidence in your abilities.

This will automatically sort all your files by extension, generate tiffs for .BlN, .LRt, .GrX, .BlA, .DpX, .DpY, .BlL, .BlT, and/or .Tws files, as well as stitch and display the resulting images. The .LRt and .GrX will also have a Gaussian blur applied. There will also be an unblurred .GrX image.

After all of this is completed, you will receive an email informing you that your data is ready for your viewing pleasure.

You can be emailed at every step, if you so choose.

Once done, then you can go into the .BlN, .LRt, .GrX, .BlA, .DpX, .DpY, .BlL, .BlT, and/or .Tws folders and into the "Cropped" folder within each to view the fused image.
