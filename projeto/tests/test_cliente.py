import pytest
from projeto.models.endereco import Endereco
from projeto.models.enums.unidadeFederativa import UF
from projeto.models.cliente import Cliente
from projeto.models.enums.generos import Generos
from projeto.models.enums.estadoCivil import EstadoCivil

@pytest.fixture
def pessoa_valida():
    cliente = Cliente("2658", "Felipe", "7198755214", "felipe@gmail.com", 
                      Endereco("Terreno K", "85", "Frente a praça", "41874-258", "Salvador", UF.BAHIA), "11/02/1998", 
                      Generos.MASCULINO, EstadoCivil.DIVORCIADO, "715565656665656")
    return cliente

def test_cliente_id_valido(pessoa_valida):
     assert pessoa_valida.id == "2658"

def test_cliente_nome_valido(pessoa_valida):
     assert pessoa_valida.nome == "Felipe"
