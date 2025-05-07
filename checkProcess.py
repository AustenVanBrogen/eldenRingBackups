import wmi

def testExport():
    print("Sup bitch?!?")

def checkProcessStatus(processName):
    gameIsRunning = False
    
    f = wmi.WMI()
    for process in f.Win32_Process():
        if process.Name == processName:
            return True