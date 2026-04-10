from crud import Livro
import tkinter as tk
from tkinter import messagebox

class App:
    def __init__(self):
        Livro.criar_banco()

        self.janela = tk.Tk()
        self.janela.title("Gerenciamento de Livros")
        self.janela.geometry("650x700")
        self.janela.resizable(False, False)

        tk.Label(self.janela, text="ADICIONAR LIVROS", font=("Arial", 10, "bold"),
        bd=2, relief="solid").grid(row=0, column=1, columnspan=4, pady=15, sticky="ew")

        tk.Label(self.janela, text="Título:").grid(row=1, column=0, sticky="e", padx=20, pady=10)
        self.entry_titulo_add = tk.Entry(self.janela, width=30)
        self.entry_titulo_add.grid(row=1, column=1, padx=8, pady=8)

        tk.Label(self.janela, text="Ano:").grid(row=1, column=2, sticky="e", padx=20, pady=10)
        self.entry_ano_add = tk.Entry(self.janela, width=30)
        self.entry_ano_add.grid(row=1, column=3, padx=8, pady=8)

        tk.Label(self.janela, text="Autor:").grid(row=2, column=0, sticky="e", padx=20, pady=10)
        self.entry_autor_add = tk.Entry(self.janela, width=30)
        self.entry_autor_add.grid(row=2, column=1, padx=8, pady=8)

        tk.Label(self.janela, text="ISBN:").grid(row=2, column=2, sticky="e", padx=20, pady=10)
        self.entry_isbn_add = tk.Entry(self.janela, width=30)
        self.entry_isbn_add.grid(row=2, column=3, padx=8, pady=8)

        tk.Button(self.janela, text="Adicionar Livro", width=20,
        command=self.adicionar_livro).grid(row=3, column=3, pady=10)

        tk.Label(self.janela, text="CONSULTAR LIVROS", font=("Arial", 10, "bold"),
        bd=2, relief="solid").grid(row=4, column=1, columnspan=4, pady=15, sticky="ew")

        tk.Label(self.janela, text="Título:").grid(row=5, column=0, sticky="e", padx=30, pady=10)
        self.entry_titulo_consulta = tk.Entry(self.janela, width=30)
        self.entry_titulo_consulta.grid(row=5, column=1, padx=8, pady=8)

        tk.Button(self.janela, text="Consultar pelo título", width=20,
        command=self.consultar_titulo).grid(row=5, column=3, pady=5)

        tk.Button(self.janela, text="Consultar livros", width=20,
        command=self.consultar_livro).grid(row=6, column=3, pady=5)

        tk.Label(self.janela, text="ATUALIZAR LIVROS", font=("Arial", 10, "bold"),
        bd=2, relief="solid").grid(row=7, column=1, columnspan=4, pady=15, sticky="ew")

        tk.Label(self.janela, text="ID:").grid(row=8, column=0, sticky="e", padx=20, pady=10)
        self.entry_id_update = tk.Entry(self.janela, width=30)
        self.entry_id_update.grid(row=8, column=1, padx=8, pady=8)

        tk.Label(self.janela, text="Autor:").grid(row=8, column=2, sticky="e", padx=20, pady=10)
        self.entry_autor_update = tk.Entry(self.janela, width=30)
        self.entry_autor_update.grid(row=8, column=3, padx=8, pady=8)

        tk.Label(self.janela, text="Título:").grid(row=9, column=0, sticky="e", padx=20, pady=10)
        self.entry_titulo_update = tk.Entry(self.janela, width=30)
        self.entry_titulo_update.grid(row=9, column=1, padx=8, pady=8)

        tk.Label(self.janela, text="ISBN:").grid(row=9, column=2, sticky="e", padx=20, pady=10)
        self.entry_isbn_update = tk.Entry(self.janela, width=30)
        self.entry_isbn_update.grid(row=9, column=3, padx=8, pady=8)

        tk.Label(self.janela, text="Ano:").grid(row=10, column=0, sticky="e", padx=20, pady=10)
        self.entry_ano_update = tk.Entry(self.janela, width=30)
        self.entry_ano_update.grid(row=10, column=1, padx=8, pady=8)

        tk.Button(self.janela, text="Atualizar", width=20,
        command=self.atualizar).grid(row=10, column=3, pady=10)

        tk.Label(self.janela, text="EXCLUIR LIVROS", font=("Arial", 10, "bold"),
        bd=2, relief="solid").grid(row=11, column=1, columnspan=4, pady=15, sticky="ew")

        tk.Label(self.janela, text="ID:").grid(row=12, column=0, sticky="e", padx=20, pady=10)
        self.entry_id_excluir = tk.Entry(self.janela, width=30)
        self.entry_id_excluir.grid(row=12, column=1, padx=8, pady=8)

        tk.Button(self.janela, text="Excluir", width=20,
        command=self.excluir).grid(row=12, column=3, pady=10)

        tk.Button(self.janela, text="Limpar campos", width=20,
        command=self.limpar_janelas).grid(row=13, column=3, pady=10)

        tk.Button(self.janela, text="Sair", width=20,
        command=self.fechar_sistema).grid(row=14, column=3, pady=10)

    def pegar_titulo(self, entry):
        return entry.get().strip()

    def pegar_autor(self, entry):
        return entry.get().strip()

    def pegar_isbn(self, entry):
        return entry.get().strip()

    def pegar_ano(self, entry):
        try:
            return int(entry.get().strip())
        except ValueError:
            return None

    def pegar_id(self, entry):
        try:
            return int(entry.get().strip())
        except ValueError:
            return None

    def adicionar_livro(self):
        titulo = self.pegar_titulo(self.entry_titulo_add)
        autor = self.pegar_autor(self.entry_autor_add)
        isbn = self.pegar_isbn(self.entry_isbn_add)
        ano = self.pegar_ano(self.entry_ano_add)

        if not titulo:
            messagebox.showwarning("Validação", "Digite o titulo do livro.")
            return
        if not autor:
            messagebox.showwarning("Validação", "Digite o autor do livro.")
            return
        if not isbn:
            messagebox.showwarning("Validação", "Digite o ISBN do livro.")
            return
        if ano is None:
            messagebox.showwarning("Validação", "Ano precisa ser um número.")
            return

        try:
            Livro(titulo, autor, ano, isbn).inserir_livro()
            messagebox.showinfo("OK", f"Livro '{titulo}' adicionado!")
        except Exception as e:
            messagebox.showerror("Erro", str(e))

    def atualizar(self):
        id_livro = self.pegar_id(self.entry_id_update)
        titulo = self.pegar_titulo(self.entry_titulo_update)
        autor = self.pegar_autor(self.entry_autor_update)
        isbn = self.pegar_isbn(self.entry_isbn_update)
        ano = self.pegar_ano(self.entry_ano_update)

        if id_livro is None:
            messagebox.showwarning("Validação", "ID inválido.")
            return
        if not titulo:
            messagebox.showwarning("Validação", "Digite o titulo do livro.")
            return
        if not autor:
            messagebox.showwarning("Validação", "Digite o autor do livro.")
            return
        if not isbn:
            messagebox.showwarning("Validação", "Digite o ISBN do livro.")
            return
        if ano is None:
            messagebox.showwarning("Validação", "Ano precisa ser um número.")
            return

        try:
            atualizado = Livro().atualizar_livro(id_livro, titulo, autor, ano, isbn)
            if atualizado:
                messagebox.showinfo("OK", f"Livro '{titulo}' atualizado!")
            else:
                messagebox.showwarning("Aviso", "ID não encontrado. Nenhum livro foi atualizado.")
        except Exception as e:
            messagebox.showerror("Erro", str(e))

    def consultar_livro(self):
        try:
            livros = Livro().consultar_livros()

            if not livros:
                messagebox.showinfo("Consulta", "Nenhum livro cadastrado.")
                return

            resultado = ""
            for livro in livros:
                resultado += (
                    f"ID: {livro[0]}\n"
                    f"Título: {livro[1]}\n"
                    f"Autor: {livro[2]}\n"
                    f"Ano: {livro[3]}\n"
                    f"ISBN: {livro[4]}\n"
                    "-------------------------\n"
                )

            messagebox.showinfo("Lista de Livros", resultado)

        except Exception as e:
            messagebox.showerror("Erro", str(e))

    def consultar_titulo(self):
        titulo = self.entry_titulo_consulta.get().strip()

        if not titulo:
            messagebox.showwarning("Validação", "Digite um título para consultar.")
            return

        try:
            livros = Livro().consultar_por_titulo(titulo)

            if not livros:
                messagebox.showinfo("Consulta", "Nenhum livro encontrado.")
                return

            resultado = ""
            for livro in livros:
                resultado += (
                    f"ID: {livro[0]}\n"
                    f"Título: {livro[1]}\n"
                    f"Autor: {livro[2]}\n"
                    f"Ano: {livro[3]}\n"
                    f"ISBN: {livro[4]}\n"
                    "-------------------------\n"
                )

            messagebox.showinfo("Resultado da Consulta", resultado)

        except Exception as e:
            messagebox.showerror("Erro", str(e))

    def excluir(self):
        id_livro = self.pegar_id(self.entry_id_excluir)

        if id_livro is None:
            messagebox.showwarning("Validação", "ID inválido.")
            return

        try:
            deletado = Livro().deletar_livro(id_livro)

            if deletado:
                messagebox.showinfo("OK", "Livro deletado com sucesso!")
            else:
                messagebox.showwarning("Aviso", "ID não encontrado. Nenhum livro foi deletado.")

        except Exception as e:
            messagebox.showerror("Erro", str(e))

    def limpar_janelas(self):
        self.entry_titulo_add.delete(0, tk.END)
        self.entry_ano_add.delete(0, tk.END)
        self.entry_autor_add.delete(0, tk.END)
        self.entry_isbn_add.delete(0, tk.END)

        self.entry_titulo_consulta.delete(0, tk.END)

        self.entry_id_update.delete(0, tk.END)
        self.entry_titulo_update.delete(0, tk.END)
        self.entry_autor_update.delete(0, tk.END)
        self.entry_ano_update.delete(0, tk.END)
        self.entry_isbn_update.delete(0, tk.END)

        self.entry_id_excluir.delete(0, tk.END)

    def fechar_sistema(self):
        self.janela.destroy()
        from login import Login
        Login().run()

    def run(self):
        self.janela.mainloop()

