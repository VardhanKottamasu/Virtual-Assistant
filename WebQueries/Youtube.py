import Main
import webbrowser as wb


def YoutubeSearch():
    Main.speak('What should I search in youtube')
    search_Term = Main.TakeCommand().lower()
    Main.speak("here we go to youtube")
    wb.open('https://www.youtube.com/results?search_query='+search_Term)