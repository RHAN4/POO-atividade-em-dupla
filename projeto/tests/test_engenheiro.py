import pytest
from projeto.models import engenheiro
from projeto.models.engenheiro import Engenheiro
from projeto.models.endereco import Endereco
from projeto.models.enums.estadoCivil import EstadoCivil
from projeto.models.enums.generos import Generos
from projeto.models.enums.setores import Setores
from projeto.models.enums.unidadeFederativa import UF

@pytest.fixture
def pessoa_valida():
    engenheiro = Engenheiro("1111", "Mateus", "7198442578", "mateus@gmail.com", "12574896802", "14852974", 
                    "8479", Setores.ENGENHARIA, "10000", 
                    Endereco("Avenida W", "12", "Em frente a Embasa", "41825471", "Salvador", UF.BAHIA), 
                    "17/03/1997", Generos.MASCULINO, EstadoCivil.SEPARADO, "7444")
    return engenheiro

def test_engenheiro_id_valido(pessoa_valida):
     assert pessoa_valida.id == "1111"

def test_engenheiro_nome_valido(pessoa_valida):
     assert pessoa_valida.nome == "Mateus"