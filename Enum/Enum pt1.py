from enum import Enum

class Sexo(Enum):
    #Definindo valores do Enum
    MASCULINO = "Masculino"
    FEMININO = "Feminino"

class Pessoa:
    def __init__(self,nome:str,idade:int,sexo: Sexo) -> None:
        """Construtor."""
        self.nome = nome
        self.idade = idade
        self.sexo = sexo

    def __str__(self) -> str:
        return f"Nome: {self.nome}\nIdade: {self.idade}\nSexo: {self.sexo.value}"
    
pessoa1 = Pessoa("Rafael", 23, Sexo.MASCULINO)

print(pessoa1)