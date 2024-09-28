import pytest
from projeto.models.endereco import Endereco
from projeto.models.enums.unidadeFederativa import UF
from projeto.models.prestacaoServico import PrestacaoServico

@pytest.fixture
def pessoa_valida():
    prestador = PrestacaoServico(3333, "AirCon", "71988775522", "aircon@gmail.com", 
                                 Endereco("Avenida J", "44", "Departamento O", "43806741", "Salvador", UF.BAHIA), 
                                 "66666666666666", "8444", "20/01/1999", "30/06/2024")
    return prestador

def test_validar_id(pessoa_valida):
     assert pessoa_valida.id == 3333

def test_validar_nome(pessoa_valida):
     assert pessoa_valida.nome == "AirCon"

def test_validar_telefone(pessoa_valida):
    assert pessoa_valida.telefone == "71988775522"

def test_validar_email(pessoa_valida):
    assert pessoa_valida.email == "aircon@gmail.com"

def test_validar_endereco_logradouro(pessoa_valida):
    assert pessoa_valida.endereco.logradouro == "Avenida J"

def test_validar_endereco_numero(pessoa_valida):
    assert pessoa_valida.endereco.numero == "44"

def test_validar_endereco_complemento(pessoa_valida):
    assert pessoa_valida.endereco.complemento == "Departamento O"

def test_validar_endereco_cep(pessoa_valida):
    assert pessoa_valida.endereco.cep == "43806741"

def test_validar_endereco_cidade(pessoa_valida):
    assert pessoa_valida.endereco.cidade == "Salvador"

def test_validar_endereco_uf(pessoa_valida):
    assert pessoa_valida.endereco.uf == UF.BAHIA

def test_id_valor_negativo(pessoa_valida):
    with pytest.raises(ValueError, match = "Digite apenas números positivos para o ID"):
        PrestacaoServico(-3333, "AirCon", "71988775522", "aircon@gmail.com", 
                                 Endereco("Avenida J", "44", "Departamento O", "43806741", "Salvador", UF.BAHIA), 
                                 "66666666666666", "8444", "20/01/1999", "30/06/2024")
        
def test_id_valor_invalido(pessoa_valida):
    with pytest.raises(TypeError, match = "Digite apenas números para o ID"):
        PrestacaoServico("3333", "AirCon", "71988775522", "aircon@gmail.com", 
                                 Endereco("Avenida J", "44", "Departamento O", "43806741", "Salvador", UF.BAHIA), 
                                 "66666666666666", "8444", "20/01/1999", "30/06/2024")

def test_nome_vazio(pessoa_valida):
    with pytest.raises(ValueError, match = "O nome não pode estar em branco"):
        PrestacaoServico(3333, "", "71988775522", "aircon@gmail.com", 
                                 Endereco("Avenida J", "44", "Departamento O", "43806741", "Salvador", UF.BAHIA), 
                                 "66666666666666", "8444", "20/01/1999", "30/06/2024")
        
def test_telefone_invalido(pessoa_valida):
   with pytest.raises(TypeError, match= "Digite apenas números."):
        PrestacaoServico(3333, "AirCon", 71988775522, "aircon@gmail.com", 
                                 Endereco("Avenida J", "44", "Departamento O", "43806741", "Salvador", UF.BAHIA), 
                                 "66666666666666", "8444", "20/01/1999", "30/06/2024")

def test_email_invalido(pessoa_valida):
   with pytest.raises(TypeError, match= "Email não pode estar vazio."):
        PrestacaoServico(3333, "AirCon", "71988775522", "", 
                                 Endereco("Avenida J", "44", "Departamento O", "43806741", "Salvador", UF.BAHIA), 
                                 "66666666666666", "8444", "20/01/1999", "30/06/2024")
        
def test_CNPJ_invalido(pessoa_valida):
    with pytest.raises(TypeError, match = "CNPJ inválido."):
        PrestacaoServico(3333, "AirCon", "71988775522", "aircon@gmail.com", 
                                 Endereco("Avenida J", "44", "Departamento O", "43806741", "Salvador", UF.BAHIA), 
                                 "666666666666665", "8444", "20/01/1999", "30/06/2024")