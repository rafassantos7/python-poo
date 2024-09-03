from abc import ABC, abstractmethod
import os

os.system("clear")

class Endereco():
    def __init__(self, logradouro: str, numero: str, complemento: str, cep: str, cidade: str) -> None:
        self.logradouro = logradouro
        self.numero = numero
        self.complemento = complemento
        self.cep = cep
        self.cidade = cidade

    def __str__(self) -> str:
        return f"\n\n{self.logradouro}\nNumero: {self.numero}\nComplemento: {self.complemento}\nCep: {self.cep}\nCidade: {self.cidade}"
        

        
class Funcionario(ABC):
    def __init__(self,nome :str, tel: str, email: str, endereco: Endereco) -> None:
        self.nome = nome
        self.tel = tel
        self.email = email
        self.endereco = endereco


    @abstractmethod
    def salario_final() -> float:
        pass

    def __str__(self) -> str:
        return f"Nome : {self.nome}\nTel: {self.tel}\nEmail: {self.email}\nEndereço: {self.endereco}"

class Engenheiro(Funcionario):
    def __init__(self, nome: str, tel: str, email: str, endereco: Endereco, crea: str) -> None:
        super().__init__(nome, tel, email, endereco)
        self.crea = crea

    def salario_final() -> float:
        pass

    def __str__(self) -> str:
        return f"{super().__str__()}\nCrea: {self.crea}"


class Medico(Funcionario):
    def __init__(self, nome: str, tel: str, email: str, endereco: Endereco, crm: str) -> None:
        super().__init__(nome, tel, email, endereco)
        self.crm = crm

    def salario_final() -> float:
        pass

    def __str__(self) -> str:
        return f"{super().__str__()}"

eng1 = Engenheiro("Rafael","40028922","seila231@gmail.com",Endereco("Rua dos pulinhos","144","Proximo a rua dos capengas","2036547","Salvador"),"n sei o que é crea")

print(eng1)