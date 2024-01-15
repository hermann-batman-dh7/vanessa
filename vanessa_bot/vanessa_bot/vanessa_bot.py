import pyttsx3
import speech_recognition as sr
from botcity.core import DesktopBot
import pyautogui
import time

class Bot(DesktopBot):
    @staticmethod
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

    @staticmethod
    def speak(text):
        engine = pyttsx3.init()
        engine.say(text)
        engine.runAndWait()
        
    #condições(em definições) para a exucução de determinados processos

    def sendmail(self, execution=None):
        
        Bot.speak("Abrindo o aplicativo de e-mail")
        pyautogui.press('winleft')
        time.sleep(2)
        pyautogui.typewrite('email')
        time.sleep(2)
        pyautogui.press('enter')
        
        if not self.find("novo_mail", matching=0.97, waiting_time=10000):
            self.not_found("novo_mail")
        self.click()
        
        #e-mail_para
        print("Por favor, diga para quem deseja mandar o mail")
        Bot.speak("Por favor, diga para quem deseja mandar o mail")
        variaveldetextos = Bot.recognize_speech()
        Bot.speak("O destinatário foi definodo como:"+variaveldetextos)
        pyautogui.moveTo(1061, 112)  
        pyautogui.click()
        pyautogui.typewrite(variaveldetextos)

        #assunto
        print("Qual é o assunto dessa conversa?")
        Bot.speak("Qual é o assunto dessa conversa?")
        variaveldetextos = Bot.recognize_speech()
        Bot.speak("O seu assunto escolhido foi:"+variaveldetextos)
        if not self.find("assunto", matching=0.97, waiting_time=10000):
            self.not_found("assunto")
        self.click()
        pyautogui.typewrite(variaveldetextos)

        #falacias
        print("E o que gostaria que fosse dito?")
        Bot.speak("E o que gostaria que fosse dito?")
        variaveldetextos = Bot.recognize_speech()
        Bot.speak("Você pediu que fosse escrito...:"+variaveldetextos)
        pyautogui.moveTo(1025, 275)  
        pyautogui.click()
        pyautogui.typewrite(variaveldetextos)
        
        #confirmação
        def confirm_email_send():
            while True:
                Bot.speak("Gostaria de confirmar o envio do seu e-mail?")
                variaveldetextos = Bot.recognize_speech().lower()

                if "sim" in variaveldetextos:
                    pyautogui.moveTo(1285, 54)
                    pyautogui.click()
                    Bot.speak("E-mail enviado com sucesso")
                    return  
                elif "não" in variaveldetextos:
                    pyautogui.moveTo(1188, 49)
                    pyautogui.click()
                    pyautogui.moveTo(594, 430)
                    pyautogui.click()
                    Bot.speak("E-mail descartado com sucesso")
                    return
                else:
                    Bot.speak("Desculpe, não entendi sua resposta, repita por favor.")
        confirm_email_send()
  
    def not_found(self, label):
        print(f"Element not found: {label}")
        
    def spotify(self, execution=None):
        
        Bot.speak("Abrindo o Spotify")
        pyautogui.press('winleft')
        time.sleep(1)
        pyautogui.typewrite('spotify')
        time.sleep(2)
        pyautogui.press('enter')
        
    def not_found(self, label):
        print(f"Element not found: {label}")
        
    def exploradorpesq(self, execution=None):
        
        Bot.speak("O que está procurando?")
        variaveldetextos = Bot.recognize_speech()
        Bot.speak("Procurando em seu explorador de arquivos por..." +variaveldetextos)
        pyautogui.hotkey("winleft", "e")  
        time.sleep(1)
        pyautogui.moveTo(1273, 105)
        pyautogui.typewrite(variaveldetextos)
        time.sleep(1)
        pyautogui.press('enter')
        
    def not_found(self, label):
        print(f"Element not found: {label}")
        
    def winpesq(self, execution=None):
        
        print("O que gostaria de encontrar em seu computador?")
        Bot.speak("O que gostaria de encontrar em seu computador?")
        variaveldetextos = Bot.recognize_speech()
        Bot.speak("Procurando por"+variaveldetextos)
        pyautogui.press('winleft')
        time.sleep(1)
        pyautogui.typewrite(variaveldetextos)
        time.sleep(1)
        Bot.speak("resultados encontrados.")
        
    def not_found(self, label):
        print(f"Element not found: {label}")
        
    #Pesquisa sem enrolação
    def pesqdir(valor):
        valordireto = valor
        print(valordireto)
        import websearch
        websearch.pesquisa(valordireto)
        
    def not_found(self, label):
        print(f"Element not found: {label}")
   
    #Pesquisa com enrolação
    def webbrow(self, execution=None):
        import websearch
        Bot.speak("O que gostaria de pesquisar?")
        # Captura a entrada de voz do usuário
        textofsearch = input('escreva: ')
        print(textofsearch) 
        #Bot.recognize_speech().lower()
        Bot.speak("Encontrando resultados para"+textofsearch)
        websearch.pesquisa(value=textofsearch)
        
    def not_found(self, label):
        print(f"Element not found: {label}")
        
    def qualquerapp(valor):
        
        print("Você quer abrir por:", valor)
        Bot.speak("Abrindo por"+valor)
        pyautogui.press('winleft')
        time.sleep(2)
        pyautogui.typewrite(valor)
        time.sleep(2)
        pyautogui.press('enter') 
        
    def not_found(self, label):
        print(f"Element not found: {label}")
        
    def hibernarpc():
            
        pyautogui.hotkey("winleft", "r")  
        pyautogui.typewrite("shutdown /h")
        pyautogui.sleep(2)  
        pyautogui.press("enter")
        pyautogui.sleep(5)

    def not_found(self, label):
        print(f"Element not found: {label}")
        
    def encerarpc():
        
        def confirm_encerrarpc():
            while True:
                Bot.speak("Tem certeza que deseja encerrar o computador?... Os trabalhos não salvos poderão ser perdidos, ainda assim dejesa continuar?")
                variaveldetextos = Bot.recognize_speech().lower()

                if "sim" in variaveldetextos:
                    Bot.speak("Desligando, computador")
                    pyautogui.hotkey("alf", "f4")  
                    pyautogui.sleep(1)  
                    pyautogui.press("enter")
                    return  
                elif "não" in variaveldetextos:
                    Bot.speak("Entendido, chame quando precisar")
                    pyautogui.press("esc")
                    return
                else:
                    Bot.speak("Desculpe, não entendi sua resposta, repita por favor.")
        confirm_encerrarpc()
        
    def not_found(self, label):
        print(f"Element not found: {label}")
        
    def ditado(nota):
        
        pyautogui.hotkey("winleft", "r") 
        time.sleep(1)
        pyautogui.typewrite("notepad")
        pyautogui.press("enter")
        print("O que gostaria de anotar?")
        Bot.speak("O que gostaria de anotar?")
        variaveldetextos = Bot.recognize_speech()
        Bot.speak("Você pediu que fosse escrito...:"+variaveldetextos)  
        pyautogui.typewrite(variaveldetextos)
    
    def not_found(self, label):
        print(f"Element not found: {label}")
        
    def notifs(self, execution=None):
        
        Bot.speak("Verificando as suas notificações...")
        pyautogui.hotkey('win', 'n')
    
    def not_found(self, label):
        print(f"Element not found: {label}")
        
    def notifs(self, execution=None):
        
        Bot.speak("Entendido...")
        pyautogui.hotkey('win', 'a')
    
    def not_found(self, label):
        print(f"Element not found: {label}")

if __name__ == '__main__':
    Bot.main()
