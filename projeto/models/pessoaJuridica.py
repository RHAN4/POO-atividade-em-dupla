from projeto.models.pessoa import Pessoa
from projeto.models.prestacaoServico import PrestacaoServico
from projeto.models.fornecedor import Fornecedor

class PessoaJuridica(Pessoa):
    def __init__(self, CNPJ: str, inscricaoEstadual: str, prestacaoServico: PrestacaoServico,
                 fornecedor: Fornecedor) -> None:
        self.CNPJ = CNPJ
        self.inscricaoEstadual = inscricaoEstadual
        self.prestacaoServico = prestacaoServico
        self.fornecedor = fornecedor
