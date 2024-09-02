import os

os.system("clear")

class Livro:
    def __init__(self,titulo :str, autor: str, numeroPag: int, preco: float) -> None:
        self.titulo = titulo
        self.autor = autor
        self.numeroPag = numeroPag
        self.preco = preco


    def exibir_dados(self) -> str:
        return f"Titulo: {self.titulo}\nAutor: {self.autor}\nNúmero Pag: {self.numeroPag}\nPreço: {self.preco}"

livro = Livro("Breno, o Pequeno","Luis Phelipe",69,24.24)

os.system("clear")
print(livro.exibir_dados())