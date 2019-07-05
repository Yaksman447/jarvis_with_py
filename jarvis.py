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
                    try:
                    speak('what do you want me to say?')
                    content = myCommand()
            
                    server = smtplib.SMTP ('smtp.gmail.com', 587)
                    server.ehlo()
                    server.starttls()
                    server.login("Your_Username", 'Your_Password')
                    server.sendmail('Your_Username', "Recipient_Username", content)
                    server.close()
                    speak('Email sent!')

                except:
                    speak('Sorry ! I am unable to send your message at this moment!')


        elif 'nothing' in query or 'abort' in query or 'stop' in query:
            speak('okay')
            speak('Bye Sir, have a good day.')
            sys.exit()
           
        elif 'hello' in query:
            speak('Greetings to you')

        elif 'bye' in query:
            speak('Bye to you too, have a good day.')
            sys.exit()
                                    
        #elif 'play music' in query:
           # music_folder = Your_music_folder_path
            #music = [music1, music2, music3, music4, music5]
            #random_music = music_folder + random.choice(music) + '.mp3'
            #os.system(random_music)
                  
            #speak('Okay, here is your music! Enjoy!')
            

        else:
            query = query
            speak('Searching...')
            try:
                try:
                    res = client.query(query)
                    results = next(res.results).text
                    speak('WOLFRAM-ALPHA says - ')
                    speak('Got it.')
                    speak(results)
                    
                except:
                    results = wikipedia.summary(query, sentences=2)
                    speak('Got it.')
                    speak('WIKIPEDIA says - ')
                    speak(results)
        
            except:
                webbrowser.open('www.google.com')
        
        speak('Next Command! Sir!')
                    
            
            
      
        