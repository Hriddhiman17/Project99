import os
import shutil
import time

def remove ():
    deletedfiles = 0
    deletedfolders = 0
    path = "C:/Users/Aparna Dutta/Whitehat Jr/WorstFolderinmylife"
    days = 30
    seconds = time.time() - (days * 24 * 60 * 60)
    if(os.path.exists(path)):
        for rootFolder, folders, files in os.walk(path):
            if(seconds >= getFileFolderAge(path)):
                removeFolder(rootFolder)
                deletedfolders += 1
            else:
                for folder in folders:
                    folderpath = os.path.join(rootFolder, folder)
                    if(seconds >= getFileFolderAge(folderpath)):
                        removeFolder(folder)
                        deletedfolders += 1
                for file in files:
                    filepath =  os.path.join(rootFolder, file)
                    if(seconds >= getFileFolderAge(folderpath)):
                        removeile(file)
                        deletedfiles += 1

def getFileFolderAge(path):
    ctime = os.stat(path).st_ctime
    return ctime

def removeFolder():
    if not shutil.rmtree(path):
        print('This folder - ' + path + 'has removed successfully')
    else:
        print('Unable to delete the folder')

def removeFile():
    if not shutil.rmtree(path):
        print('This file - ' + path + 'has removed successfully')
    else:
        print('Unable to delete the file')

remove()
