import Main
import os

def OpenAndroidStudio():  
    Main.speak('Opening Android Studio')
    android=r'"C:/Program Files/Android/Android Studio/bin/studio64.exe"'
    os.startfile(android)