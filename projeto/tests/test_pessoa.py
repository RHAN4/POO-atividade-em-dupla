# import pytest
# from projeto.models.pessoa import Pessoa

# @pytest.fixture
# def pessoa_valida():
#     pessoa = Pessoa("Marta", 23)
#     return pessoa

# # Alterando o nome da pessoa de "Marta" para "Vitoria"
# def alterando_pessoa_nome(pessoa_valida):
#     pessoa_valida.nome = "Vitoria"
#     assert pessoa_valida.nome == "Vitoria"

# def test_pessoa_nome_valido(pessoa_valida):
#     assert pessoa_valida.nome == "Marta"

# def test_pessoa_idade_valida(pessoa_valida):
#     assert pessoa_valida.idade == 23

# # def test_pessoa_idade_negativa_retorna_mensagem_excecao(pessoa_valida):
# #     with pytest.raises(ValueError, match="Idade não pode ser negativa."):
# #         Pessoa("Marta", -1)