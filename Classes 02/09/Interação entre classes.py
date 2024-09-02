import os

os.system("clear")

class Endereco:

    def __init__(self,logradouro: str, numero: int) -> None:
        self.logradouro = logradouro
        self.numero = numero

    def exibir_endereco(self) -> str:
        return f"Endereco: {self.logradouro}\nNumero: {self.numero}"

class Aluno:

    def __init__(self, nome: str, idade: int, endereco : Endereco) -> None:
        
        self.nome = nome
        self.idade = idade
        self.endereco = endereco

    def __str__(self) -> str:
        return f"Nome {self.nome}\nIdade:{self.idade}\n{self.endereco.exibir_endereco()}"
        

aluno1 = Aluno("Rafael",22,Endereco("Rua da Alegria",199))

endereco2 = Endereco("Rua da Homossexualidade",24)
aluno2 = Aluno("Luis",18,endereco2)

print(aluno1)
print()
print(aluno2)