import datetime
import json
import os
import random
import time
import webbrowser as wb
from urllib.request import urlopen
import psutil
import pyautogui
import pyjokes
import pyttsx3
import requests
import speech_recognition as sr
import wikipedia
import wolframalpha
import smtplib
import ssl



#Local Files
import sample
import DateTime
import CpuStatus
import Jokes
import News
import Calculations
import Screenshot
import MailService

import OpenApplications.OpenMSWord as wordloc
import OpenApplications.OpenMSExcel as excelloc
import OpenApplications.OpenMSPowerpoint as pptloc
import OpenApplications.OpenVS as vsloc
import OpenApplications.OpenVSCode as vscloc
import OpenApplications.OpenChrome as chro
import OpenApplications.OpenAndroidStudio as andro
import OpenApplications.OpenNotepad as notep
import OpenApplications.OpenMSPaint as msp

import WebQueries.Youtube as you
import WebQueries.Google as goo

engine = pyttsx3.init()
wolframalpha_app_id = 'YL9Q96-54XGYT22UL'

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# def time_():
#     Time=datetime.datetime.now().strftime('%I:%M:%S')
#     speak('The current time is')
#     speak(Time)
#     print(Time)

# def date_():
#     dateTime= datetime.datetime.now().strftime('%d:%B:%Y')
#     speak(dateTime)
#     print(dateTime)
#     # year=datetime.datetime.now().year
#     # month=datetime.datetime.now().month
#     # date=datetime.datetime.now().date.strftime()
#     # speak('The current date is')
#     # speak(date)
#     # speak(month)
#     # speak(year)

def wishme():
    speak('Hello')
    h=datetime.datetime.now().hour
    if h>=6 and h<12:
        speak('Good Morning, sir')
    elif h>=12 and h<18:
        speak('Good afternoon, Sir!')
    elif h>18 and h<22:
        speak("Good Evening, Sir!")
    else:
        speak('Good Night, Sir!')
    DateTime.time_()
    DateTime.date_()
    speak("Your Personal Assistant, at your service!")

def TakeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source,duration=1)
        print('Listening........')
        # r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print('Recognizing.....')
        query=r.recognize_google(audio,language='en-US')
        print(query)
    except Exception as e:
        print(e)
        return "None"
    return query


# def cpu():
#     usage = str(psutil.cpu_percent())
#     speak('CPU is at'+usage)
#     battery=psutil.sensors_battery()
#     # speak('battery is at')
#     speak(battery)

# def joke():
#     speak(pyjokes.get_joke())



if __name__ == "__main__":    
    # root=Tk()
    # myLabel=Label(root,text='Listening.....')
    # myLabel.pack()
           
    
    # label2=Label(root,text=query)
    # label2.pack()
    while True:
        query = TakeCommand().lower()
        if 'time' in query:
            DateTime.time_()
        elif 'date' in query:
            DateTime.date_()

        elif 'hai' in query or 'good morning' in query or 'good afternoon' in query or 'good evening' in query:
            wishme()

        elif 'introduce' in query:
            print('Hello. I\'m Vardhan\'s personal Assistant')
            speak('Hello. I\'m Vardhan\'s personal Assistant')

        elif 'youtube' in query:
            you.YoutubeSearch()
        
        elif 'google' in query:
            goo.GoogleSearch()

        elif 'cpu' in query:
            CpuStatus.cpu()

        elif 'battery' in query or 'charge' in query:
            CpuStatus.battery_status()

        elif 'joke' in query:
            Jokes.joke()

        elif 'exit' in query:
            speak('Going offline, sir')
            quit()

        elif 'word' in query:
            wordloc.OpenMSWord()

        elif 'excel' in query:
            excelloc.OpenMSExcel()

        elif 'powerpoint' in query:
            pptloc.OpenMSPowerpoint()

        elif 'visual studio' in query:
            vsloc.OpenVS()

        elif 'chrome' in query or 'browser' in query:
            chro.OpenChrome()
        
        elif 'android studio' in query:
            andro.OpenAndroidStudio()

        elif 'notepad' in query or 'text editor' in query:
            notep.OpenNotepad()

        elif 'paint' in query:
            msp.OpenMSPaint()

        elif 'take a note' in query:
            speak('What shall I write, sir?')
            notes= TakeCommand()
            file=open('notes.txt','w')
            speak('Should I include date and time, sir (yes or no)')
            ans = TakeCommand()
            if 'yes' in ans:
                strTime = datetime.datetime.now().strftime('%H:%M:%S')
                file.write(strTime)
                file.write(':-')
                file.write(notes)
                speak('Done taking notes, sir!')
            else:
                file.write(notes)
        
        elif 'show me my note' in query:
            speak('showing notes, sir')
            file = open('notes.txt','r')
            print(file.read())
            speak(file.read())

        elif 'screenshot' in query:
            Screenshot.Screenshot()
            speak('Screenshot taken, sir!')
            print('Screenshot taken, sir!')

        elif 'music' in query or 'songs' in query:
            songs_dir = 'D:\Songs'
            music=os.listdir(songs_dir)
            print('')
            speak('Sarting music, sir?')
            # ans=TakeCommand().lower()
            # if 'number' in ans:
            #     no=int(ans.replace('number',''))
            # elif 'random' in ans:
            no=random.randint(1,100)

            os.startfile(os.path.join(songs_dir,music[no]))

        elif 'remember that' in query:
            speak('What should I remember?')
            memory=TakeCommand()
            speak('You asked me remeber that'+memory)
            remember = open('memory.txt','w')
            remember.write(memory)
            remember.close()

        elif 'remember anything' in query:
            remember = open('memory.txt','r')
            speak('You asked me to remeber that'+remember.read())


        elif 'news' in query:
            News.News()


        elif 'where is' in query or 'locate' in query or 'map' in query:
            query = query.replace('where is','')
            location=query
            speak('User asked to locate'+location)
            wb.open_new_tab('https://www.google.com/maps/place/'+location)


        elif 'calculate' in query:
            Calculations.Calculations(query)
            

        elif 'what is' in query or 'who is' in query:
            client = wolframalpha.Client(wolframalpha_app_id)
            res = client.query(query)
            try:
                print(next(res.results).text)
                speak(next(res.results).text)

            except:
                print('No results, sir')    
        
        
        elif 'stop listening' in query:
            speak('For how many seconds,sir?')
            ans = int(TakeCommand())
            time.sleep(ans)
            print(ans)
        elif 'restart' in query:
            os.system('shutdown /r /t 1')
        elif 'shutdown' in query:
            os.system('shutdown /s /t 1')
        elif 'thank you'in query or 'thanks'in query or 'thank' in query:
            speak('Welcome, sir!')
        elif 'email' in query or 'mail' in query:
            MailService.mailer()
            speak('Mail sent successfully, sir!')