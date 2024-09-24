import pytest

from ..modelos.pessoa import Pessoa
from ..modelos.profissao import Profissao

@pytest.fixture
def criar_pessoa():
    return Pessoa("Rafael",23, Profissao.DENTISTA)

def validar_nome(criar_pessoa):
    assert criar_pessoa.nome == "Rafael"

