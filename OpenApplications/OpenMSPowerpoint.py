import Main
import os

def OpenMSPowerpoint():  
    Main.speak('Opening MS Powerpoint')
    ms_ppt=r'""C:/Program Files/Microsoft Office/root/Office16/POWERPNT.EXE""'
    os.startfile(ms_ppt)