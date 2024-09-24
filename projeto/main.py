import os
from .modelos.pessoa import Pessoa
from .modelos.profissao import Profissao

pessoa1 = Pessoa("malu", 19, Profissao.PROFESSOR)

os.system("clear||cls")
print(pessoa1)