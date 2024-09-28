from abc import ABC, abstractmethod
from projeto.models.endereco import Endereco
from projeto.models.pessoa import Pessoa

class PessoaJuridica(Pessoa, ABC):
    @abstractmethod
    def __init__(self, id: int, nome: str, telefone: str, email: str, endereco: Endereco, 
                 CNPJ: str, inscricaoEstadual: str) -> None:
        super().__init__(id, nome, telefone, email, endereco)
        self.CNPJ = self._verificar_CNPJ(CNPJ)
        self.inscricaoEstadual = inscricaoEstadual

    def _verificar_CNPJ(self, CNPJ):
            if len(CNPJ) > 14:
                raise TypeError("CNPJ inválido.")
            return CNPJ

    def __str__(self) -> str:
        return super().__str__()
    def __str__(self) -> str:
        return (f"\nCNPJ: {self.CNPJ}"
                f"\nInscrição estadual: {self.inscricaoEstadual}")