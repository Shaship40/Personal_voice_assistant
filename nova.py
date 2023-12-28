import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib
from config import apikey
import random
import numpy as np
import openai
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import time
from time import sleep
import pywhatkit
import pyautogui
import requests
from personal import *
import wolframalpha

engine = pyttsx3.init('sapi5')

voices= engine.getProperty('voices') #getting details of current voice

engine.setProperty('voice', voices[0].id)

wolfram_app = wolframalpha.Client(WolframKey)


def searchYoutube(query):
     
        query = query.replace("youtube search","")
        query = query.replace("youtube","")
        query = query.replace("jarvis","")
        # web  = "https://www.youtube.com/results?search_query=" + query
        # webbrowser.open(web)
        pywhatkit.playonyt(query)

def Wolfram_Alpha(query):
    try:
        response = wolfram_app.query(query)
        result = next(response.results).text
        return result
    except Exception as e:
        print(f"Error: {e}")
        return "Sorry, I couldn't understand that."
        
        

def speak(audio):

    engine.say(audio) 

    engine.runAndWait() #Without this command, speech will not be audible to us.

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<16:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("I am Nova Sir. Please tell me how may I help you") 


def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

        if "search on Google" in query.lower():
            search_term = query.lower().replace("search on google", "").strip()
            google_search_url = f"https://www.google.com/search?q={search_term}"
            speak(f"Searching {search_term} on Google...")
            webbrowser.open(google_search_url)
            return "None"

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query


if __name__=="__main__" :
    wishMe()
    while True:
       query = takeCommand().lower()
       sites = [ ["wikipedia", "https://www.wikipedia.com"], ["google", "https://www.google.com"], ["facebook", "https://www.facebook.com"], ["instagram" , "https://www.instagram.com"], ["twitter" , "https://www.twitter.com"] , ["stackoverflow" , "https://www.satckoverflow.com"], ["linkedin", "https://www.linkedin.com"] , ["whatsapp","https://www.whatsapp.com"] ,["netflix" , "https://www.netflix.com"] , ["amazon","https://www.amazon.com"] ,["reddit", "https://www.reddit.com"]]
       for site in sites:
            if f"Open {site[0]}".lower() in query.lower():
                speak(f"Opening {site[0]} sir...")
                webbrowser.open(site[1])

    # Logic for executing tasks based on query
       if 'search wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)      


    #    elif "youtube search" in query:
    #        searchYoutube()
       elif 'search youtube' in query or 'music' in query or 'song' in query:
        speak("Sure, what would you like to search?")
        user_input = takeCommand()
        searchYoutube(user_input)  # Pass the user's input to the searchYoutube function
        speak("Done, Sir")

       elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")
      
       elif 'open code' in query:
            codePath = "C:\\Users\\shash\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
            
       elif "stop".lower() in query.lower():
            exit()

       elif 'question' in query.lower():  # Modify this condition based on how you want to trigger Wolfram Alpha
            speak("Sure, let me find the answer for you.")
            takeCommand(query)
            result = Wolfram_Alpha(query)  # Use the Wolfram_Alpha function to get the answer
            speak(result)

 
    
