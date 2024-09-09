from abc import ABC, abstractmethod
from enum import Enum
import os

class Sexo(Enum):
    MASCULINO = "Masculino"
    FEMININO = "Feminino"

class Setor(Enum):
    FINANCEIRO = "Financeiro"
    RECURSOS_HUMANOS = "Recursos Humanos"
    VENDAS = "Vendas"
    MARKETING = "Marketing"

class Funcionario:
    def __init__(self,id: int, nome: str, idade: int, salario: float, setor: Setor, sexo: Sexo) -> None:
        
        self.id = id
        self.nome = nome
        self.idade = idade
        self.salario = salario
        self.setor = setor
        self.sexo = sexo

    def __str__(self) -> str:
        return f"Id: {self.id}\nNome: {self.nome}\nIdade: {self.idade}\nSalario: {self.salario}\nSetor: {self.setor.value}\nSexo: {self.sexo.value}"


func1 = Funcionario(777,"Rafael",23,4000,Setor.RECURSOS_HUMANOS,Sexo.MASCULINO)

print(func1)
