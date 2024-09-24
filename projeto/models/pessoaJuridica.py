from projeto.models.endereco import Endereco
from projeto.models.pessoa import Pessoa
from projeto.models.prestacaoServico import PrestacaoServico
from projeto.models.fornecedor import Produto

class PessoaJuridica(Pessoa):
    def __init__(self, id: str, nome: str, telefone: str, email: str, endereco: Endereco, 
                 CNPJ: str, inscricaoEstadual: str, prestacaoServico: PrestacaoServico,
                  fornecedor: Produto) -> None:
        super().__init__(id, nome, telefone, email, endereco)
        self.CNPJ = CNPJ
        self.inscricaoEstadual = inscricaoEstadual
        self.prestacaoServico = prestacaoServico
        self.produto = fornecedor

    def __str__(self) -> str:
        return super().__str__()
    def __str__(self) -> str:
        return (f"\nCNPJ: {self.CNPJ}"
                f"\nInscrição estadual: {self.inscricaoEstadual}"
                f"\nPrestação de serviço: {self.prestacaoServico}"
                f"\nFornecedor: {self.fornecedor}")
