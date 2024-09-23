import pytest
from ..models.pessoa import Pessoa #Caminho Relativo   
from pytest_pt1.models.enum.sexo import Sexo #Caminho Absoluto

@pytest.fixture
def criar_pessoa():
   # pessoa_1 = Pessoa("Rafael",23,Sexo.MASCULINO) 
    return Pessoa("Rafael",23,Sexo.MASCULINO.nome)

def test_nome(criar_pessoa):
    assert criar_pessoa.nome == "Rafael"

def test_idade(criar_pessoa):
    assert criar_pessoa.idade == 23

def test_pessoa_alterar_nome_valido(criar_pessoa):
    criar_pessoa.nome = "Pedro"
    assert criar_pessoa.nome == "Pedro"

def test_pessoa_idade_negativa_retorna_mensagem_excessao():
    with pytest.raises(ValueError, match = "Idade não pode ser negativa."):
        Pessoa("Rafael",-1,Sexo.MASCULINO.nome)

def test_pessoa_idade_tipo_invalido_retorna_mensagem_excessao():
     with pytest.raises(TypeError, match = "A idade deve contar apenas números."):
         Pessoa("Rafael","216",Sexo.MASCULINO.nome)