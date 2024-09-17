import pytest
from ..models.pessoa import Pessoa #Caminho Relativo   
from pytest_pt1.models.enum.sexo import Sexo #Caminho Absoluto

@pytest.fixture
def criar_pessoa():
   # pessoa_1 = Pessoa("Rafael",23,Sexo.MASCULINO) 
    return Pessoa("Rafael",23,Sexo.MASCULINO)

def test_nome(criar_pessoa):
    assert criar_pessoa.nome == "Rafael"

def test_idade(criar_pessoa):
    assert criar_pessoa.idade == 23