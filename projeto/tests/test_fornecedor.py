import pytest
from projeto.models.fornecedor import Fornecedor
from projeto.models.endereco import Endereco
from projeto.models.enums.unidadeFederativa import UF

@pytest.fixture
def produto_valido():
    produto = Fornecedor(5247, "Vidraçaria", "71987874545", "vidracaria@gmail.com", 
                         Endereco("Rua L", "15", "Setor 8", "49005470",
                                   "Salvador", UF.BAHIA), "798889/0001", "13339", 
                         "Vidro blindado")
    return produto

def test_validar_id(produto_valido):
     assert produto_valido.id == 5247

def test_validar_nome(produto_valido):
    assert produto_valido.nome == "Vidraçaria"

def test_validar_telefone(produto_valido):
    assert produto_valido.telefone == "71987874545"

def test_validar_email(produto_valido):
    assert produto_valido.email == "vidracaria@gmail.com"

def test_validar_CNPJ(produto_valido):
    assert produto_valido.CNPJ == "798889/0001"

def test_validar_inscricaoEstadual(produto_valido):
    assert produto_valido.inscricaoEstadual == "13339"

def test_validar_produto(produto_valido):
    assert produto_valido.produto == "Vidro blindado"

def test_validar_logradouro(produto_valido):
    assert produto_valido.endereco.logradouro == "Rua L"

def test_validar_numero(produto_valido):
    assert produto_valido.endereco.numero == "15"

def test_validar_complemento(produto_valido):
    assert produto_valido.endereco.complemento == "Setor 8"

def test_validar_CEP(produto_valido):
    assert produto_valido.endereco.cep == "49005470"

def test_validar_cidade(produto_valido):
    assert produto_valido.endereco.cidade == "Salvador"

def test_validar_uf(produto_valido):
    assert produto_valido.endereco.uf == UF.BAHIA

# def test_validar_id_tipo_int(produto_valido):
#      with pytest.raises(TypeError, match="Digite somente números inteiros para o ID."):
#          Fornecedor("W", "Vidraçaria", "71987874545", "vidracaria@gmail.com", 
#                           Endereco("Rua L", "15", "Setor 8", "49005470", "Salvador", UF.BAHIA), "798889/0001", "13339", 
#                           "Vidro blindado")

# def test_validar_id_valor_negativo(produto_valido):
#      with pytest.raises(ValueError, match="Digite um número que seja inteiro e positivo para o ID."):
#          Fornecedor(-5247, "Vidraçaria", "71987874545", "vidracaria@gmail.com", 
#                           Endereco("Rua L", "15", "Setor 8", "49005470", "Salvador", UF.BAHIA), "798889/0001", "13339", 
#                           "Vidro blindado")
        
# def test_validar_nome_vazio(produto_valido):
#      with pytest.raises(ValueError, match="O nome não pode estar vazio."):
#          Fornecedor(5247, "", "71987874545", "vidracaria@gmail.com", 
#                           Endereco("Rua L", "15", "Setor 8", "49005470", "Salvador", UF.BAHIA), "798889/0001", "13339", 
#                           "Vidro blindado")