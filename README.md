# DIC-SEM
Processes DIC/SEM Data

Please download both the "Batch Files" and "Python Scripts" folders.

Once both have been downloaded, please place in a location not in the directory you are running the DIC calculations on.

Once you have placed the "Batch Files" and "Python Scripts" folders in a directory, create another directory called "ImageJ_Macros". The folders should have addresses of "Directory/Batch Files", "Directory/Python Scripts", and "Directory/ImageJ_Macros"

Go into the "Python Scripts" folder and edit the "Pilot.txt" file to assign the:
_________________________________________________________________________________________________________________________________________________________________
Main Directory: Where the main folder is that will house all of the data for your DIC project.

Number of steps: This is the step number you are on. Don't use 0, but if you are on step 1, use 1, step 2, 2, etc.

Image J Macros Directory: This is the directory you created "ImageJ_Macros"

Batch Files Directory: This is the directory you downloaded

Path to Fiji: This shouldn't be changed if using Marshawn.

Your Email: If you would like emails to alert you when a step has completed, put your email in here. If you don't want emails, then either have Marshawn email itself or put cmbean2@illinois.edu

GPU Workstation Email: Don't change if using Marshawn.

Password: Don't change.

Project Name: Change this at your leisure. It will just announce to you the project that Marshawn is working on.

Grid Cols: This is the number of columns in your DIC set.

Grid Rows: This is the number of rows in your DIC set.

Tile Overlap: This is the percent overlap between images. This is for the ImageJ macros.
_________________________________________________________________________________________________________________________________________________________________

Once "Pilot.txt" has been edited, you may run it in the "Pilot.py" script to make sure that everything is displayed correctly. This is important, because all of the subsequent scripts read from this text file for certain inputs.

After you are satisfied with the Pilot.txt file, you may continue to the next step. If something is not displaying correctly in the "Pilot.py" variable explorer, you must change it and then enter every single Python script in the "Python Scripts" folder in order to make sure no mistakes occur.

_Note: # means an arbitrary number that is the step number_

Now, place both the step0 and step# folders, with images, in your Main Directory. Then go to the "Good to Go" folder and click "Executor.bat". This will add the step number to all of the step# folder images, create the Aligned Images Directory, create the necessary batch files in the Batch Files directory, and create the necessary ImageJ Macros.

Next, go into the "Batch Files" directory and double-click "Image Alignment.bat". Once the image alignment has completed, you will need to proceed with the next step by hand. You need to make a text file in Notepad that is "ima.ima", replacing the .txt with .ima. You will then put "step0_1_1.tif" and "step# . . ." in this .ima file, with them on different lines. Save this in the Aligned Images Directory.

Once saved, open a random image from the most recent step in ImageJ and select a rectangle that includes the necessary number of particles. That will be your subset size. Start with a scanning zone of 40x40x40x40 and a subsampling of 3x3. Select the "Translation" mode for determining the parameters. Once no fuzz is apparent in the image (after proper setting of parameters), switch the calculation mode to "H1DIC + Translation" (or whatever is relevant to you), the jump to an appropriate value (which can be assessed in ImageJ by measuring the slip band width), and then check the "Jump in locale base" box in the Post-Processing section and increase the width to 8 pixels.

Run XCorrel and quit right after. You only need the ima.PAR file to save the parameters.

Open the ima.PAR file in Notepad and then open "Create IMA_PAR files.py". Write in the appropriate step number into line 65, then tiput the values from ima.PAR into the labelled section (lines 72-78), and change anything else that indicates it should be changed. Run this once all necessary changes have been made.

Then open "XCorrel_Batch_File_Generator.py" in the "Good to Go" folder. You need to change line 48 to be a representative name for your project, and put in the relevant step number. Line 55 needs to have the correct Aligned Images Directory address put in so it reads "f.write("start /wait XCorrel_V9.11a.exe (Insert Aligned Image Directory address here)\\IMAFile_p%s_%s.ima\n" % (i,j))" and you need to remember that the "\" in the address needs to be a "\\" when put into Python. Don't ask me why, I just work here.

This will create a file in C://xCorrel, so you will need to go there and double-click on your batch file there. It will run every image in your "AlignedImages_step#" directory.

Once completed, you need to get back on Marshawn and go to your "Batch Files" folder again. Go to the batch file "Double_Click_Me.bat" and double-click it. It is a difficult instruction, but I have complete confidence in your abilities.

This will automatically sort all your files by extension, generate tiffs for .BlN, .LRt, .GrX, .BlA, .DpX, and .DpY files, as well as stitch and display the resulting images. The .LRt, .GrX, and .BlA will also have a Gaussian blur applied.

You can be emailed at every step, if you so choose.

Once done, then you can go into the .BlN, .LRt, .GrX, .BlA, .DpX, and/or .DpY folders and into the "Cropped" folder within each to view the fused image.
