@echo off
start NewSorter
start /wait Generate_Tiffs_from_Raw_Data_amended
start /wait Create_Preprocessed_ImageJ_Macros
start /wait Create_ImageJ_Preprocessed_Batch_Files
start /wait ImageJ_Preprocessed
start /wait MakeCroppedFoldersandPostprocessed
start /wait Create_Fuse_ImageJ_Macros_BlN
start /wait Create_Fuse_and_Blur_ImageJ_Macros_GrX
start /wait Create_Fuse_and_Blur_ImageJ_Macros_BlA
start /wait Create_ImageJ_MakeFuse_Batch_Files
start /wait ImageJ_Fusion_BlN
start /wait ImageJ_Fusion_GrX
start /wait ImageJ_Fusion_BlA
start /wait Create_Fuse_and_Blur_ImageJ_Macros_LRt
start /wait ImageJ_Fusion_LRt