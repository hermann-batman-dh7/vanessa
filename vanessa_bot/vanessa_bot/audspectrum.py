import numpy as np
import matplotlib.pyplot as plt
import sounddevice as sd
from matplotlib import animation

# Configurações para a captura de áudio
fs = 44100
duration = 0.1

# Variáveis para armazenar os dados de áudio
data = np.zeros(int(fs * duration))

# Configurações do gráfico
fig, ax = plt.subplots()
line, = ax.plot([], [], lw=2)
ax.set_xlim(0, duration)
ax.set_ylim(-1, 1)

# Função de inicialização da animação
def init():
    line.set_data([], [])
    return line,

# Função de animação
def animate(i):
    global data
    data = np.roll(data, -1)
    recording = sd.rec(int(fs * duration), samplerate=fs, channels=1, blocking=True)
    recording = np.mean(recording, axis=1)
    data[-1] = recording[0]
    x = np.linspace(0, duration, len(data))
    line.set_data(x, data)
    return line,

# Crie a animação, especificando save_count para evitar o caching
ani = animation.FuncAnimation(fig, animate, init_func=init, frames=200, interval=20, blit=True, save_count=10)

# Inicie a gravação e a animação
with sd.Stream(samplerate=fs, channels=1, callback=None):
    plt.show()
