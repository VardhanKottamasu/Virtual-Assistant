import Main
import os

def OpenMSExcel():  
    Main.speak('Opening MS Excel')
    ms_excel=r'"C:/Program Files/Microsoft Office/root/Office16/EXCEL.EXE"'
    os.startfile(ms_excel)