from pytest_pt1.models.enum.sexo import Sexo
class Pessoa:
    def __init__(self,nome:str,idade:int,sexo: Sexo) -> None:
        self.nome = nome
        self.idade = self._verificar_idade(idade)
        self.sexo = sexo


    def _verificar_idade(self,idade):
        if not isinstance (idade, int):
            raise TypeError("A idade deve contar apenas números.")
        if idade < 0:
            raise ValueError("Idade não pode ser negativa.")
        return idade
