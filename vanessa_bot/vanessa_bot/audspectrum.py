import numpy as np
import matplotlib.pyplot as plt
import sounddevice as sd
from tkinter import *
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Configurações de áudio
RATE = 44100  # Taxa de amostragem
DURATION = 20  # Duração de cada leitura em segundos

def capturar_audio(indata, frames, time, status):
    global line
    line.set_ydata(indata)
    plt.draw()
    root.after(10, capturar_audio, indata, frames, time, status)

def iniciar_visualizacao():
    global line, root
    fig, ax = plt.subplots()
    x = np.arange(0, RATE * DURATION)
    y = np.zeros(RATE * DURATION)
    line, = ax.plot(x, y)
    ax.set_ylim(-32768, 32767)  # Defina a amplitude máxima e mínima
    ax.set_title('Visualizador de Áudio em Tempo Real')
    ax.set_xlabel('Amostras')
    ax.set_ylabel('Amplitude')
    
    plt.ion()  # Modo interativo
    plt.show()

    with sd.InputStream(callback=capturar_audio, channels=1, samplerate=RATE):
        root.mainloop()

root = Tk()
root.title("Visualizador de Áudio em Tempo Real")

btn_iniciar = ttk.Button(root, text="Iniciar Visualização", command=iniciar_visualizacao)
btn_iniciar.pack(pady=20)

root.mainloop()
