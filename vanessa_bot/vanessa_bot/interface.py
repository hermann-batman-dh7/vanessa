from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from main import callmainact  # Certifique-se de que a função callmainact esteja definida em main.py

janela = Tk()
janela.configure(bg='black')
janela.title("vanessa")
def on_minimize():
    janela.destroy()

largura_janela = 300
altura_janela = 300
posicao_x = (janela.winfo_screenwidth() // 2) - (largura_janela // 2)
posicao_y = (janela.winfo_screenheight() // 2) - (altura_janela // 2)
janela.geometry(f"{largura_janela}x{altura_janela}+{posicao_x}+{posicao_y}")
janela.resizable(False, False)
janela.attributes("-topmost", True)
janela.protocol("WM_DELETE_WINDOW", on_minimize)

style = ttk.Style()
style.configure('TLabel', background='black', foreground='white', font=('Arial', 12))
style.configure('TButton', background='#4CAF50', foreground='black', font=('Arial', 12), padding=10)

imagem1 = PhotoImage(file="cover.png")
label_imagem1 = ttk.Label(janela, image=imagem1)
label_imagem1.pack(pady=10)

imagem2 = Image.open("miq.png")
imagem2 = imagem2.resize((50, 50))
imagem2_tk = ImageTk.PhotoImage(imagem2)
label_imagem2 = ttk.Label(janela, image=imagem2_tk)
label_imagem2.place(x=45, y=200)
label_imagem2.bind("<Button-1>", callmainact)

janela.mainloop()
