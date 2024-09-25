from abc import ABC, abstractmethod
from projeto.models.endereco import Endereco
from projeto.models.pessoa import Pessoa

class PessoaJuridica(Pessoa, ABC):
    def __init__(self, id: int, nome: str, telefone: str, email: str, endereco: Endereco, 
                 CNPJ: str, inscricaoEstadual: str) -> None:
        super().__init__(id, nome, telefone, email, endereco)
        self.CNPJ = CNPJ
        self.inscricaoEstadual = inscricaoEstadual

    def __str__(self) -> str:
        return super().__str__()
    def __str__(self) -> str:
        return (f"\nCNPJ: {self.CNPJ}"
                f"\nInscrição estadual: {self.inscricaoEstadual}"
                f"\nPrestação de serviço: {self.prestacaoServico}")