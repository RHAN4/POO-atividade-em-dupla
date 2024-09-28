import pytest
from projeto.models.medico import Medico
from projeto.models.endereco import Endereco
from projeto.models.enums.estadoCivil import EstadoCivil
from projeto.models.enums.generos import Generos
from projeto.models.enums.setores import Setores
from projeto.models.enums.unidadeFederativa import UF

@pytest.fixture
def pessoa_valida():
    medico = Medico(5568, "Fernanda", "7198442578", "fernanda@gmail.com", "99999999999999", "222222222222", 
                    "8479", Setores.SAUDE, 10000, 
                    Endereco("Avenida W", "12", "Em frente a Embasa", "41825471", "Salvador", UF.BAHIA), 
                    "17/03/1997", Generos.FEMININO, EstadoCivil.VIUVO, "7444")
    return medico

def test_medico_id_valido(pessoa_valida):
     assert pessoa_valida.id == 5568

def test_medico_nome_valido(pessoa_valida):
     assert pessoa_valida.nome == "Fernanda"

def test_medico_telefone_valido(pessoa_valida):
     assert pessoa_valida.telefone == "7198442578"

def test_medico_email_valido(pessoa_valida):
     assert pessoa_valida.email == "fernanda@gmail.com"

def test_medico_cpf_valido(pessoa_valida):
     assert pessoa_valida.CPF == "99999999999999"

def test_medico_rg_valido(pessoa_valida):
     assert pessoa_valida.RG == "222222222222"

def test_medico_matricula_valido(pessoa_valida):
     assert pessoa_valida.matricula == "8479"

def test_medico_genero_valido(pessoa_valida):
    assert pessoa_valida.genero == Generos.FEMININO

def test_medico_estadoCivil_valido(pessoa_valida):
    assert pessoa_valida.estadoCivil == EstadoCivil.VIUVO

def test_medico_dataNascimento_valido(pessoa_valida):
    assert pessoa_valida.dataNascimento == "17/03/1997"

def test_medico_setor_valido(pessoa_valida):
    assert pessoa_valida.setor == Setores.SAUDE

def test_medico_salario_valido(pessoa_valida):
    assert pessoa_valida.salario == 10000

def test_medico_crm_valido(pessoa_valida):
    assert pessoa_valida.CRM == "7444"

def test_medico_endereco_logradouro_valido(pessoa_valida):
    assert pessoa_valida.endereco.logradouro == "Avenida W"

def test_medico_endereco_numero_valido(pessoa_valida):
    assert pessoa_valida.endereco.numero == "12"

def test_medico_endereco_complemento_valido(pessoa_valida):
    assert pessoa_valida.endereco.complemento == "Em frente a Embasa"

def test_medico_endereco_cep_valido(pessoa_valida):
    assert pessoa_valida.endereco.cep == "41825471"

def test_medico_endereco_cidade_valido(pessoa_valida):
    assert pessoa_valida.endereco.cidade == "Salvador"

def test_medico_endereco_uf_valido(pessoa_valida):
    assert pessoa_valida.endereco.uf == UF.BAHIA

def test_id_valor_negativo(pessoa_valida):
    with pytest.raises(ValueError, match = "Digite apenas números positivos para o ID"):
        Medico(-5568, "Fernanda", "7198442578", "fernanda@gmail.com", "99999999999999", "222222222222", 
                    "8479", Setores.SAUDE, 10000, 
                    Endereco("Avenida W", "12", "Em frente a Embasa", "41825471", "Salvador", UF.BAHIA), 
                    "17/03/1997", Generos.FEMININO, EstadoCivil.VIUVO, "7444")        
        
def test_id_valor_invalido(pessoa_valida):
    with pytest.raises(TypeError, match = "Digite apenas números para o ID"):
        Medico("5568", "Fernanda", "7198442578", "fernanda@gmail.com", "99999999999999", "222222222222", 
                    "8479", Setores.SAUDE, 10000, 
                    Endereco("Avenida W", "12", "Em frente a Embasa", "41825471", "Salvador", UF.BAHIA), 
                    "17/03/1997", Generos.FEMININO, EstadoCivil.VIUVO, "7444")
        
def test_nome_vazio(pessoa_valida):
    with pytest.raises(ValueError, match = "O nome não pode estar em branco"):
        Medico(5568, "", "7198442578", "fernanda@gmail.com", "99999999999999", "14852974", 
                    "8479", Setores.SAUDE, 10000, 
                    Endereco("Avenida W", "12", "Em frente a Embasa", "41825471", "Salvador", UF.BAHIA), 
                    "17/03/1997", Generos.FEMININO, EstadoCivil.VIUVO, "7444")
        
def test_telefone_invalido(pessoa_valida):
   with pytest.raises(TypeError, match= "Digite apenas números."):
        Medico(5568, "Fernanda", 7198442578, "fernanda@gmail.com", "99999999999999", "14852974", 
                    "8479", Setores.SAUDE, 10000, 
                    Endereco("Avenida W", "12", "Em frente a Embasa", "41825471", "Salvador", UF.BAHIA), 
                    "17/03/1997", Generos.FEMININO, EstadoCivil.VIUVO, "7444")

def test_email_invalido(pessoa_valida):
   with pytest.raises(TypeError, match= "Email não pode estar vazio."):
        Medico(5568, "Fernanda", "7198442578", "", "99999999999999", "14852974", 
                    "8479", Setores.SAUDE, 10000, 
                    Endereco("Avenida W", "12", "Em frente a Embasa", "41825471", "Salvador", UF.BAHIA), 
                    "17/03/1997", Generos.FEMININO, EstadoCivil.VIUVO, "7444")
        
def test_rg_invalido(pessoa_valida):
    with pytest.raises(TypeError, match = "RG inválido"):
        Medico(5568, "Fernanda", "7198442578", "fernanda@gmail.com", "99999999999999", "2222222222227", 
                    "8479", Setores.SAUDE, 10000, 
                    Endereco("Avenida W", "12", "Em frente a Embasa", "41825471", "Salvador", UF.BAHIA), 
                    "17/03/1997", Generos.FEMININO, EstadoCivil.VIUVO, "7444")

def test_cpf_invalido(pessoa_valida):
    with pytest.raises(TypeError, match = "CPF inválido"):
        Medico(5568, "Fernanda", "7198442578", "fernanda@gmail.com", "999999999999994", "222222222222", 
                    "8479", Setores.SAUDE, 10000, 
                    Endereco("Avenida W", "12", "Em frente a Embasa", "41825471", "Salvador", UF.BAHIA), 
                    "17/03/1997", Generos.FEMININO, EstadoCivil.VIUVO, "7444")