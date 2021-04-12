import Main
import os

def OpenVSCode():  
    Main.speak('Opening Visual Studio Code')
    vsc=r'"C:/Users/Vardhan Kottamasu/AppData/Local/Programs/Microsoft VS Code/Code.exe"'
    os.startfile(vsc)