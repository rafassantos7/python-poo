from models.pessoa import Pessoa

class Programador(Pessoa):
    def __init__(self, nome: str, idade: int, telefone: int, salario: int, id: int) -> None:
        super().__init__(nome, idade, telefone, salario)
        self.id = id

    def salario_total(self) -> float:
        BONIFICACAO = 0.5
        salario_final += self.salario * BONIFICACAO
        return salario_final
        
    def __str__(self) -> str:
        return f"{super().__str__()}\nId : {self.id}"