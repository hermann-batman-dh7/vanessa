import pyttsx3
import speech_recognition as sr
from vanessa_bot import Bot
import core

'''engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[-2].id)
def speak(text):
    engine.say(text)
    engine.runAndWait()'''

while True:
        text = ""
        text = input("O que deseja: ")
        #Bot.speak("O que deseja: ")
        print(text)
        
        if text == 'email':
            bot_instance = Bot()
            bot_instance.sendmail()
            
        if text == 'spotify':
            bot_instance = Bot()
            bot_instance.spotify()
            
        if text == 'explorador':
             bot_instance = Bot()
             bot_instance.explorador()
             
        if text == 'google':
             bot_instance = Bot()
             bot_instance.webbrow()