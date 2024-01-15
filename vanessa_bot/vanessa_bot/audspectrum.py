import numpy as np
import matplotlib.pyplot as plt

# Gerando um sinal de exemplo
fs = 1000  # Frequência de amostragem (Hz)
t = np.linspace(0, 1, fs, endpoint=False)  # Vetor de tempo de 1 segundo
f = 5  # Frequência do sinal (Hz)
signal = np.sin(2 * np.pi * f * t)  # Sinal senoidal

# Criando o espectrograma
plt.specgram(signal, Fs=fs, cmap='viridis')

# Personalizando o gráfico (opcional)
plt.title('Espectrograma do Sinal')
plt.xlabel('Tempo [s]')
plt.ylabel('Frequência [Hz]')
plt.colorbar(label='Intensidade dB')

# Mostrando o gráfico
plt.show()
