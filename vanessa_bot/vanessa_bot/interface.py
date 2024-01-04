from tkinter import *
from tkinter import ttk
from main import mainact

def on_minimize():
    "Intercepta a ação de minimizar e reativa o comportamento padrão de fechar a janela."
    janela.destroy()

janela = Tk()
janela.configure(bg='black')
janela.title("vanessa")

largura_janela = 350
altura_janela = 350

posicao_x = (janela.winfo_screenwidth() // 2) - (largura_janela // 2)
posicao_y = (janela.winfo_screenheight() // 2) - (altura_janela // 2)

janela.geometry(f"{largura_janela}x{altura_janela}+{posicao_x}+{posicao_y}")
janela.resizable(False, False)

# Definir janela como sempre no topo
janela.attributes("-topmost", True)

# Intercepta o evento de minimizar
janela.protocol("WM_DELETE_WINDOW", on_minimize)

# Estilização com ttk
style = ttk.Style()
style.configure('TLabel', background='black', foreground='white', font=('Arial', 12))
style.configure('TButton', background='#4CAF50', foreground='black', font=('Arial', 12), padding=10)

# Carregando e exibindo a imagem
imagem = PhotoImage(file="cover.png")
label_imagem = ttk.Label(janela, image=imagem)
label_imagem.pack(pady=20)

texto_orientacao = ttk.Label(janela, text="Fale com a vanessa")
texto_orientacao.pack(pady=10)

botao = ttk.Button(janela, text="Clique Para iniciar uma conversa", command=mainact)
botao.pack(pady=0)

'''entrada_texto = Entry(janela, width=50)
entrada_texto.pack(pady=20)
# Botão para enviar a entrada
botao = Button(janela, text="Enviar", command=)
botao.pack(pady=20)'''

janela.mainloop()
