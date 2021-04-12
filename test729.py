# import streamlit as st
# import speech_recognition as sr
# import pymysql
# import Main


# conn=pymysql.connect(host="localhost",user="root",passwd="",db="testdb")

# mycursor=conn.cursor()

# sql = "SELECT link from univinfo where university_name='SCSVMV UNIVERSITY' and department_name ='CSE';"

# mycursor.execute(sql)
# link=mycursor.fetchall()
# link=link[0][0]
# print(link)
# conn.commit()
# conn.close()

# def takecomand():
#     r=sr.Recognizer()
#     with sr.Microphone() as source:
#         st.write("answer please....")
#         r.adjust_for_ambient_noise(source,duration=1)
#         audio=r.listen(source)
#         try:
#             text=r.recognize_google(audio)
#             st.write("You  said :",text)
#         except:
#             st.write("Please say again ..")
#         return text

# # def TakeCommand():
# #     r=sr.Recognizer()
# #     with sr.Microphone() as source:
# #         r.adjust_for_ambient_noise(source,duration=1)
# #         print('Listening........')
# #         # r.pause_threshold = 1
# #         audio = r.listen(source)

# #     try:
# #         print('Recognizing.....')
# #         query=r.recognize_google(audio,language='en-US')
# #         print(query)
# #     except Exception as e:
# #         print(e)
# #         return "None"
# #     return query

# Main.speak('Tell the name of the university')
# univname=takecomand()
# Main.speak('Which department do you want to know about?')
# deptname=takecomand()
# conn=pymysql.connect(host="localhost",user="root",passwd="",db="testdb")

# mycursor=conn.cursor()

# sql = "SELECT link from univinfo where university_name=univname and department_name =deptname"

# mycursor.execute(sql)
# link=mycursor.fetchall()
# link=link[0][0]
# print(link)
# conn.commit()
# conn.close()

# if st.button("Click me"):
#     query=takecomand().lower()
#     # if 'SCSVMV UNIVERSITY' in query and 'CSE' in query:
#     #     print(link)



import streamlit as st
import speech_recognition as sr
import pymysql
import pyttsx3

engine = pyttsx3.init()


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


# conn=pymysql.connect(host="localhost",user="root",passwd="",db="testdb")

# mycursor=conn.cursor()

# sql = "SELECT link from univinfo where university_name='SCSVMV UNIVERSITY' and department_name ='CSE';"

# mycursor.execute(sql)
# link=mycursor.fetchall()
# link=link[0][0]
# print(link)
# conn.commit()
# conn.close()

# def takecomand():
#     r=sr.Recognizer()
#     with sr.Microphone() as source:
#         st.write("answer please....")
#         r.adjust_for_ambient_noise(source,duration=1)
#         audio=r.listen(source)
#     try:
#         text=r.recognize_google(audio,language="en-US")
#         st.write("You  said :",text)
            
#     except:
#         st.write("Please say again ..")
#     return text
        
def TakeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source,duration=1)
        st.write("Listening........")
        # r.pause_threshold = 1
        audio = r.listen(source)

    try:
        st.write('Recognizing.....')
        query=r.recognize_google(audio,language='en-US')
        st.write(query)
    except Exception as e:
        st.write(e)
        return "None"
    return query

if st.button("Start Listening"):
    speak('Tell the name of the university')
    st.write("Tell the name of the university")
    univname=TakeCommand()
    speak('Which department do you want to know about?')
    st.write('Which department do you want to know about?')
    deptname=TakeCommand()
    
    conn=pymysql.connect(host="localhost",user="root",passwd="",db="testdb")

    mycursor=conn.cursor()
    tuple1=(univname,deptname)
    sql = "SELECT link from univinfo where university_name=%s and department_name =%s;"
    mycursor.execute(sql,tuple1)
    link=mycursor.fetchall()
    link=link[0][0]
    st.print(link)
    conn.commit()
    conn.close()


    # if 'SCSVMV UNIVERSITY' in query and 'CSE' in query:
    #     print(link)