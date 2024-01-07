import sounddevice as sd
import speech_recognition as sr

def capture_audio():
    fs = 44100  # Taxa de amostragem
    duration = 3  # Duração da gravação em segundos

    audio_data = sd.rec(int(fs * duration), samplerate=fs, channels=1, dtype='int16')
    sd.wait()

    return audio_data.flatten()

def recognize_speech(audio_data):
    recognizer = sr.Recognizer()
    audio_source = sr.AudioData(audio_data.tobytes(), 44100, 2)  # Corrigido aqui: 44100 para taxa de amostragem e 2 para largura da amostra (16 bits = 2 bytes)

    try:
        text = recognizer.recognize_google(audio_source)
        return text.lower()
    except sr.UnknownValueError:
        return ""

def main():
    while True:
        audio_data = capture_audio()
        text = recognize_speech(audio_data)
        
        if "oi vanessa" in text:
            print("Comando de ativação detectado!")
            # Aqui, você pode adicionar a lógica para ativar sua assistente e processar outros comandos.

if __name__ == "__main__":
    main()
