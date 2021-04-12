import Main
import pyautogui
import datetime

def Screenshot():
    Time=datetime.datetime.now().strftime('%I%M%S')
    l=str(Time)
    img= pyautogui.screenshot()
    img.save('C:/Users/Vardhan Kottamasu/Pictures/AssistantScreenshots/'+l+'-screenshot.png')