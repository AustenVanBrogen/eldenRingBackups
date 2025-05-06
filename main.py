import json
import shutil
import os

eldenRingPath = None
eldenRingBackupPath = None


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
    with open('fileLocations.json') as fileLocations:
        fileData = json.load(fileLocations)
        eldenRingPath = fileData["eldenRingSaveLocation"]
        eldenRingBackupPath = fileData["eldenRingBackupLocation"]
        fileLocations.close()

    copyFile(eldenRingPath, eldenRingBackupPath)

if __name__ == '__main__':
    main()

