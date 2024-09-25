from abc import ABC, abstractmethod
from projeto.models.endereco import Endereco

class Pessoa(ABC):
    @abstractmethod
    def __init__(self, id: int,  nome: str, telefone: str, email: str, endereco: Endereco)  -> None:
        self.id = id
        self.nome = nome
        self.telefone = telefone 
        self.email = email 
        self.endereco = endereco 

if not isinstance(id, int):
    raise ValueError("ID deve conter apenas números.")
def test_id_int():
    id == "DDD"

    # def _verificar_id(self, id):
    #     if id < 0:
    #         raise ValueError("ID não pode ser negativa.")
    # if not isinstance(id, int):
    #         raise TypeError("ID deve conter apenas números.")
    # return id

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

                
    #  def _verificar_nome(self, nome):
    #      if nome == "Marta" 
         
    #def _verificar_idade(self, idade):
     #   if idade < 0:
      #      raise ValueError("Idade não pode ser negativa.")
       # if not isinstance(idade, int):
        ##    raise TypeError("Idade deve conter apenas números.")
        #return idade
