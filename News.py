import Main
from urllib.request import urlopen
import json

def News():
    try:
        jsonObj = urlopen('http://newsapi.org/v2/top-headlines?country=us&category=technology&apiKey=6eb338b939a84192b6929b5cd6ef3dbf')
        data = json.load(jsonObj)
        i=1
        Main.speak('Here are some top headlines, sir!')
        for item in data['articles']:
            print(str(i)+'.'+item['title']+'\n')
            print(item['description']+'\n')
            Main.speak(item['title'])
            i+=1
    except Exception as e:
        print("That/'s the news for this time..")