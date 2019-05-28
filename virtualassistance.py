import pyttsx3
import speech_recoginition as sr 
import datetime
import webbrowser
import os
import secure_smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voice',voice[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
     speak("Good Morning!") 
    elif hour>=12 and hour<18:
        speak("Good After noon!")
    else:
        speak("Good EVening!")    

    speak("I am Mia. please tell me how may i seduce you sir")    

def takecommand():

    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_thershold = 1
        audio = r.listen(source)

    try:
        print("Reconizing...")
        query = r.Recognize_google(audio, language='en-in')
        print(f"user said: {query}\n")

    except Exception as e:
         #print(e)
         print("say that again ...")
         return "None"
    return query            

def sendEmail(to, content):
    server =smtplib.SMTP('smntp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('abcd@gmai.com','password')
    server.sendmail('sendermailaddress@gmail.com',to, content)
    server.close()

if __name__ == "__main__":
     wishMe()
     while True:
         query =takecommand().lower()

         if 'wikipedia' in query:
             speak('searching wikipedia...')
             query=query.replace("wikipedia","")
             results = wikipedia.summary(query, sentences=10)
             speak("According to wikipedia")
             print(results)
             speak(results
        
         elif 'open youtube' in  query:
             webbrowser.open("youtube.com")
        
         elif 'open google' in  query:
            webbrowser.open("google.com")
        
         elif 'open stackoverflow' in  query:
            webbrowser.open("stackoverflow.com") 
         elif 'play music' in query:
            music_dir = 'D:\\music'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))


         elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"the time is {strTime}")

         elif 'email to thakurritik870' in query:
            try:
                speak('what should i say')
                content = takecommand()
                to = "Abcd8700@gmail.com"
                sendEmail(to,content)
                speak("Email has been sent!") 
            except Exception as e:
                print(e)
                speak("This mail cannot be send ")     

                      



                