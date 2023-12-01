def vanessa():
    import pyaudio
    import speech_recognition as sr
    import pyttsx3

    # Configuração do reconhecimento de fala
    recognizer = sr.Recognizer()

    # Configuração do motor de síntese de fala
    engine = pyttsx3.init()

    def capture_and_repeat():
        with sr.Microphone() as source:
            print("O que você deseja:")
            engine.say("O que você deseja:")
            engine.runAndWait()
            audio = recognizer.listen(source)

            try:
                text = recognizer.recognize_google(audio, language="pt-BR")
                print(f"Você acabou de dizer: {text}")
                engine.say(f"Você acabou de dizer: {text}")
                engine.runAndWait()
            except sr.UnknownValueError:
                print("Não foi possível entender o áudio.")
            except sr.RequestError as e:
                print(f"Ocorreu um erro durante o reconhecimento de fala: {e}")

    if __name__ == "__main__":
        capture_and_repeat()
        
        return()
    
from tkinter import *
    
janela = Tk()
janela.title("vanessa")
texto_orientacao = Label(janela, text="Fale com a Vanessa")
texto_orientacao.grid(column=0, row=0)
    
botao = Button(janela, text="Clique Para iniciar uma conversa", command= vanessa)
botao.grid(column=0, row=1) 
    
janela.mainloop()