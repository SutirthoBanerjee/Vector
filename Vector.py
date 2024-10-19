import cs50
import pyttsx3
import speech_recognition as sr
import datetime
import os
from requests import get
import wikipedia
import webbrowser
import sys
import time
import pyjokes
import time
import pyautogui
import requests
import operator
from bs4 import BeautifulSoup


engine =  pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[0].id)
engine.setProperty('rate', 190)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold=1
        audio = r.listen(source,timeout=1,phrase_time_limit=5)
    try:
        print("Recognizing ...")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}")
    except Exception as e:  
        return "none"
    return query
def wish():
    hour = int(datetime.datetime.now().hour)
    tt = time.strftime("%I:%M %p" )
    if hour >= 0 and hour<=12:
        speak(f"Good Morning its {tt} ")
    elif hour >= 12 and hour<=16:
        speak(f"Good Afternoon its {tt}")
    else :
        speak(f"Good Evening its {tt}")
    speak("Sir I am Vector. How may I help you")
    print(f"Its {tt} How may I help you")
def TaskExecution():   
    wish() 
    while True: 
        query = takecommand().lower()
        if "open notepad" in query:
            npath = "C:\\Windows\\system32\\notepad.exe"
            os.startfile(npath)
        elif "command prompt" in query:
            os.system("start cmd")
        elif "ip address" in query:
          ip = get('https://api.ipify.org').text
          speak(f"Sir your IP address is {ip}")
          print(f"sir your IP address is {ip}")
        elif "wikipedia" in query:
           speak("Searching Wikipedia ...")
           query = query.replace("wikipedia","")
           results = wikipedia.summary(query, sentences=2)
           speak("according to wikipedia")
           speak(results)
           print(results)
        elif "open youtube" in query:
            webbrowser.open("youtube.com")
        elif "open stack overflow" in query:
            webbrowser.open("stackoverflow.com")
        elif "open google" in query:
            speak("sir,what should i search on google")
            cm = takecommand() 
            webbrowser.open(f"{cm}")
        elif "the time" in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir the time is {strTime}")
            print(f"{strTime}")
        elif 'open code' in query:
            codepath = "C:\\Users\\Sutirtho Banerjee\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codepath)  
        elif "what is my name" in query:  
            speak("sir your name is Sutirtho Banerjee")
            print("Sutirtho Banerjee") 
        elif "close notepad" in query:
            speak("Ok sir closing notepad")
            os.system("taskkill /f /im notepad.exe")
        elif "close command" in query:
            speak("Ok sir closing command")
            os.system("taskkill /f /im cmd.exe")
        elif "joke" in query:
            joke = pyjokes.get_joke()
            speak(joke)
            print(joke)
        elif "shutdown" in query:
            os.system("shutdown /s /t 5")
        elif "restart" in query:
            os.system("shutdown /r /t 5")
        elif "hello" in query:
            speak("hello sir how are you")
        elif "who are you" in query:
            speak("I am Vector your virtual assistant")
            print("I am Vector your virtual assistant")
        elif "switch the window" in query:
            pyautogui.keyDown("alt")
            pyautogui.press("tab")
            time.sleep(1)
            pyautogui.keyUp("alt")
        elif "news for me" in query:
            speak("sir,what should i search for")
            cm = takecommand().lower()
            webbrowser.open(f"{cm}")
        elif "where am i" in query:
            speak("wait sir let me check")
            try:
                ipAdd = requests.get('https://api.ipify.org').text
                print(ipAdd)
                url = 'https://get.geojs.io/v1/ip/geo/'+ipAdd+'.json'
                geo_requests = requests.get(url)
                geo_data = geo_requests.json()
                city = geo_data['city']
                country = geo_data['country']
                speak(f"Sir I think we are in the city {city} of the country{country}")
                print(f"we are in the city {city} of the country{country}")
            except Exception as e:
                speak("sorry sir cant connect due to network issue")
                pass
        elif "calculate" in query:
            r = sr.Recognizer()
            with sr.Microphone() as source:
                speak("Say what you want to calculate")
                print("listening...")
                r.adjust_for_ambient_noise(source)
                audio = r.listen(source)
            my_string=r.recognize_google(audio)
            print(my_string)
            def get_operator_fn(op):
                return{
                    '+' : operator.add,
                    '-' : operator.sub,
                    'x' : operator.mul,
                    'divided' :operator.__truediv__,
                    }[op]
            def eval_binary_expr(op1, oper, op2):
                op1,op2 = int(op1), int(op2)
                return get_operator_fn(oper)(op1, op2)
            speak("your result is")
            speak(eval_binary_expr(*(my_string.split())))
        elif "sleep" in query:  
            speak("ok sir you can call me any time")
            sys.exit()   
        elif "thank you vector" in query:
            speak("most welcome sir")     
        elif "temperature" in query:
            search = "temperature in kolkata"
            url = f"https://www.google.com/search?q={search}"
            r = requests.get(url)
            data = BeautifulSoup(r.text,"html.parser")
            temp = data.find("div",class_="BNeawe").text
            speak(f"current {search} is {temp}")
            print(f"current {search} is {temp}")       
        elif "activate how to do mode" in query:
            from pywikihow import search_wikihow
            speak("activated sir ,what do you want to know")
            how = takecommand()
            max_result = 1
            how_to = search_wikihow(how, max_result)
            assert len(how_to) == 1
            how_to[0].print()
            speak(how_to[0].summary)
        elif "battery" in query:
            import psutil
            battery = psutil.sensors_battery()
            percentage = battery.percent
            speak(f"sir the system has {percentage} percent left")
            print(f"{percentage} percent")
        elif "internet" in query:
            import speedtest
            st = speedtest.Speedtest()
            dl = st.download()
            up = st.upload()
            speak(f"sir we have {dl} bit per second downloading speed and {up} bit per second uploading speed")
            print(f"sir we have {dl} bit per second downloading speed and {up} bit per second uploading speed")
        elif "volume up" in query:
            pyautogui.press("volumeup")
        elif "volume down" in query:
            pyautogui.press("volumedown")
        elif "mute" in query:
            pyautogui.press("volumemute")    
if __name__ == "__main__":
    while True:
        TaskExecution()                                                     