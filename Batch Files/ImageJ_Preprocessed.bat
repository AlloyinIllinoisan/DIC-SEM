@echo off
START "My Program" /D "C:\Program Files (x86)\Fiji.app" ImageJ-win64.exe -macro "D:/Scripts/RLB/Overnight Run/ImageJ_Macros/PreprocessedMacro_step0.ijm"	
TIMEOUT /T 120
START "My Program" /D "C:\Program Files (x86)\Fiji.app" ImageJ-win64.exe -macro "D:/Scripts/RLB/Overnight Run/ImageJ_Macros/PreprocessedMacro_step0.ijm"	
TIMEOUT /T 120
