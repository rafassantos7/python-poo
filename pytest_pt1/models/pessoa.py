from pytest_pt1.models.enum.sexo import Sexo
class Pessoa:
    def __init__(self,nome:str,idade:int,sexo: Sexo) -> None:
        if idade < 0:
            raise ValueError("Idade não pode ser negativa.")
        self.nome = nome
        self.idade = idade
        self.sexo = sexo