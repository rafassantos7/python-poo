from pytest_pt1.models.enum.sexo import Sexo
class Pessoa:
    def __init__(self,nome:str,idade:int,sexo: Sexo) -> None:
        self.nome = nome
        self.idade = idade
        self.sexo = sexo