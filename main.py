from login import Login
from crud import Livro

def main():
    Livro.criar_banco()
    Livro.criar_usuario() 
    Login().run()

if __name__ == "__main__":
    main()