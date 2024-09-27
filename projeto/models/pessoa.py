from abc import ABC, abstractmethod
from projeto.models.endereco import Endereco

class Pessoa(ABC):
    @abstractmethod
    def __init__(self, id: int,  nome: str, telefone: str, email: str, endereco: Endereco)  -> None:
        self.id = self._verificar_id(id)
        self.nome = self._verificar_nome(nome)
        self.telefone = self._verificar_telefone(telefone)
        self.email = self._verificar_email(email)
        self.endereco = endereco 
    
    def _verificar_id(self, id):
            if not isinstance(id, int):
                raise TypeError("Digite apenas números para o ID")
            if id < 0:
                raise ValueError("Digite apenas números positivos para o ID")
            return id

    def _verificar_nome(self, nome):
            if not isinstance(nome, str) or not nome.strip():
                raise ValueError("O nome não pode estar em branco")
            return nome
    
    def _verificar_telefone(self, telefone):
        if not isinstance (telefone, str):
            raise TypeError("Digite apenas números.")
        return telefone
    
    def _verificar_email(self, email):
            if not isinstance(email, str) or not email.strip():
                raise TypeError("Email não pode estar vazio.")
            return email

    def __str__(self) -> str:
        return (f"\nID: {self.id}"
                f"\nNome: {self.nome}"
                f"\nTelefone: {self.telefone}"
                f"\nEmail: {self.email}"
                f"\nEndereco: {self.endereco}"
                )
