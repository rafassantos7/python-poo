from enum import Enum

class Profissao(Enum):
    DENTISTA = ("Dentista")
    ENFERMEIRO = ("Enfermeiro")
    PROFESSOR = ("Professor")

    def __init__(self,nome: str) -> None:
        self.nome = nome