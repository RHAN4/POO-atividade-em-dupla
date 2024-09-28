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
    engenheiro = Engenheiro(1111, "Mateus", "7198442578", "mateus@gmail.com", "88888888888888", "111111111111", 
                    "8479", Setores.ENGENHARIA, 10000, 
                    Endereco("Avenida W", "12", "Em frente a Embasa", "41825471", "Salvador", UF.BAHIA), 
                    "17/03/1997", Generos.MASCULINO, EstadoCivil.SEPARADO, "7444")
    return engenheiro

def test_engenheiro_id_valido(pessoa_valida):
     assert pessoa_valida.id == 1111

def test_engenheiro_nome_valido(pessoa_valida):
     assert pessoa_valida.nome == "Mateus"

def test_engenheiro_telefone_valido(pessoa_valida):
     assert pessoa_valida.telefone == "7198442578"

def test_engenheiro_email_valido(pessoa_valida):
     assert pessoa_valida.email == "mateus@gmail.com"

def test_engenheiro_cpf_valido(pessoa_valida):
     assert pessoa_valida.CPF == "88888888888888"

def test_engenheiro_rg_valido(pessoa_valida):
     assert pessoa_valida.RG == "111111111111"

def test_engenheiro_matricula_valido(pessoa_valida):
     assert pessoa_valida.matricula == "8479"

def test_engenheiro_genero_valido(pessoa_valida):
    assert pessoa_valida.genero == Generos.MASCULINO

def test_engenheiro_estado_civil_valido(pessoa_valida):
    assert pessoa_valida.estadoCivil == EstadoCivil.SEPARADO

def test_engenheiro_dataNascimento_valido(pessoa_valida):
    assert pessoa_valida.dataNascimento == "17/03/1997"

def test_engenheiro_setor_valido(pessoa_valida):
    assert pessoa_valida.setor == Setores.ENGENHARIA

def test_engenheiro_salario_valido(pessoa_valida):
    assert pessoa_valida.salario == 10000

def test_engenheiro_crea_valido(pessoa_valida):
    assert pessoa_valida.CREA == "7444"

def test_engenheiro_endereco_logradouro_valido(pessoa_valida):
    assert pessoa_valida.endereco.logradouro == "Avenida W"

def test_engenheiro_endereco_numero_valido(pessoa_valida):
    assert pessoa_valida.endereco.numero == "12"

def test_engenheiro_endereco_complemento_valido(pessoa_valida):
    assert pessoa_valida.endereco.complemento == "Em frente a Embasa"

def test_engenheiro_endereco_cep_valido(pessoa_valida):
    assert pessoa_valida.endereco.cep == "41825471"

def test_engenheiro_endereco_cidade_valido(pessoa_valida):
    assert pessoa_valida.endereco.cidade == "Salvador"

def test_engenheiro_uf_valido(pessoa_valida):
    assert pessoa_valida.endereco.uf == UF.BAHIA

def test_id_valor_negativo(pessoa_valida):
    with pytest.raises(ValueError, match = "Digite apenas números positivos para o ID"):
        Engenheiro(-1111, "Mateus", "7198442578", "mateus@gmail.com", "88888888888888", "111111111111", 
                    "8479", Setores.ENGENHARIA, 10000, 
                    Endereco("Avenida W", "12", "Em frente a Embasa", "41825471", "Salvador", UF.BAHIA), 
                    "17/03/1997", Generos.MASCULINO, EstadoCivil.SEPARADO, "7444")        
        
def test_id_valor_invalido(pessoa_valida):
    with pytest.raises(TypeError, match = "Digite apenas números para o ID"):
        Engenheiro("1111", "Mateus", "7198442578", "mateus@gmail.com", "88888888888888", "111111111111", 
                    "8479", Setores.ENGENHARIA, 10000, 
                    Endereco("Avenida W", "12", "Em frente a Embasa", "41825471", "Salvador", UF.BAHIA), 
                    "17/03/1997", Generos.MASCULINO, EstadoCivil.SEPARADO, "7444")
        
def test_nome_vazio(pessoa_valida):
    with pytest.raises(ValueError, match = "O nome não pode estar em branco"):
        Engenheiro(1111, "", "7198442578", "mateus@gmail.com", "88888888888888", "111111111111", 
                    "8479", Setores.ENGENHARIA, 10000, 
                    Endereco("Avenida W", "12", "Em frente a Embasa", "41825471", "Salvador", UF.BAHIA), 
                    "17/03/1997", Generos.MASCULINO, EstadoCivil.SEPARADO, "7444")

def test_telefone_invalido(pessoa_valida):
   with pytest.raises(TypeError, match= "Digite apenas números."):
        Engenheiro(1111, "Mateus", 7198442578, "mateus@gmail.com", "88888888888888", "111111111111", 
                    "8479", Setores.ENGENHARIA, 10000, 
                    Endereco("Avenida W", "12", "Em frente a Embasa", "41825471", "Salvador", UF.BAHIA), 
                    "17/03/1997", Generos.MASCULINO, EstadoCivil.SEPARADO, "7444")
        
def test_email_invalido(pessoa_valida):
   with pytest.raises(TypeError, match= "Email não pode estar vazio."):
        Engenheiro(1111, "Mateus", "7198442578", "", "88888888888888", "111111111111", 
                    "8479", Setores.ENGENHARIA, 10000, 
                    Endereco("Avenida W", "12", "Em frente a Embasa", "41825471", "Salvador", UF.BAHIA), 
                    "17/03/1997", Generos.MASCULINO, EstadoCivil.SEPARADO, "7444")

def test_rg_invalido(pessoa_valida):
    with pytest.raises(TypeError, match = "RG inválido"):
        Engenheiro(1111, "Mateus", "7198442578", "mateus@gmail.com", "88888888888888", "1111111111114", 
                    "8479", Setores.ENGENHARIA, 10000, 
                    Endereco("Avenida W", "12", "Em frente a Embasa", "41825471", "Salvador", UF.BAHIA), 
                    "17/03/1997", Generos.MASCULINO, EstadoCivil.SEPARADO, "7444")

def test_cpf_invalido(pessoa_valida):
    with pytest.raises(TypeError, match = "CPF inválido"):
        Engenheiro(1111, "Mateus", "7198442578", "mateus@gmail.com", "888888888888882", "111111111111", 
                    "8479", Setores.ENGENHARIA, 10000, 
                    Endereco("Avenida W", "12", "Em frente a Embasa", "41825471", "Salvador", UF.BAHIA), 
                    "17/03/1997", Generos.MASCULINO, EstadoCivil.SEPARADO, "7444")