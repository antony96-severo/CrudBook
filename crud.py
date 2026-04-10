import sqlite3
import hashlib

class Livro:
    def __init__(self, titulo="", autor="", ano=0, isbn=""):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano
        self.isbn = isbn

    @staticmethod
    def criar_banco():
        conexao = sqlite3.connect("biblioteca.db")
        cursor = conexao.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS livros (
                id_livro INTEGER PRIMARY KEY AUTOINCREMENT,
                titulo TEXT NOT NULL,
                autor TEXT NOT NULL,
                ano INTEGER,
                isbn TEXT NOT NULL
            )
        """)

        conexao.commit()
        conexao.close()

    @staticmethod
    def criar_usuario():
        conexao = sqlite3.connect("biblioteca.db")
        cursor = conexao.cursor()

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS usuarios (
            id_usuario INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL UNIQUE,
            email TEXT NOT NULL UNIQUE,
            senha_hash TEXT NOT NULL
            )
        """)

        conexao.commit()
        conexao.close()

    def inserir_livro(self):
        conexao = sqlite3.connect("biblioteca.db")
        cursor = conexao.cursor()

        sql = """
        INSERT INTO livros (titulo, autor, ano, isbn)
        VALUES (?, ?, ?, ?)
        """
        cursor.execute(sql, (self.titulo, self.autor, self.ano, self.isbn))

        conexao.commit()
        conexao.close()

    
    def consultar_livros(self):
        conexao = sqlite3.connect("biblioteca.db")
        cursor = conexao.cursor()

        sql = "SELECT * FROM livros ORDER BY titulo ASC"
        cursor.execute(sql)
        livros = cursor.fetchall()

        conexao.close()
        return livros

    def consultar_por_titulo(self, titulo):
        conexao = sqlite3.connect("biblioteca.db")
        cursor = conexao.cursor()

        sql = """
        SELECT * FROM livros
        WHERE titulo LIKE ? COLLATE NOCASE
        ORDER BY titulo ASC
        """
        cursor.execute(sql, (f"%{titulo}%",))
        livros = cursor.fetchall()

        conexao.close()
        return livros

    def atualizar_livro(self, id_livro, titulo, autor, ano, isbn):
        conexao = sqlite3.connect("biblioteca.db")
        cursor = conexao.cursor()

        sql = """
        UPDATE livros
        SET titulo = ?, autor = ?, ano = ?, isbn = ?
        WHERE id_livro = ?
        """
        cursor.execute(sql, (titulo, autor, ano, isbn, id_livro))
        conexao.commit()

        linhas = cursor.rowcount
        conexao.close()
        return linhas > 0

    def deletar_livro(self, id_livro):
        conexao = sqlite3.connect("biblioteca.db")
        cursor = conexao.cursor()

        sql = "DELETE FROM livros WHERE id_livro = ?"
        cursor.execute(sql, (id_livro,))

        conexao.commit()
        linhas = cursor.rowcount
        conexao.close()
        return linhas > 0
    
    @staticmethod
    def gerar_senha_hash(senha):
        return hashlib.sha256(senha.encode("utf-8")).hexdigest()
    
    @staticmethod
    def cadastrar_usuario(username, email, senha):
        conexao = sqlite3.connect("biblioteca.db")
        cursor = conexao.cursor()

        senha_hash = Livro.gerar_senha_hash(senha)

        try:
            cursor.execute(
                """
                INSERT INTO usuarios (username, email, senha_hash)
                VALUES (?, ?, ?)""",
                (username, email, senha_hash)
            )
            conexao.commit()
            return True
        except sqlite3.IntegrityError:
            return False
        finally:
            conexao.close()

    @staticmethod
    def login_usuario(username, senha):
        conexao = sqlite3.connect("biblioteca.db")
        cursor = conexao.cursor()

        senha_hash = Livro.gerar_senha_hash(senha)

        cursor.execute(
            """
            SELECT id_usuario FROM usuarios
            WHERE username = ? AND senha_hash = ?
            """,
            (username, senha_hash),
        )
        usuario = cursor.fetchone()
        conexao.close()
        return usuario is not None
    
