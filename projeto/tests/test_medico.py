import pytest
from projeto.models.medico import Medico
# from projeto.models.endereco import Endereco
from projeto.models.enums.setores import Setores

@pytest.fixture
def medico_valido():
    medico = Medico("01496514798", "14589471-74", "7485", setor.SAUDE, "10000")
    return medico

def test_medico_CPF_valido(medico_valido):
    assert medico_valido.CPF == "01496514798"

def test_medico_RG_valido(medico_valido):
    assert medico_valido.RG == "14589471-74"