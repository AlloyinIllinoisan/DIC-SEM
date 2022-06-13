@echo off
START "My Program" /D "C:\Program Files (x86)\Fiji.app" ImageJ-win64.exe -macro "D:/Scripts/RLB/Overnight Run/ImageJ_Macros/MakeFuseLRt_step1.ijm"	
TIMEOUT /T 75
