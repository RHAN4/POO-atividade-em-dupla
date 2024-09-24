from projeto.models.pessoa import Pessoa
from projeto.models.endereco import Endereco
from projeto.models.enums.generos import Generos
from projeto.models.enums.estadoCivil import EstadoCivil

class PessoaFisica(Pessoa):
    def __init__(self, id: str,  nome: str, telefone: str, email: str, endereco: Endereco,
                  dataNascimento: str, genero: Generos, estadoCivil: EstadoCivil):
        super().__init__(id, nome, telefone, email, endereco)
        self.dataNascimento = dataNascimento
        self.genero = genero
        self.estadoCivil = estadoCivil

    def __str__(self) -> str:
        return super().__str__()
    
    def __str__(self) -> str:
        return (f"\nData de nascimento: {self.dataNascimento}"
                f"\nGênero: {self.genero}")
