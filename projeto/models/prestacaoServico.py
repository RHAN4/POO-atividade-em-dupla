from projeto.models.pessoaJuridica import PessoaJuridica
from projeto.models.endereco import Endereco

class PrestacaoServico(PessoaJuridica):
    def __init__(self, id: int, nome: str, telefone: str, email: str, 
                 endereco: Endereco, CNPJ: str, inscricaoEstadual: str, 
                 contratoInicio: str, contratoFim: str) -> None:
        super().__init__(id, nome, telefone, email, endereco, CNPJ, 
                         inscricaoEstadual)
        self.contratoInicio = contratoInicio
        self.contratoFim = contratoFim
    
    def __str__(self) -> str:
        return super().__str__()
    def __str__(self) -> str:
        return(f"\nInicio do contrato: {self.contratoInicio}"
               f"\nFim do contrato: {self.contratoFim}")