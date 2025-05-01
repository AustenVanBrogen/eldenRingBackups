import json
import shutil
import os
from pyuac import main_requires_admin

eldenRingPath = None
eldenRingBackupPath = None

def copyFile(sourcePath, destinationPath):
    #os.makedirs(destinationPath, existg_ok=True)
    shutil.copy(sourcePath, destinationPath)

@main_requires_admin
def main():
    with open('fileLocations.json') as fileLocations:
        fileData = json.load(fileLocations)
        eldenRingPath = fileData["eldenRingSaveLocation"]
        eldenRingBackupPath = fileData["eldenRingBackupLocation"]
        fileLocations.close()

    # print("File Location: " + eldenRingPath)
    # print("Backup File Location: " + eldenRingBackupPath)

    copyFile(eldenRingPath, eldenRingBackupPath)

if __name__ == '__main__':
    main()

