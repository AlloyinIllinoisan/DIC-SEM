@echo off
setlocal


call NewSorter.bat
call Generate_Tiffs_from_Raw_Data_amended.bat
call Create_Preprocessed_ImageJ_Macros.bat
call Create_ImageJ_Preprocessed_Batch_Files.bat
call ImageJ_Preprocessed.bat
call MakeCroppedFoldersandPostprocessed.bat
call Create_Fuse_ImageJ_Macros_BlN.bat
call Create_Fuse_and_Blur_ImageJ_Macros_GrX.bat
call Create_Fuse_and_Blur_ImageJ_Macros_BlA.bat
call Create_ImageJ_MakeFuse_Batch_Files.bat
call ImageJ_Fusion_BlN.bat
call ImageJ_Fusion_GrX.bat
call ImageJ_Fusion_BlA.bat
call Create_Fuse_and_Blur_ImageJ_Macros_LRt.bat
call ImageJ_Fusion_LRt.bat