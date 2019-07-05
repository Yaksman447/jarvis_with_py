import pyttsx
import webbrowser
import smtplib
import ramdom 
import speach_recgnition as $r
import wikipedia
import datetime
import wolframalpha
import os
import sys

engine = pyttsx3.init('sap15')
   
   #GOTO WOLFRAMALPHA.COM
 
client = wolframalpha.client('JW6Y7Q-GKWVR76AJG')

voice = engine.getProperty('voice')
engine.setProperty('voice', voices[len(voices)-1].id)

def speak(audio) : 
    prin('computer: ' + audio)
    engine.say(audio)
    engine.runAndWait()
def greetMe() : 
    currentH = int(dateme.dateme.now().hour)
    if cureentH >= 0 and cureentH < 12:
        speak('Good Morning!')
        
    if currentH >= 12 and cureentH < 18:
        speak ('Good Aternoon!') 
        
    if currentH >= 18 and currentH != 0:
        speak ('Good Evening!')
               
greetme() 


speak( 'Hollo, i am your digital Assistant Peace, The Lady Jarvis, glad to see you around')
speak('How can i help you today')


def myComand():
    
    r = sr.Recognizer()
    with sr.microphone() as source:
        print('listening.....')       
        r.puse_threshold = 1 
        audio = r.listen(source)
    try:
        query = r.recognize_google(audio, language='en-in')
        print('user:' + query + '\n' )
        
    except sr.unknownValueError 
        speak("sorry! i didn't get that! please try typing your request or command")
        query = str(input('commad: '))
        
    return query 

if __name__ == '__main__':
    
    while True:
        query = myCommand();
        query = query.lower()
        
        if 'Open youyube' in query:
            speak('okay')
            webbrowser.open('www.youtube.com')
            
        elif 'open facebook' in query:
            speak('okay') 
            webbrowser.open('www.facebook.com')
        elif 'open google' in query:
            speak('okay')
            webbrowser.open('www.google.com')
        elif 'open gmail' in query:
            webbrowser.open('www.gmail.com')
        elif "what's up" in query or "how are you" in query:
           stmsg = ["just doing my thing ", "i am fine thanks for asking", "i am great and gull of enrgy" ]
           
            
        elif 'Send an Email' in query:
            speak('Who is the Recipient Please?') 
            recipient= myCommand()
            
            if 'Me' in recipient
                    speak('what should i say')
                    content = myCommand()
            
                    server = smtplib.SMTP ('smtp.gmail.com', 587)
                    server.ehlo()
                    server.starttls()
                    
                    
            
            
      
                  
        
        


