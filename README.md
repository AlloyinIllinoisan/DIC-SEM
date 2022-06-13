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

Now, place both the step0 and step# folders, with images, in your Main Directory. Then go to the "Batch Files" folder and click on "PreXCorrel.bat". This will add "step#" to every image in those folders, create the "AlignedImages_step#" directory, and align the images between step(?) and step0.

Once the image alignment has completed, you will need to proceed with the next step by hand. You need to make a text file that is "ima.ima", replacing the .txt with .ima. You will then put "step0_1_1.tif" and "step# . . ." in this .ima file, with them on different lines.

Once saved, open a random image from the most recent step in ImageJ and select a rectangle that includes the necessary number of particles. That will be your subset size. Start with a scanning zone of 10x10x10x10 and a subsampling of 3x3. Select the "Translation" mode for determining the parameters. Once no fuzz is apparent in the image (after proper setting of parameters), switch the calculation mode to "H1DIC + Translation" (or whatever is relevant to you), the jump to an appropriate value, and then check the "Jump in locale base" box in the Post-Processing section and increase the width to 8 pixels.

Run XCorrel and quit right after. You only need the ima.PAR file to save the parameters.

Open the ima.PAR file in Notepad and then open "Create IMA_PAR files.py". Input the values from ima.PAR into the labelled section, and change anything else that indicates it should be changed. Run this once all necessary changes have been made.

Then open "Generate_XCorrel_Batch.py" and change whatever has been indicated in the comments.

This will create a file in C://xCorrel, so you will need to go there and double-click on your batch file there. It will run every image in your "AlignedImages_step#" directory.

Once completed, you should receive an email, at which point you need to get back on Marshawn and go to your "Batch Files" folder again. Go to the batch file "Double_Click_Me.bat" and double-click it.

This will automatically sort all your files by extension, generate tiffs for .BlN, .LRt, .GrX, and .BlA, as well as stitch and display the resulting images. The .LRt, .GrX, and .BlA will also have a Gaussian blur applied.

You will be emailed at every step. The last step to be run is the .LRt, so if you expect .LRt images, then that will be your last email. Otherwise the last email you will receive is for the .BlA.

Once done, then you can go into the .BlN, .BlA, .GrX, and/or .LRt folders and into the "Cropped" folder within each to view the fused image.
