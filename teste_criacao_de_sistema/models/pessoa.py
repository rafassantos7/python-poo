from abc import ABC, abstractmethod

class Pessoa(ABC):
    def __init__(self,nome:str,idade:int,telefone:int,salario:int) -> None:
        self.nome = nome
        self.idade = idade
        self.telefone = telefone
        self.salario = salario

    @abstractmethod
    def salario_total(self) -> float:
        pass
    
    def __str__(self) -> str:
        return  f"Nome: {self.nome}\nIdade: {self.idade}\nTelefone: {self.telefone}\nSalario: {self.salario}"