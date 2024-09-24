from .pessoaJuridica import PessoaJuridica
from projeto.models.endereco import Endereco
from projeto.models.prestacaoServico import PrestacaoServico

class Fornecedor(PessoaJuridica):
    def __init__(self, id: int, nome: str, telefone: str, email: str, endereco: Endereco, CNPJ: str, 
                 inscricaoEstadual: str, prestacaoServico: PrestacaoServico, produto: str) -> None:
        super().__init__(id, nome, telefone, email, endereco, CNPJ, inscricaoEstadual, prestacaoServico)
        self.produto = produto
    

    def _verificar_id(self, id: int) -> int:
        return super()._verificar_id(id)
    
    def _verificar_nome(self, nome: str) -> str:
        return super()._verificar_nome(nome)
    
    def __str__(self) -> str:
        return super().__str__()
    
    def __str__(self) -> str:
        return (f"\nProduto: {self.produto}")