import Main
import os

def OpenMSWord():  
    Main.speak('Opening Ms word')
    ms_word=r'"C:/Program Files/Microsoft Office/root/Office16/WINWORD.EXE"'
    os.startfile(ms_word)