import tkinter as tk
# criação da janela principal
janela = tk.Tk()
janela.title("Olá, Tkinter!")
janela.geometry("800x600+600+300")
janela.resizable(True, False)

# Rótulo simples
label = tk.Label(janela, text="Bem vindo ao Tkinter!")
label2= tk.Label(janela, text="Bem vindo Erlania!")
label.pack()
label2.pack()
# inicio do loop principal
janela.mainloop()