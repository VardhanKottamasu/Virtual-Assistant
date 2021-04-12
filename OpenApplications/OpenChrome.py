import Main
import os

def OpenChrome():  
    Main.speak('Opening Chrome')
    chr=r'"C:/Program Files (x86)/Google/Chrome/Application/chrome.exe"'
    os.startfile(chr)