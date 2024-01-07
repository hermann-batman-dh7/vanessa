from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from main import callmainact

janela = Tk()
janela.configure(bg='black')
janela.title("vanessa")
def on_minimize():
    janela.destroy()

'propriedades da janela'
largura_janela = 300
altura_janela = 300
posicao_x = (janela.winfo_screenwidth() // 2) - (largura_janela // 2)
posicao_y = (janela.winfo_screenheight() // 2) - (altura_janela // 2)
janela.geometry(f"{largura_janela}x{altura_janela}+{posicao_x}+{posicao_y}")
janela.resizable(False, False)
janela.attributes("-topmost", True)
janela.protocol("WM_DELETE_WINDOW", on_minimize)

'estilização e estética'
style = ttk.Style()
style.configure('TLabel', background='black', foreground='white', font=('Arial', 12))
style.configure('TButton', background='#4CAF50', foreground='black', font=('Arial', 12), padding=10)

'Inserção de elementos'
#imagens
avatar = PhotoImage(file="cover.png")
label_avatar = ttk.Label(janela, image=avatar)
label_avatar.pack(pady=10)

micro = Image.open("miq.png")
micro = micro.resize((50, 50))
micro_tk = ImageTk.PhotoImage(micro)
label_micro = ttk.Label(janela, image=micro_tk)
label_micro.place(x=45, y=200)
label_micro.bind("<Button-1>", callmainact)

janela.mainloop()
