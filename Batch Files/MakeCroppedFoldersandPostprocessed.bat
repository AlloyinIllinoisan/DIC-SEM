@echo OFF
call C:\ProgramData\Anaconda3\condabin\activate.bat
cd "D:\Scripts\RLB\Overnight Run\Good to Go"
python MakeCroppedFolders_and_MakePostprocessed.py
