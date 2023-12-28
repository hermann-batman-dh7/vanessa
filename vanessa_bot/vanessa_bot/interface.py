import pyttsx3 
from tkinter import *
from main import mainact

janela = Tk()
janela.title("Vanessa")

largura_janela = 300
altura_janela = 300
posicao_x = (janela.winfo_screenwidth() // 2) - (largura_janela // 2)
posicao_y = (janela.winfo_screenheight() // 2) - (altura_janela // 2)

janela.geometry(f"{largura_janela}x{altura_janela}+{posicao_x}+{posicao_y}")
janela.resizable(False, False)

# Carregando e exibindo a imagem
imagem = PhotoImage(file="cover.png")
label_imagem = Label(janela, image=imagem)
label_imagem.pack(pady=20)

texto_orientacao = Label(janela, text="Fale com a Vanessa")
texto_orientacao.pack(pady=10)  # Ajustei o padding para acomodar a imagem

botao = Button(janela, text="Clique Para iniciar uma conversa", command=mainact)
botao.pack(pady=0)

'''entrada_texto = Entry(janela, width=50)

entrada_texto.pack(pady=20)

# Botão para enviar a entrada
botao = Button(janela, text="Enviar", command=mainact)
botao.pack(pady=20)'''

janela.mainloop()
