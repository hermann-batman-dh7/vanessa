import speech_recognition as sr
import pyttsx3
import time
import threading
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QPushButton

def capturar_comando_voz():
    reconhecedor = sr.Recognizer()

    with sr.Microphone() as source:
        reproduzir_audio("Me conte alguma coisa interessante...")
        reconhecedor.adjust_for_ambient_noise(source)
        audio = reconhecedor.listen(source)

    try:
        comando = reconhecedor.recognize_google(audio)
        reproduzir_audio(f"Comando Capturado: {comando}")
        return comando.lower()  # Converta para minúsculas para facilitar a comparação
    except sr.UnknownValueError:
        reproduzir_audio("Não foi possível entender o comando.")
        return None
    except sr.RequestError as e:
        reproduzir_audio(f"Erro na requisição: {e}")
        return None

def reproduzir_audio(mensagem):
    motor = pyttsx3.init()
    motor.say(mensagem)
    motor.runAndWait()

# Função para capturar comandos de voz em uma thread separada
def captura_voz_thread():
    while True:
        comando = capturar_comando_voz()

        # Atualizar o tempo inicial sempre que houver interação do usuário
        tempo_inicial = time.time()

        if comando == "iniciar animação":
            reproduzir_audio("Iniciando animação...")
            # Lógica para iniciar a animação aqui
            
        elif comando == "parar animação":
            reproduzir_audio("Parando animação...")
            # Lógica para parar a animação aqui
            
        elif esta_no_idle():
            reproduzir_audio("Entrando em modo de espera...")
            # Lógica para a animação de idle aqui

# Função para verificar se está no estado de idle
def esta_no_idle():
    tempo_atual = time.time()
    tempo_passado = tempo_atual - tempo_inicial

    if tempo_passado >= tempo_limite_idle:
        return True
    else:
        return False

# Interface Gráfica
class MinhaUI(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(100, 100, 270, 200)
        self.setWindowTitle('Vanessa')

        self.label = QLabel(self)
        self.label.setGeometry(10, 10, 200, 30)
        self.label.setText("Aguardando comando...")

        self.botao_iniciar = QPushButton('Iniciar Animação', self)
        self.botao_iniciar.clicked.connect(self.iniciar_animacao)

        self.botao_parar = QPushButton('Parar Animação', self)
        self.botao_parar.clicked.connect(self.parar_animacao)

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.botao_iniciar)
        layout.addWidget(self.botao_parar)

        self.setLayout(layout)

    def iniciar_animacao(self):
        reproduzir_audio("Iniciando animação...")
        # Lógica para iniciar a animação aqui

    def parar_animacao(self):
        reproduzir_audio("Parando animação...")
        # Lógica para parar a animação aqui

if __name__ == '__main__':
    # Defina o tempo limite para o estado de idle (em segundos)
    tempo_limite_idle = 60  # Por exemplo, 1 minuto

    # Marque o tempo inicial
    tempo_inicial = time.time()

    # Inicie a thread de captura de voz
    thread_captura_voz = threading.Thread(target=captura_voz_thread)
    thread_captura_voz.start()

    # Inicie a interface gráfica
    app = QApplication([])
    ui = MinhaUI()
    ui.show()
    app.exec_()
