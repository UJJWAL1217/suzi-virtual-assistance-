import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib
import pywhatkit
import pyautogui
import random
from requests import get

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
#print('voice')
#print(voice[1].id)
engine.setProperty('voice',voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("good morning!")
    elif hour>=12 and hour<18:
        speak("good afternoon")
    else :
        speak("good evening")

    speak("i am divya sir . Please tell me how may i help you")

def takeCommand():
    #takes microphone input from the user and returns string output
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold=1
        audio=r.listen(source)
    try:
        print("Recognizing...")
        query=r.recognize_google(audio, language='en-IN')
        print(f"User said : {query}\n")#print("user said:",query)
    except Exception as e:
        #print(e) print the error

        print ("say that again please....")
        speak ("say that again please....")
        return"None"
    return query

def sendEmail(to , content):# smtp lib use to send mail gmail id from less secure apps
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('ujjwal.tajne2020@vitbhopal.ac.in' , 'UJJwal17122003')
    server.sendmail('ujjwaltajne17@gmail.com',to,content)
    server.close()

def sendWhatsappmsg(to , content ):
    #pywhatkit.sendwhatmsg_instantly(to,content,5,False,3)
    pywhatkit.sendwhatmsg_instantly(to , content , 15, True, 4)


if __name__=="__main__":
    wishMe()
    while True:
         query = takeCommand().lower()

         if 'wikipedia' in query:
            speak('searching wikipedia...')
            query=query.replace("wikipedia","")
            results=wikipedia.summary(query,sentences=2)
            speak("according to wikipedia")
            print(results)
            speak(results)

         elif 'open youtube' in query:
             webbrowser.open("youtube.com")

         elif 'open whatsap' in query:
             webbrowser.open("web.whatsapp.com")

         elif 'play music' in query :
             speak('playing music')
             n=random.randint(0,8)
             music_dir='D:\\songs'
             songs=os.listdir(music_dir)
             print(list(songs))
             os.startfile(os.path.join(music_dir,songs[n]))#we can use random module and generate the number from range and play the new song

         elif 'the time' in query:
             strTime = datetime.datetime.now().strftime("%H:%M:%S")
             print(strTime)
             speak(f"sir,the time is {strTime}")

         elif 'open powerpoint' in query:
             speak('opeaning powerpoint')
             codepath="C:\\Program Files\\Microsoft Office\\root\Office16\\POWERPNT.EXE"
             os.startfile(codepath)

         elif 'send email to' in query:
             try:
                 speak("what should i send?")
                 content = takeCommand()
                 to = "ujjwaltajne17@gmail.com"
                 sendEmail(to,content)
                 speak("email has been send")
             except Exception as e:
                 print(e)
                 speak("Sorry sir , I am not able to send this mail at trhe moment")

         elif 'no thanks' in query:
             speak("thanks for using me , have a good day sir.")
             exit()

         elif 'send whatsapp message' in query:
             try:
                 print("what should i send?")
                 speak("what should i send?")
                 content=takeCommand()
                 to  = "+917974848773"
                 speak("i am sending the message")
                 sendWhatsappmsg(to , content )
                 pyautogui.press('enter')
                 speak("message has been sent")
             except Exception as e:
                 print(e)
                 speak("Sorry sir , I am not able to send this message at the moment")

         elif 'open excel' in query:
             speak('opeaning excel')
             codepath="C:\\Program Files\\Microsoft Office\\root\\Office16\\EXCEL.EXE"
             os.startfile(codepath)

         elif 'open notepad' in query:
             speak('opeaning notepad')
             codepath="C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Accessories\\Notepad.lnk"
             os.startfile(codepath)

         elif 'विकिपीडिया' in query:
            speak('searching wikipedia...')
            query=query.replace(" विकिपीडिया","")
            results=wikipedia.summary(query,sentences=2)
            speak("according to wikipedia")
            print(results)
            speak(results)

         elif 'ip address' in query:
             ip=get('https://api.ipify.org').text
             speak(f"your ip address is {ip}")
             print(ip)

         elif 'open facebook' in query:
             speak('opeaning facebook ')
             webbrowser.open('www.facebook.com')

         elif 'open Google' in query :
             speak (" sir , please tell me what should i search on google ")
             input=takeCommand().lower()
             webbrowser.open(f"{input}")

         elif 'play song on youtube' in query:
             speak('what should i play?')
             song=takeCommand().lower()
             pywhatkit.playonyt(song)
             speak('playing song on youtube')

         elif 'will you marry me' in query:
             speak('i am already married with wifi')

