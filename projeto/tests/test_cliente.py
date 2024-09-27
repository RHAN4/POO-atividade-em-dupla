import pytest
from projeto.models.endereco import Endereco
from projeto.models.enums.unidadeFederativa import UF
from projeto.models.cliente import Cliente
from projeto.models.enums.generos import Generos
from projeto.models.enums.estadoCivil import EstadoCivil

@pytest.fixture
def pessoa_valida():
    cliente = Cliente(2658, "Felipe", "7198755214", "felipe@gmail.com", 
                      Endereco("Terreno K", "85", "Frente a praça", "41874-258", "Salvador", UF.BAHIA), "11/02/1998", 
                      Generos.MASCULINO, EstadoCivil.DIVORCIADO, "715565656665656")
    return cliente

def test_validar_id_cliente(pessoa_valida):
     assert pessoa_valida.id == 2658

def test_validar_nome_cliente(pessoa_valida):
     assert pessoa_valida.nome == "Felipe"

def test_validar_telefone_cliente(pessoa_valida):
    assert pessoa_valida.telefone == "7198755214"

def test_validar_email_cliente(pessoa_valida):
    assert pessoa_valida.email == "felipe@gmail.com"

def test_validar_genero_cliente(pessoa_valida):
    assert pessoa_valida.genero == Generos.MASCULINO

def test_validar_estado_civil_cliente(pessoa_valida):
    assert pessoa_valida.estadoCivil == EstadoCivil.DIVORCIADO

def test_validar_data_nascimento_cliente(pessoa_valida):
    assert pessoa_valida.dataNascimento == "11/02/1998"

def test_validar_protocolo_atendimento_cliente(pessoa_valida):
    assert pessoa_valida.protocoloAtendimento == "715565656665656"

def test_validar_endereco_logradouro_cliente(pessoa_valida):
    assert pessoa_valida.endereco.logradouro == "Terreno K"

def test_validar_endereco_numero_cliente(pessoa_valida):
    assert pessoa_valida.endereco.numero == "85"

def test_validar_endereco_complemento_cliente(pessoa_valida):
    assert pessoa_valida.endereco.complemento == "Frente a praça"

def test_validar_endereco_cep_cliente(pessoa_valida):
    assert pessoa_valida.endereco.cep == "41874-258"

def test_validar_endereco_cidade_cliente(pessoa_valida):
    assert pessoa_valida.endereco.cidade == "Salvador"

def test_validar_endereco_uf_cliente(pessoa_valida):
    assert pessoa_valida.endereco.uf == UF.BAHIA

def test_id_valor_negativo(pessoa_valida):
    with pytest.raises(ValueError, match = "Digite apenas números positivos para o ID"):
        Cliente(-2658, "Felipe", "7198755214", "felipe@gmail.com", 
                      Endereco("Terreno K", "85", "Frente a praça", "41874-258", "Salvador", UF.BAHIA), "11/02/1998", 
                      Generos.MASCULINO, EstadoCivil.DIVORCIADO, "715565656665656")
        
def test_id_valor_invalido(pessoa_valida):
    with pytest.raises(TypeError, match = "Digite apenas números para o ID"):
        Cliente("2658", "Felipe", "7198755214", "felipe@gmail.com", 
                      Endereco("Terreno K", "85", "Frente a praça", "41874-258", "Salvador", UF.BAHIA), "11/02/1998", 
                      Generos.MASCULINO, EstadoCivil.DIVORCIADO, "715565656665656")
        
def test_nome_vazio(pessoa_valida):
    with pytest.raises(ValueError, match = "O nome não pode estar em branco"):
        Cliente(2658, "", "7198755214", "felipe@gmail.com", 
                      Endereco("Terreno K", "85", "Frente a praça", "41874-258", "Salvador", UF.BAHIA), "11/02/1998", 
                      Generos.MASCULINO, EstadoCivil.DIVORCIADO, "715565656665656")
        
def test_telefone_invalido(pessoa_valida):
   with pytest.raises(TypeError, match= "Digite apenas números."):
        Cliente(2658, "Felipe", 7198755214, "felipe@gmail.com", 
                      Endereco("Terreno K", "85", "Frente a praça", "41874-258", "Salvador", UF.BAHIA), "11/02/1998", 
                      Generos.MASCULINO, EstadoCivil.DIVORCIADO, "715565656665656")
        
def test_email_invalido(pessoa_valida):
   with pytest.raises(TypeError, match= "Email não pode estar vazio."):
        Cliente(2658, "Felipe", "7198755214", "", 
                      Endereco("Terreno K", "85", "Frente a praça", "41874-258", "Salvador", UF.BAHIA), "11/02/1998", 
                      Generos.MASCULINO, EstadoCivil.DIVORCIADO, "715565656665656")