import nltk
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import load_model

# Assume que 'texts' é uma lista de frases tokenizadas
texts = ["exemplo de frase 1", "exemplo de frase 2", ...]

# Cria um Tokenizer e ajusta no texto
tokenizer = Tokenizer()
tokenizer.fit_on_texts(texts)

# Converte o texto em sequências de números
sequences = tokenizer.texts_to_sequences(texts)

# Preenche ou trunca as sequências para ter o mesmo comprimento
padded_sequences = pad_sequences(sequences, maxlen=MAX_LENGTH)

# Carrega o modelo
model = load_model('seu_modelo.h5')

# Preveja usando o modelo
predictions = model.predict(padded_sequences)
