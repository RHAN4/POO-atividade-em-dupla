import pytest
from projeto.models.endereco import Endereco
from projeto.models.enums.unidadeFederativa import UF
from projeto.models.pessoaFisica import PessoaFisica 
from projeto.models.enums.generos import Generos
from projeto.models.enums.estadoCivil import EstadoCivil

@pytest.fixture
def pessoa_valida():
    pessoaFisica = PessoaFisica("4545", "João", "7198854726", "joao@gmail.com", 
                                Endereco("Rua F", "41", "Em frente a loja", "74858-100", "Salvador", UF.BAHIA), "19/12/2000", 
                                Generos.MASCULINO, EstadoCivil.CASADO)
    return pessoaFisica

def test_pessoaJuridica_id_valido(pessoa_valida):
     assert pessoa_valida.id == "4545"

def test_pessoaJuridica_nome_valido(pessoa_valida):
     assert pessoa_valida.nome == "João"
