import speech_recognition as sr
from vanessa_bot import Bot
import datahora
import pyttsx3

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
    #print("Como o posso ajudar hoje? ")
    speak("Como o posso ajudar? ")
    text = input("Como o posso ajudar? ")
    #text = recognize_speech()
    print(text)
    
    qualquerapp = text.split()
    if "abra" in qualquerapp and "o" in qualquerapp:
        index_por = qualquerapp.index("o")
        abraapp = ' '.join(qualquerapp[index_por + 1:])  #Pegando as palavras após "o"
        bot_instance = Bot()
        Bot.qualquerapp(valor=abraapp)
    
    email = text     
    keywords = ['e-mail'] 
    keyword_present = any(keyword in email for keyword in keywords)    
    if keyword_present:
        bot_instance = Bot()
        bot_instance.sendmail()
        
    spotify = text     
    keywords = ['spotify'] 
    keyword_present = any(keyword in spotify for keyword in keywords)    
    if keyword_present:
        bot_instance = Bot()
        bot_instance.spotify()
        
    explorador = text     
    keywords = ['explorador'] 
    keyword_present = any(keyword in explorador for keyword in keywords)    
    if keyword_present:
        bot_instance = Bot()
        bot_instance.explorador()
        
    #Pesquisa com enrolação
    internetpesq = text     
    keywords = ['quero fazer uma pesquisa', 'preciso que pesquises por algo'] 
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
        
    horas = text     
    keywords = ['hora', 'que horas', 'diga a hora', 'diz as horas', 'que horas são'] 
    keyword_present = any(keyword in horas for keyword in keywords)    
    if keyword_present:
            speak(datahora.SystemInfo.get_time())
                
    data = text     
    keywords = ['data', 'qual a data de hoje', 'diga a data', 'diz a data de hoje'] 
    keyword_present = any(keyword in data for keyword in keywords)        
    if keyword_present:
            speak(datahora.SystemInfo.get_date())
            
    clima = text     
    keywords = ['clima', 'qual o clima de hoje', 'diga o clima', 'diz o clima de hoje'] 
    keyword_present = any(keyword in clima for keyword in keywords)        
    if keyword_present:
            city = 'Lubango'
            speak(datahora.SystemInfo.get_weather(city))
            
    encerrarpc = text     
    keywords = ['encerrar'] 
    keyword_present = any(keyword in encerrarpc for keyword in keywords)    
    if keyword_present:
        bot_instance = Bot()
        bot_instance.encerrarpc()
        
    ditado = text     
    keywords = ['anote'] 
    keyword_present = any(keyword in ditado for keyword in keywords)    
    if keyword_present:
        bot_instance = Bot()
        bot_instance.ditado()    
            
if __name__ == "__main__":
    mainact()
    
def callmainact():
    while True:
        mainact()
