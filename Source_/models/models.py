import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, Flatten, Dense
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
import numpy as np

# Dados de exemplo
texts = [
    "Esta é uma frase positiva.",
    "Outra frase positiva.",
    "Frase negativa.",
    "Uma frase negativa muito negativa."
]

labels = np.array([1, 1, 0, 0], dtype=np.int32)  # Convertido para um array numpy

# Restante do código permanece o mesmo

# Treinamento do modelo
model.fit(padded_sequences, labels, epochs=10)

# Salvamento do modelo
model.save('seu_modelo.h5')
