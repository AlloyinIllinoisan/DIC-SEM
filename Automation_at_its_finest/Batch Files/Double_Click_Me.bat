@echo off
setlocal

call NewSorter_Batch.bat
call Generate_Tiffs_from_Raw_Data_amended_Batch.bat
call ImageJ_Preprocessed.bat
call MakeCroppedFoldersandMakePostprocessed_batch.bat
call ImageJ_Fusion_BlN.bat
call ImageJ_Fusion_GrX.bat
call ImageJ_Fusion_BlA.bat
call ImageJ_Fusion_LRt.bat
call Finished_Batch.bat