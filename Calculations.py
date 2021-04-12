import Main
import wolframalpha

wolframalpha_app_id = 'YL9Q96-54XGYT22UL'
def Calculations(query):
    try:
        client = wolframalpha.Client(wolframalpha_app_id)
        index=query.lower().split().index('calculate')
        query = query.split()[index + 1:]
        res=client.query(''.join(query))
        answer = next(res.results).text
        print('The answer is:'+answer)
        Main.speak('The answer is:'+answer)
    except:
        print('Sorry, sir! I didn\'t understand that')