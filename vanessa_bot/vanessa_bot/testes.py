import speech_recognition as sr
import pyautogui

def ditado_para_texto():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Fale algo...")
        recognizer.adjust_for_ambient_noise(source)  # Ajusta para o ruído ambiente
        audio = recognizer.listen(source, timeout=10)  # Escuta por 10 segundos (ajuste conforme necessário)

    try:
        texto = recognizer.recognize_google(audio, language="pt-BR")  # Reconhecimento de voz usando Google Speech Recognition
        return texto
    except sr.UnknownValueError:
        print("Não foi possível entender o áudio.")
    except sr.RequestError as e:
        print(f"Erro na requisição ao Google Speech Recognition service")

    return None

def escrever_no_word(texto):
    # Substitua o caminho pelo caminho real do Word ou do programa de texto desejado
    pyautogui.hotkey("winleft", "r")  # Ativa a caixa de execução (substitua "winleft" pelo atalho no seu sistema)
    pyautogui.typewrite("notepad")  # Substitua "winword.exe" pelo executável do Word ou do programa de texto desejado
    pyautogui.press("enter")

    # Aguarda um momento para o Word iniciar (ajuste conforme necessário)
    pyautogui.sleep(5)

    # Digita o texto no Word
    pyautogui.typewrite(texto)

if __name__ == "__main__":
    while True:
        texto_ditado = ditado_para_texto()

        if texto_ditado:
            print(f"Texto reconhecido: {texto_ditado}")
            escrever_no_word(texto_ditado)
