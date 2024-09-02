from abc import ABC, abstractmethod
import os

os.system("clear")

class Funcionario(ABC):
    #Construtor
    def __init__(self, nome : str, idade: int, salario: float) -> None:
        self.nome = nome
        self.idade = idade
        self.salario = salario

    def calcular_salario(self) -> float:
        pass

    @abstractmethod
    def __str__(self) -> str:
        return f"Nome: {self.nome}\nIdade: {self.idade}\nSalario Base: {self.salario}"

class Gerente(Funcionario):
    def calcular_salario(self) -> float:
        BONIFICACAO = 1.2
        salario_final = self.salario * BONIFICACAO
        return salario_final
    
    def __str__(self) -> str:
        return f"Dados do Gerente:\n{super().__str__()}\nSalario Final: {self.calcular_salario()}\n"

class Motoboy(Funcionario):
    def __init__(self, nome: str, idade: int, salario: float, cnh: str) -> None:
        super().__init__(nome, idade, salario)
        self.cnh = cnh

    def calcular_salario(self) -> float:
        BONIFICACAO = 1.3
        salarioFinal = self.salario * BONIFICACAO
        return salarioFinal

    def __str__(self) -> str:
        return f"Dados do Motoboy:\n{super().__str__()}\nSalario: {self.calcular_salario()}\n"
    
#Instanciar classes.

# funcionario1 = Funcionario("Jose",33,1000)
# print(f"Nome: {funcionario1.nome}")

gerente1 = Gerente("Rafael",23,3000)

print(gerente1)
# print(f"Salario: {gerente1.calcular_salario()}")

motoboy1 = Motoboy("Silvestre",24,4000,"852369741")

print(motoboy1)
# print(f"Salario: {motoboy1.salario}")
