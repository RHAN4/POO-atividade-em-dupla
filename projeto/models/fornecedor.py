from projeto.models.endereco import Endereco
from projeto.models.pessoaJuridica import PessoaJuridica

class Fornecedor(PessoaJuridica):
    def __init__(self, id: int, nome: str, telefone: str, email: str, 
                 endereco: Endereco, CNPJ: str, inscricaoEstadual: str, 
                 produto: str) -> None:
        super().__init__(id, nome, telefone, email, endereco, 
                         CNPJ, inscricaoEstadual)
        self.produto = produto

    def __str__(self) -> str:
        return super().__str__()
    def __str__(self) -> str:
        return (f"\nProduto fornecido: {self.produto}")

# if not isinstance(id, int):
#     raise ValueError("ID deve conter apenas números.")
# def test_id_int():
#     id == "555"