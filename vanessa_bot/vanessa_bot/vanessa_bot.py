import os
from sympy import bottom_up
from vosk import Model, KaldiRecognizer
import pyttsx3
import pyautogui
import speech_recognition as sr
import time
from botcity.core import DesktopBot

engine = pyttsx3.init()

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[-2].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()

def recognize_speech():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Diga algo...")
        speak("Diga algo...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    try:
        text = recognizer.recognize_google(audio, language='pt-BR')
        return text
    except sr.UnknownValueError:
        print("Desculpe, não foi possível entender o áudio.")
        return ""
    except sr.RequestError as e:
        print("Não foi possível obter resultados do serviço de Reconhecimento de Fala do Google.")
        #speak("Não foi possível obter resultados do serviço de Reconhecimento de Fala do Google. Portanto, eu vou dar um erro. Beleza?")
        return ""

while True:
    def speak(text):
        engine = pyttsx3.init()
        engine.say(text)
        engine.runAndWait()

        # Reconhecimento de fala
    texto_reconhecido = recognize_speech()

    class Bot(DesktopBot):
        def sendmail(self, execution):
            texto_reconhecido = recognize_speech()
            pyautogui.press('winleft')
            time.sleep(2)
            speak('abrindo o aplicativo de email')
            pyautogui.typewrite('email')
            time.sleep(2)
            pyautogui.press('enter')

            if not self.find("novo_email", matching=0.97, waiting_time=10000):
                speak('iniciando a escrita de um novo email')
                self.not_found("novo_email")
            self.click()
        
            speak('para quem deseja escrever o email?')
            destino = texto_reconhecido
            pyautogui.moveTo(1009,249)
            pyautogui.typewrite(destino)
            print(destino)
                    
            if not self.find("assunto", matching=0.97, waiting_time=10000):
                self.not_found("assunto")
            self.click()
            self.paste('Hello, Im A bot')
            
            pyautogui.moveTo(959, 365)
            pyautogui.click()
            speak('o que gostaria que fosse dito?')
            falacia=texto_reconhecido
            pyautogui.typewrite(falacia)
        
            if not self.find("enviar", matching=0.97, waiting_time=10000):
                speak('enviando o seu email')
                self.not_found("enviar")
                self.click()
                
    if __name__ == '__main__':
        Bot().main()   

        def not_found(self, label):
            print(f"Element not found: {label}")               
                
'''            
def spoty(self, execution=None):
    pyautogui.press('winleft')
    time.sleep(2)
    speak('abrindo o aplicativo de spotify')
    pyautogui.typewrite('spotify')
    pyautogui.press('enter')
   
                   
def notepad():
    speak('abrindo o bloco de notas')
    os.system('notepad.exe')
    
def word():
    speak('abrindo o word')
    os.system('word.exe')
    
def browser():
    speak('abrindo o navegador')
    url="www.google.com"
    webbrowser.get().open(url)
'''