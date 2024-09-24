import pytest
from projeto.models.fornecedor import Fornecedor
from projeto.models.endereco import Endereco
from projeto.models.enums.unidadeFederativa import UF
from projeto.models.prestacaoServico import PrestacaoServico

@pytest.fixture
def produto_valido():
    produto = Fornecedor(5247, "Vidro", "71987874545", "vidro@gmail.com", 
                         Endereco("Rua L", "15", "Setor 8", "4900547", "Salvador", UF.BAHIA), "798889", "63213339", 
                         PrestacaoServico("12/08/2008", "23/09/2023"), "Vidro Um")
    return produto


def test_validar_id_tipo_int(produto_valido):
    with pytest.raises(TypeError, match="Digite somente números inteiros para o ID."):
        Fornecedor("W", "Vidro", "71987874545", "vidro@gmail.com", 
                         Endereco("Rua L", "15", "Setor 8", "4900547", "Salvador", UF.BAHIA), "798889", "63213339", 
                         PrestacaoServico("12/08/2008", "23/09/2023"), "Vidro Um")

def test_validar_id_valor_negativo(produto_valido):
    with pytest.raises(ValueError, match="Digite um número que seja inteiro e positivo para o ID."):
        Fornecedor(-5247, "Vidro", "71987874545", "vidro@gmail.com", 
                         Endereco("Rua L", "15", "Setor 8", "4900547", "Salvador", UF.BAHIA), "798889", "63213339", 
                         PrestacaoServico("12/08/2008", "23/09/2023"), "Vidro Um")
        
def test_validar_id_nome_vazio(produto_valido):
    with pytest.raises(ValueError, match="O nome não pode estar vazio."):
        Fornecedor(5247, "", "71987874545", "vidro@gmail.com", 
                         Endereco("Rua L", "15", "Setor 8", "4900547", "Salvador", UF.BAHIA), "798889", "63213339", 
                         PrestacaoServico("12/08/2008", "23/09/2023"), "Vidro Um")
        
def test_validar_id_fornecedor(produto_valido):
    assert produto_valido.id == 5247

def test_validar_nome_fornecedor(produto_valido):
    assert produto_valido.nome == "Vidro"

def test_validar_telefone_fornecedor(produto_valido):
    assert produto_valido.telefone == "71987874545"

def test_validar_email_fornecedor(produto_valido):
    assert produto_valido.email == "vidro@gmail.com"

def test_validar_cnpj_fornecedor(produto_valido):
    assert produto_valido.cpnj == "798889"

def test_validar_inscricao_estadual_fornecedor(produto_valido):
    assert produto_valido.inscricao_estadual == "63213339"

def test_validar_prestacaoServico_fornecedor(produto_valido):
    assert produto_valido.prestacaoServico == "12/08/2008" and "23/09/2023"

def test_validar_produto_fornecedor(produto_valido):
    assert produto_valido.produto == "Vidro Um"

def test_validar_endereco_logradouro_fornecedor(produto_valido):
    assert produto_valido.endereco.logradouro == "Rua L"

def test_validar_endereco_numero_fornecedor(produto_valido):
    assert produto_valido.endereco.numero == "1331"

def test_validar_endereco_complemento_fornecedor(produto_valido):
    assert produto_valido.endereco.complemento == "Setor 8"

def test_validar_endereco_cep_fornecedor(produto_valido):
    assert produto_valido.endereco.cep == "49000-547"

def test_validar_endereco_cidade_fornecedor(produto_valido):
    assert produto_valido.endereco.cidade == "Salvador"

def test_validar_endereco_uf_fornecedor(produto_valido):
    assert produto_valido.endereco.uf == UF.BAHIA