import pytest
from projeto.models.endereco import Endereco
from projeto.models.enums.unidadeFederativa import UF
from projeto.models.fornecedor import Produto
from projeto.models.pessoaJuridica import PessoaJuridica
from projeto.models.prestacaoServico import PrestacaoServico

@pytest.fixture
def pessoa_valida():
    pessoaJuridica = PessoaJuridica("7841", "Marta", "7188445967", "marta@gmail.com", 
                                    Endereco("Avenida 5", "74", "Ao lado da tenda", "45782-147", "Salvador", UF.BAHIA), 
                                    "748555", "Tudo", 
                                    PrestacaoServico("14-03-2001", "15-10-2007"), Produto("Sim"))
    return pessoaJuridica

def test_pessoaJuridica_id_valido(pessoa_valida):
     assert pessoa_valida.id == "7841"

def test_pessoaJuridica_nome_valido(pessoa_valida):
     assert pessoa_valida.nome == "Marta"
