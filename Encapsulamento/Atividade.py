from abc import ABC, abstractmethod
import os

os.system("clear || cls")

class Endereco:
    def __init__(self, logradouro : str, numero: str, cidade:str) -> None:
        self.logradouro = logradouro
        self.numero = numero
        self.cidade = cidade

    def __str__(self) -> str:
        return f"{self.logradouro}\nNumero: {self.numero}\nCidade: {self.cidade}"
    

class Funcionario(ABC):
    def __init__(self,nome :str, email: str, salario: float, endereco: Endereco) -> None:
        self.nome = nome
        self.email = email
        self.salario = salario
        self.endereco = endereco

    def __str__(self) -> str:
        return f"\nNome: {self.nome}\nEmail: {self.email}\nSalario: {self.salario}\nEndereço: {self.endereco}"

    @abstractmethod
    def salario_final(self) -> float:
        pass

class Motoboy(Funcionario):
    def __init__(self, nome: str, email: str, salario: float, endereco: Endereco, cnh: str) -> None:
        super().__init__(nome, email, salario, endereco)
        self.cnh = cnh

    def salario_final(self) -> float:
        return f"{super().salario_final()}\nCNH: {self.cnh}"
    
    def __str__(self) -> str:
        return f"{super().__str__()}"

class Gerente(Funcionario):

    def salario_final(self) -> float:
        return super().salario_final()
    

moto1 = Motoboy("Rafael","emailpeba000@gmail.com",3000,Endereco("Rua dos motocas",3,"Salvador"),"784132465")

print(moto1)