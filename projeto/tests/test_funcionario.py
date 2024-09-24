from abc import abstractmethod
import pytest
from projeto.models.endereco import Endereco
from projeto.models.enums.setores import Setores
from projeto.models.enums.unidadeFederativa import UF
from projeto.models.funcionario import Funcionario
from projeto.models.enums.generos import Generos
from projeto.models.enums.estadoCivil import EstadoCivil

@pytest.fixture
def pessoa_valida():
    funcionario = Funcionario("1012", "Cátia", "71988475263", "catia@gmail.com", "14752465810", "1574856814", "8555", 
                              Setores.ENGENHARIA, "70000", Endereco("Rua Y", "55", "Em frente ao bar", 
                                                                    "46852-147", "Salvador", UF.BAHIA), "22/06/1988", 
                                                                    Generos.FEMININO, EstadoCivil.VIUVO)
    return funcionario

def test_funcionario_id_valido(pessoa_valida):
     assert pessoa_valida.id == "1012"

def test_funcionario_nome_valido(pessoa_valida):
     assert pessoa_valida.nome == "Cátia"