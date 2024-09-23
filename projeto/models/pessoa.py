from abc import ABC, abstractmethod
from projeto.models.endereco import Endereco

class Pessoa(ABC):
    @abstractmethod
    def __init__(self, id: str,  nome: str, telefone: str, email: str, endereco: Endereco)  -> None:
        self.id = id 
        self.nome = nome
        self.telefone = telefone 
        self.email = email 
        self.endereco = endereco 
    
    def __str__(self) -> str:
        return (f"\nId: {self.id}"
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
