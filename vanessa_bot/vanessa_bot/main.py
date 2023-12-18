from vosk import Model, KaldiRecognizer
import pyttsx3
from vanessa_bot import Bot
import speech_recognition as sr
import pyttsx3
import vanessa_bot
import core
import pyaudio
import json
'''
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[-2].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()

model = Model('model')
rec = KaldiRecognizer(model, 16000)
P = pyaudio.PyAudio()
stream = P.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=2048)
stream.start_stream()

while True:
    data = stream.read(2048, exception_on_overflow=False)
    if len(data) == 0:
        break
    if rec.AcceptWaveform(data):
        result = rec.Result()
        result = json.loads(result)

        if result is not None:
            text = result['text']
            print(text)
            if text == 'teste':
                bot_instance = Bot()
                bot_instance.sendmail()

while True:
    text = ""
    text = input("Insira ou fale alguma coisa: ")
    print(text)
    speak(text)
    index_por = text.lower().find('pesquise por')

    if index_por != -1:
        
        import webautomation
        termo_pesquisa = text[index_por + 12:].strip()
        print(f'Termo de pesquisa: {termo_pesquisa}')
        webautomation.pesq(value=termo_pesquisa)
        
    if text == 'horas':
        speak(core.SystemInfo.get_time())
   
    if text == 'data':
        speak(core.SystemInfo.get_date())

    if text == 'notas':
        vanessa_bot.notepad()
        
    if text == 'navegador':
        vanessa_bot.browser()
    
    if text == 'word':
        vanessa_bot.word() 
'''

def recognize_speech():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        speak("Diga algo...")
        print("Diga algo...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    try:
        text = recognizer.recognize_google(audio, language='pt-BR')
        return text
    except sr.UnknownValueError:
        print("Desculpe, não foi possível entender o áudio.")
        speak("Desculpe, não foi possível entender o áudio.")
        return ""
    except sr.RequestError as e:
        print(f"Não foi possível obter resultados do serviço de Reconhecimento de Fala do Google.")
        return ""
    
while True:
    def speak(text):
        engine = pyttsx3.init()
        engine.say(text)
        engine.runAndWait()

        texto_reconhecido = recognize_speech()

        if texto_reconhecido:
            print("Você disse:", texto_reconhecido)
            speak("Você disse:", texto_reconhecido)
            if texto_reconhecido == 'teste':
                if __name__ == '__main__':
                    bot_instance = Bot()
                    bot_instance.sendmail() 
                    
            #Text-to-Speech
            speak("Você disse: " + texto_reconhecido)
        else:
            print("Nenhum áudio detectado.")
        texto_reconhecido = recognize_speech()

            