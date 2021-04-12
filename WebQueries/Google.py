import Main
import webbrowser as wb


def GoogleSearch():
    Main.speak('What should I search in Google')
    search_Term = Main.TakeCommand().lower()
    Main.speak("here/'s your search result")
    wb.open('https://www.google.com/search?q='+search_Term)