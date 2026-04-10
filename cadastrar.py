from login import Login
from crud import Livro
import tkinter as tk
from tkinter import messagebox

class Cadastro:
    def __init__(self):
        self.janela = tk.Tk()
        self.janela.title("Gerenciamento de Livros - Cadastro")
        self.janela.geometry("400x300")
        self.janela.resizable(False, False)

        tk.Label(
            self.janela,
            text="Cadastre-se para acessar",
            font=("Arial", 10, "bold")
        ).grid(row=0, column=1, columnspan=2, pady=(50,10), sticky="ew")

        tk.Label(self.janela, text="Usuário:").grid(row=2, column=0, sticky="e", padx=30)
        self.entry_cadastrar_usuario = tk.Entry(self.janela, width=30)
        self.entry_cadastrar_usuario.grid(row=2, column=1)

        tk.Label(self.janela, text="E-mail:").grid(row=3, column=0, sticky="e", padx=30)
        self.entry_cadastrar_email = tk.Entry(self.janela, width=30)
        self.entry_cadastrar_email.grid(row=3, column=1)

        tk.Label(self.janela, text="Senha:").grid(row=4, column=0, sticky="e", padx=30)
        self.entry_cadastrar_senha = tk.Entry(self.janela, width=30, show="*")
        self.entry_cadastrar_senha.grid(row=4, column=1)

        tk.Label(self.janela, text="Confirmar:").grid(row=5, column=0, sticky="e", padx=30)
        self.entry_confirmar_senha = tk.Entry(self.janela, width=30, show="*")
        self.entry_confirmar_senha.grid(row=5, column=1, pady=(0,10))

        tk.Button(self.janela, text="Voltar", width=15, command=self.voltar_login)\
            .grid(row=6, column=1, pady=2)

        tk.Button(self.janela, text="Salvar", width=15, command=self.salvar_dados)\
            .grid(row=7, column=1, pady=2)

    def salvar_dados(self):
        usuario = self.entry_cadastrar_usuario.get().strip()
        email = self.entry_cadastrar_email.get().strip()
        senha = self.entry_cadastrar_senha.get().strip()
        confirmar = self.entry_confirmar_senha.get().strip()

        if not usuario or not email or not senha:
            messagebox.showwarning("Validação", "Preencha todos os campos")
            return

        if senha != confirmar:
            messagebox.showwarning("Validação", "As senhas não conferem")
            return

        if Livro.cadastrar_usuario(usuario, email, senha):
            messagebox.showinfo("OK", "Usuário cadastrado com sucesso!")
            self.voltar_login()
        else:
            messagebox.showerror("Erro", "Usuário ou e-mail já existem")

    def voltar_login(self):
        self.janela.destroy()
        Login().run()

    def run(self):
        self.janela.mainloop()
