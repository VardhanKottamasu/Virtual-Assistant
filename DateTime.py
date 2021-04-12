import datetime
import Main

def time_():
    Time=datetime.datetime.now().strftime('%I:%M:%S')
    Main.speak('The current time is')
    Main.speak(Time)
    print(Time)

def date_():
    dateTime= datetime.datetime.now().strftime('%d:%B:%Y')
    Main.speak(dateTime)
    print(dateTime)