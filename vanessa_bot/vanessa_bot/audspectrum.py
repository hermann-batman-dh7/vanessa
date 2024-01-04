import tkinter as tk
from tkinter import ttk
import sounddevice as sd
import numpy as np

def update_scrollbar():
    # Capture o áudio do microfone
    audio_data = sd.rec(int(sampling_rate * duration), samplerate=sampling_rate, channels=1, dtype='float32')
    sd.wait()
    
    # Calcule a média do áudio capturado
    audio_avg = np.mean(audio_data)
    
    # Atualize a posição da barra de rolagem com base no valor médio do áudio
    scrollbar.set(audio_avg * 100)  # Multiplicando por 100 para tornar a diferença mais visível
    root.after(10, update_scrollbar)  # Atualize a barra de rolagem a cada 10 milissegundos

# Configurações de áudio
sampling_rate = 44100  # Taxa de amostragem
duration = 0.1  # Duração da gravação em segundos

# Configurações da GUI
root = tk.Tk()
root.title("Visualizador de Áudio")

# Crie uma barra de rolagem horizontal (Scrollbar)
scrollbar = ttk.Scale(root, from_=0, to=100, orient="horizontal", command=None)
scrollbar.pack(pady=50)

# Inicie a atualização da barra de rolagem com base no áudio capturado
update_scrollbar()

root.mainloop()
