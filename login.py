from crud import Livro
import tkinter as tk
from tkinter import messagebox

class Login:
    def __init__(self):
        self.janela = tk.Tk()
        self.janela.title("Gerenciamento de Livros - Login")
        self.janela.geometry("400x300")
        self.janela.resizable(False, False)

        tk.Label(self.janela,text="Fazer Login",font=("Arial", 10, "bold")).grid(row=0, column=1, columnspan=2, pady=(50,10), sticky="ew")

        tk.Label(self.janela, text="Usuário:").grid(row=2, column=0, sticky="e", padx=30, pady=2)
        self.entry_usuario = tk.Entry(self.janela, width=30)
        self.entry_usuario.grid(row=2, column=1, pady=2)

        tk.Label(self.janela, text="Senha:").grid(row=3, column=0, sticky="e", padx=30, pady=2)
        self.entry_senha = tk.Entry(self.janela, width=30, show="*")
        self.entry_senha.grid(row=3, column=1, pady=(2,10))

        tk.Button(self.janela,text="Fazer Login",width=15,command=self.fazer_login).grid(row=4, column=1, pady=2)

        tk.Button(self.janela,text="Fazer Cadastro",width=15,command=self.fazer_cadastro).grid(row=5, column=1, pady=2)

    def fazer_login(self):
        usuario = self.entry_usuario.get().strip()
        senha = self.entry_senha.get().strip()

        if not usuario:
            messagebox.showwarning("Validação", "Digite o nome do usuário")
            return
        if not senha:
            messagebox.showwarning("Validação", "Digite a senha")
            return

        if Livro.login_usuario(usuario, senha):
            messagebox.showinfo("OK", "Login realizado com sucesso!")
            self.janela.destroy()

            from gui import App
            App().run()
        else:
            messagebox.showerror("Erro", "Usuário ou senha inválidos")

    def fazer_cadastro(self):
        self.janela.destroy()
        from cadastrar import Cadastro
        Cadastro().run()

    def run(self):
        self.janela.mainloop()
