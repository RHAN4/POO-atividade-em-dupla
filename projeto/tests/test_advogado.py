import pytest
from projeto.models.advogado import Advogado
from projeto.models.endereco import Endereco
from projeto.models.enums import unidadeFederativa
from projeto.models.enums.estadoCivil import EstadoCivil
from projeto.models.enums.generos import Generos
from projeto.models.enums.setores import Setores
from projeto.models.enums.unidadeFederativa import UF

@pytest.fixture
def pessoa_valida():
    advogado = Advogado(9999, "Ariel", "7198442578", "ariel@gmail.com", "12574896802", "14852974", 
                    "8479", Setores.JURIDICO, 10000, 
                    Endereco("Avenida W", "12", "Em frente a Embasa", "41825471", "Salvador", UF.BAHIA), 
                    "17/03/1997", Generos.FEMININO, EstadoCivil.SEPARADO, "7444")
    return advogado

def test_validar_id_advogado(pessoa_valida):
     assert pessoa_valida.id == 9999

def test_validar_nome_advogado(pessoa_valida):
     assert pessoa_valida.nome == "Ariel"

def test_validar_telefone_advogado(pessoa_valida):
    assert pessoa_valida.telefone == "7198442578"

def test_validar_email_advogado(pessoa_valida):
    assert pessoa_valida.email == "ariel@gmail.com"

def test_validar_genero_advogado(pessoa_valida):
    assert pessoa_valida.genero == Generos.FEMININO

def test_validar_estado_civil_advogado(pessoa_valida):
    assert pessoa_valida.estadoCivil == EstadoCivil.SEPARADO

def test_validar_data_nascimento_advogado(pessoa_valida):
    assert pessoa_valida.dataNascimento == "17/03/1997"

def test_validar_cpf_advogado(pessoa_valida):
    assert pessoa_valida.CPF == "12574896802"

def test_validar_rg_advogado(pessoa_valida):
    assert pessoa_valida.RG == "14852974"

def test_validar_matricula_advogado(pessoa_valida):
    assert pessoa_valida.matricula == "8479"

def test_validar_setor_advogado(pessoa_valida):
    assert pessoa_valida.setor == Setores.JURIDICO

def test_validar_salario_advogado(pessoa_valida):
    assert pessoa_valida.salario == 10000

def test_validar_crea_advogado(pessoa_valida):
    assert pessoa_valida.OAB == "7444"

def test_validar_endereco_logradouro_advogado(pessoa_valida):
    assert pessoa_valida.endereco.logradouro == "Avenida W"

def test_validar_endereco_numero_advogado(pessoa_valida):
    assert pessoa_valida.endereco.numero == "12"

def test_validar_endereco_complemento_advogado(pessoa_valida):
    assert pessoa_valida.endereco.complemento == "Em frente a Embasa"

def test_validar_endereco_cep_advogado(pessoa_valida):
    assert pessoa_valida.endereco.cep == "41825471"

def test_validar_endereco_cidade_advogado(pessoa_valida):
    assert pessoa_valida.endereco.cidade == "Salvador"

def test_validar_endereco_uf_advogado(pessoa_valida):
    assert pessoa_valida.endereco.uf == UF.BAHIA

def test_id_valor_negativo(pessoa_valida):
    with pytest.raises(ValueError, match = "Digite apenas números positivos para o ID"):
        Advogado(-9999, "Ariel", "7198442578", "ariel@gmail.com", "12574896802", "14852974", 
                    "8479", Setores.JURIDICO, 10000, 
                    Endereco("Avenida W", "12", "Em frente a Embasa", "41825471", "Salvador", UF.BAHIA), 
                    "17/03/1997", Generos.FEMININO, EstadoCivil.SEPARADO, "7444")
        
def test_id_valor_invalido(pessoa_valida):
    with pytest.raises(TypeError, match = "Digite apenas números para o ID"):
        Advogado("9999", "Ariel", "7198442578", "ariel@gmail.com", "12574896802", "14852974", 
                    "8479", Setores.JURIDICO, 10000, 
                    Endereco("Avenida W", "12", "Em frente a Embasa", "41825471", "Salvador", UF.BAHIA), 
                    "17/03/1997", Generos.FEMININO, EstadoCivil.SEPARADO, "7444")

def test_nome_vazio(pessoa_valida):
    with pytest.raises(ValueError, match = "O nome não pode estar em branco"):
        Advogado(9999, "", "7198442578", "ariel@gmail.com", "12574896802", "14852974", 
                    "8479", Setores.JURIDICO, 10000, 
                    Endereco("Avenida W", "12", "Em frente a Embasa", "41825471", "Salvador", UF.BAHIA), 
                    "17/03/1997", Generos.FEMININO, EstadoCivil.SEPARADO, "7444")
        
def test_telefone_invalido(pessoa_valida):
   with pytest.raises(TypeError, match= "Digite apenas números."):
        Advogado(9999, "Ariel", 7198442578, "ariel@gmail.com", "12574896802", "14852974", 
                    "8479", Setores.JURIDICO, 10000, 
                    Endereco("Avenida W", "12", "Em frente a Embasa", "41825471", "Salvador", UF.BAHIA), 
                    "17/03/1997", Generos.FEMININO, EstadoCivil.SEPARADO, "7444")

def test_email_invalido(pessoa_valida):
   with pytest.raises(TypeError, match= "Email não pode estar vazio."):
        Advogado(9999, "Ariel", "7198442578", "", "12574896802", "14852974", 
                    "8479", Setores.JURIDICO, 10000, 
                    Endereco("Avenida W", "12", "Em frente a Embasa", "41825471", "Salvador", UF.BAHIA), 
                    "17/03/1997", Generos.FEMININO, EstadoCivil.SEPARADO, "7444")