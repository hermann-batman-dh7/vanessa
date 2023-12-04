import http
import webbrowser
import os
import webbrowser
import webautomation

def pesq(value):
    url = "https://www.google.com/search?q="
    webbrowser.get().open(url + value)

# Obtém a entrada do usuário
entrada_usuario = input('Digite algo: ')

# Procura pela palavra "por" na entrada do usuário
index_por = entrada_usuario.lower().find('por')

# Se "por" estiver presente, obtenha o texto após "por" e remova espaços em branco extras
if index_por != -1:
    termo_pesquisa = entrada_usuario[index_por + 3:].strip()
    print(f'Termo de pesquisa: {termo_pesquisa}')

    # Chama a função pesq com o termo de pesquisa
    webautomation.pesq(value=termo_pesquisa)
else:
    print('A palavra "por" não foi encontrada na entrada do usuário.')
