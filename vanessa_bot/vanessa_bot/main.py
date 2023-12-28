import speech_recognition as sr
from vanessa_bot import Bot
import datahora
import os
import pyaudio
import pyttsx3
import json


def mainact():
    
    #função de speak da máquina
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[-2].id)
    
    def speak(text):
        engine.say(text)
        engine.runAndWait()
    
    def recognize_speech():
        recognizer = sr.Recognizer()

        with sr.Microphone() as source:
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source)
        try:
            text = recognizer.recognize_google(audio, language='pt-BR')
            return text
        except sr.UnknownValueError:
            print("Desculpe, não foi possível entender o áudio.")
            Bot.speak("Desculpe, não foi possível entender o áudio.")
            return ""
        except sr.RequestError as e:
            print(f"Não foi possível obter resultados do serviço de Reconhecimento de Fala do Google.")
            return ""
    
    text = ""
    speak("O que você deseja: ")
    text = input("O que você deseja: ")
    #text = recognize_speech()
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
        
    horas = text     
    keywords = ['hora', 'que horas', 'diga a hora', 'diz as horas', 'que horas são'] 
    keyword_present = any(keyword in horas for keyword in keywords)    
    if keyword_present:
            speak(datahora.SystemInfo.get_time())
                 
    data = text     
    keywords = ['data', 'qual a data de hoje', 'diga a data', 'diz a data de hoje'] 
    keyword_present = any(keyword in horas for keyword in keywords)        
    if keyword_present:
            speak(datahora.SystemInfo.get_date())
            
    clima = text     
    keywords = ['clima', 'qual o clima de hoje', 'diga o clima', 'diz o clima de hoje'] 
    keyword_present = any(keyword in horas for keyword in keywords)        
    if keyword_present:
            city = 'Lubango'
            speak(datahora.SystemInfo.get_weather(city))
            
            
if __name__ == "__main__":
    mainact()