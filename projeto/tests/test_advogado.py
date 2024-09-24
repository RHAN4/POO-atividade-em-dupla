import pytest
from projeto.models.advogado import Advogado
from projeto.models.endereco import Endereco
from projeto.models.enums.estadoCivil import EstadoCivil
from projeto.models.enums.generos import Generos
from projeto.models.enums.setores import Setores
from projeto.models.enums.unidadeFederativa import UF

@pytest.fixture
def pessoa_valida():
    advogado = Advogado("9999", "Ariel", "7198442578", "ariel@gmail.com", "12574896802", "14852974", 
                    "8479", Setores.JURIDICO, "10000", 
                    Endereco("Avenida W", "12", "Em frente a Embasa", "41825471", "Salvador", UF.BAHIA), 
                    "17/03/1997", Generos.FEMININO, EstadoCivil.SEPARADO, "7444")
    return advogado

def test_advogado_id_valido(pessoa_valida):
     assert pessoa_valida.id == "9999"

def test_advogado_nome_valido(pessoa_valida):
     assert pessoa_valida.nome == "Ariel"