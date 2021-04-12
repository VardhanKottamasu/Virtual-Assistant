import Main
import os

def OpenVS():  
    Main.speak('Opening Visual Studio')
    vs=r'"C:/Program Files (x86)/Microsoft Visual Studio/2019/Community/Common7/IDE/devenv.exe"'
    os.startfile(vs)