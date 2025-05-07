import json
import shutil
import os
import time
import sys
import signal
from checkProcess import testExport
from checkProcess import checkProcessStatus
import psutil

eldenRingPath = None
eldenRingBackupPath = None
secondsInTenMinutes = 600
programEnded = False
processName = "eldenring.exe"
gameIsRunning = False

def getBaseDir(path):
    endpoint = path.rfind("\\")
    baseDir = path[0:endpoint]
    return baseDir


def copyFile(sourcePath, destinationPath):

    #Makes the directory for the backup if it doesn't exist
    baseDir = getBaseDir(destinationPath)
    os.makedirs(baseDir, exist_ok=True)

    if os.path.isdir(destinationPath) == True:
        shutil.rmtree(destinationPath)
    shutil.copytree(sourcePath, destinationPath)

def main():
    while not programEnded: 

        gameIsRunning = checkProcessStatus(processName)

        if gameIsRunning:  
            with open('fileLocations.json') as fileLocations:
                fileData = json.load(fileLocations)
                eldenRingPath = fileData["eldenRingSaveLocation"]
                eldenRingBackupPath = fileData["eldenRingBackupLocation"]
                fileLocations.close()

            copyFile(eldenRingPath, eldenRingBackupPath)
            time.sleep(secondsInTenMinutes)

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("Program ended")

