from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from main import callmainact  # Certifique-se de que a função callmainact existe em main.py

def enviar_para_terminal(event=None):
    texto = entrada_texto.get()  # Obter o texto inserido na Entry
    print(texto)
    # Aqui você pode adicionar qualquer outra lógica ou chamar a função callmainact com o texto

# Configuração da janela principal
janela = Tk()
janela.configure(bg='#282a36')
janela.title("Vanessa")

def on_minimize():
    janela.destroy()

# Propriedades da janela
largura_janela = 300
altura_janela = 300
posicao_x = (janela.winfo_screenwidth() // 2) - (largura_janela // 2)
posicao_y = (janela.winfo_screenheight() // 2) - (altura_janela // 2)
janela.geometry(f"{largura_janela}x{altura_janela}+{posicao_x}+{posicao_y}")
janela.resizable(False, False)
janela.attributes("-topmost", True)
janela.protocol("WM_DELETE_WINDOW", on_minimize)

# Estilização e estética
style = ttk.Style()
style.configure('TLabel', background='black', foreground='white', font=('Arial', 12))
style.configure('TButton', background='#4CAF50', foreground='black', font=('Arial', 12), padding=10)

# Avatar
avatar_image = PhotoImage(file="cover.png")
'''avatar_image = Image.open("miq.png")
avatar_image = avatar_image.resize((100, 100))'''
label_avatar = ttk.Label(janela, image=avatar_image)
label_avatar.pack(pady=20)

# Microfone
micro_image = Image.open("miq.png")
micro_image = micro_image.resize((50, 50))
micro_tk = ImageTk.PhotoImage(micro_image)
label_micro = ttk.Label(janela, image=micro_tk)
label_micro.place(x=120, y=210)

# Vinculando a função callmainact ao clique do botão do microfone
label_micro.bind("<Button-1>", lambda e: callmainact())

# Adicionando a Entry para inserção de texto
entrada_texto = ttk.Entry(janela, width=40)
entrada_texto.pack(pady=10)
entrada_texto.place(x=30, y=270)
# Vincular a função enviar_para_terminal ao evento 'Enter' na Entry
entrada_texto.bind("<Return>", enviar_para_terminal)

# Botão para enviar o texto inserido para o terminal
#botao_enviar = ttk.Button(janela, text="Enviar", command=enviar_para_terminal)
#botao_enviar.pack(pady=10)

janela.mainloop()
