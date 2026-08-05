import tkinter as tk
from tkinter import ttk

# Janela principal
janela = tk.Tk()
janela.title("Sistema de Cadastro")
janela.geometry("500x350")
janela.resizable(False, False)

# ==========================
# FRAME 1 - LOGIN
# ==========================
frame1 = tk.Frame(janela, bg="white")
frame1.pack(fill="both", expand=True)

# Título
titulo = tk.Label(
    frame1,
    text="TELA DE LOGIN",
    font=("Arial", 18, "bold"),
    bg="white",
    fg="#003366"
)
titulo.pack(pady=20)

# Usuário
lbl_usuario = tk.Label(
    frame1,
    text="Usuário:",
    font=("Arial", 11),
    bg="white"
)
lbl_usuario.pack()

entry_usuario = ttk.Entry(frame1, width=30)
entry_usuario.pack(pady=5)

# Senha
lbl_senha = tk.Label(
    frame1,
    text="Senha:",
    font=("Arial", 11),
    bg="white"
)
lbl_senha.pack()

entry_senha = ttk.Entry(frame1, width=30, show="*")
entry_senha.pack(pady=5)

# Botão Entrar
btn_entrar = ttk.Button(
    frame1,
    text="Entrar"
)
btn_entrar.pack(pady=15)

# Botão Limpar
btn_limpar = ttk.Button(
    frame1,
    text="Limpar"
)
btn_limpar.pack()

# Link Esqueci a senha
lbl_esqueci = tk.Label(
    frame1,
    text="Esqueci minha senha",
    fg="blue",
    cursor="hand2",
    bg="white"
)
lbl_esqueci.pack(pady=15)

janela.mainloop()

