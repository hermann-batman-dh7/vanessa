import speech_recognition as sr
from vanessa_bot import Bot
import datahora
import pyttsx3
import threading

def mainact():
    
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
    #print("Como o posso ajudar hoje? ")
    speak("Como o posso ajudar? ")
    text = input("Como o posso ajudar? ")
    #text = recognize_speech()
    print(text)
    
    'Funcionalidades'
    
    #abrindo aplicativos e pesquisando dentro deles(os possiveis)
    qualquerapp = text.split()
    if "abra" in qualquerapp and "o" in qualquerapp:
        index_por = qualquerapp.index("o")
        abraapp = ' '.join(qualquerapp[index_por + 1:])
        bot_instance = Bot()
        Bot.qualquerapp(valor=abraapp)
        
    qualquerapp = text.split()
    if "abra" in qualquerapp and "a" in qualquerapp:
        index_por = qualquerapp.index("a")
        abraapp = ' '.join(qualquerapp[index_por + 1:])
        bot_instance = Bot()
        Bot.qualquerapp(valor=abraapp)
        
    spotify = text     
    keywords = ['spotify'] 
    keyword_present = any(keyword in spotify for keyword in keywords)    
    if keyword_present:
        bot_instance = Bot()
        bot_instance.spotify()
        
    exploradorpesq = text     
    keywords = ['explorador'] 
    keyword_present = any(keyword in exploradorpesq for keyword in keywords)    
    if keyword_present:
        bot_instance = Bot()
        bot_instance.exploradorpesq()
        
    ditado = text     
    keywords = ['anote', 'aponte,', 'escreva'] 
    keyword_present = any(keyword in ditado for keyword in keywords)    
    if keyword_present:
        bot_instance = Bot()
        bot_instance.ditado()
    
    #abrindo o app de email e enviando
    email = text     
    keywords = ['e-mail'] 
    keyword_present = any(keyword in email for keyword in keywords)    
    if keyword_present:
        bot_instance = Bot()
        bot_instance.sendmail()
         
    #Pesquisa com enrolação
    internetpesq = text     
    keywords = ['pesquisa', 'resultado', 'resultados'] 
    keyword_present = any(keyword in internetpesq for keyword in keywords)    
    if keyword_present:
        bot_instance = Bot()
        bot_instance.webbrow()
        
    #Pesquisa sem enrolação
    palavras = text.split()
    if "pesquise" in palavras and "por" in palavras:
        index_por = palavras.index("por")
        pesquisa = ' '.join(palavras[index_por + 1:])  #Pegando as palavras após "por"
        print("Você quer pesquisar por:", pesquisa)
        speak("Você quer pesquisar por: " + pesquisa) 
        bot_instance = Bot()
        Bot.pesqdir(valor=pesquisa)
        
    palavras = text.split()
    if "encontre" in palavras and "na" in palavras:
        index_por = palavras.index("na")
        pesquisa = ' '.join(palavras[index_por + 1:])  #Pegando as palavras após "por"
        print("Você quer pesquisar por:", pesquisa)
        speak("Você quer pesquisar por: " + pesquisa) 
        bot_instance = Bot()
        Bot.pesqdir(valor=pesquisa)
      
    #Informações diárias  
    horas = text     
    keywords = ['hora', 'horas'] 
    keyword_present = any(keyword in horas for keyword in keywords)    
    if keyword_present:
            print(datahora.SystemInfo.get_time())
            speak(datahora.SystemInfo.get_time())
                
    data = text     
    keywords = ['data'] 
    keyword_present = any(keyword in data for keyword in keywords)        
    if keyword_present:
            print(datahora.SystemInfo.get_date())
            speak(datahora.SystemInfo.get_date())
            
    clima = text     
    keywords = ['clima', 'temperatura'] 
    keyword_present = any(keyword in clima for keyword in keywords)        
    if keyword_present:
            city = 'Lubango'
            print(datahora.SystemInfo.get_weather(city))
            speak(datahora.SystemInfo.get_weather(city))
    
    #Automações no computador        
    hibernarpc = text     
    keywords = ['hiberne', 'supenda',  'suspende'] 
    keyword_present = any(keyword in hibernarpc for keyword in keywords)    
    if keyword_present:
        bot_instance = Bot()
        bot_instance.hibernarpc()
        
    encerarpc = text     
    keywords = ['desligue', 'encerre', 'mate'] 
    keyword_present = any(keyword in encerarpc for keyword in keywords)    
    if keyword_present:
        bot_instance = Bot()
        bot_instance.encerarpc()
        
    winpesq = text     
    keywords = ['pesquise no computador', 'ache'] 
    keyword_present = any(keyword in winpesq for keyword in keywords)    
    if keyword_present:
        bot_instance = Bot()
        bot_instance.winpesq()    
            
if __name__ == "__main__":
    mainact()
    
    thread = threading.Thread(target=mainact)
    thread.start()
    while True:
            pass
    
def callmainact():
    while True:
        mainact()
        

