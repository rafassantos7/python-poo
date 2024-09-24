from ..modelos.profissao import Profissao

class Pessoa:
    def __init__(self,nome: str, idade: int, profissao: Profissao) -> None:
        self.nome = nome
        self.idade = idade
        self.profissao = profissao

    def __str__(self) -> str:
        return f"Nome: {self.nome}\nIdade: {self.idade}\nProfissao: {self.profissao.nome}"