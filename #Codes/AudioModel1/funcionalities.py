import os 
from datetime import datetime

# Solicita ao usuário para inserir algo
usuario_input = input("Digite algo: ")

# Exibe o que o usuário digitou
print("Você digitou:", usuario_input)
    
if "que horas são" in usuario_input or "me diga as horas" in usuario_input or "diz as horas" in usuario_input or "horas" in usuario_input: 
    # Obtém a hora atual
    hora_atual = datetime.now().time()

    # Obtém horas e minutos
    horas = hora_atual.hour
    minutos = hora_atual.minute

    # Exibe a hora formatada
    print("São {} horas e {} minutos.".format(horas, minutos))
