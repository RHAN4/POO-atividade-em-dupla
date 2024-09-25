from abc import ABC, abstractmethod
from projeto.models.endereco import Endereco

class Pessoa(ABC):
    @abstractmethod
    def __init__(self, id: int,  nome: str, telefone: str, email: str, endereco: Endereco)  -> None:
        self.id = self._verificar_id(id)
        self.nome = nome
        self.telefone = telefone 
        self.email = email 
        self.endereco = endereco 
    
    def _verificar_id(self, id):
        if not isinstance(id, int):
            raise TypeError("Digite somente números inteiros para o ID.")
        return id

# Impedir que letras sejam inseridas para o ID
#if not isinstance(id, int):
#    raise TypeError("ID deve conter apenas números.")
# def test_id_int():
#     # id == "DDD"

# # Impedir que seja inserido números negativos para o ID
# if not isinstance (id, int):
#     raise ValueError("ID não pode ser negativa.")
# def test_id_positivo():
#     id == -7859

# def verificar_nome(self, nome):
#     if nome == "Vidraçaria":
#         pass
#         if not isinstance (nome, str):
#             raise NameError("O nome não pode ser vazio.")
# def test_nome_vazio():
#             nome == ""


# def verificar_id(self, id):
#     if id < 0:
#             raise ValueError("ID não pode ser negativa.")
#     if not isinstance(id, int):
#             raise TypeError("ID deve conter apenas números.")
#     return id

    # def _verificar_id(self, id: int) -> int:
    #     if not isinstance(id, int):
    #         raise TypeError("Digite somente números inteiros para ID.")
    #     if id < 0:
    #         raise ValueError("Digite um número que seja inteiro e positivo para ID.")
    #     return id


    def __str__(self) -> str:
        return (f"\nID: {self.id}"
                f"\nNome: {self.nome}"
                f"\nTelefone: {self.telefone}"
                f"\nEmail: {self.email}"
                f"\nEndereco: {self.endereco}"
                )
