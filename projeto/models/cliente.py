from projeto.models.endereco import Endereco
from projeto.models.enums.estadoCivil import EstadoCivil
from projeto.models.enums.generos import Generos
from projeto.models.pessoaFisica import PessoaFisica

class Cliente(PessoaFisica):
    def __init__(self, id: str, nome: str, telefone: str, email: str, endereco: Endereco, 
                 dataNascimento: str, genero: Generos, estadoCivil: EstadoCivil, protocoloAtendimento: str):
        super().__init__(id, nome, telefone, email, endereco, dataNascimento, genero, estadoCivil)
        self.protocoloAtendimento = protocoloAtendimento

    def _verificar_id(self, id: int) -> int:
        return super()._verificar_id(id)

    def __str__(self) -> str:
        return super().__str__()
    def __str__(self) -> str:
        return (f"\nNúmero de protocolo: {self.protocoloAtendimento}")