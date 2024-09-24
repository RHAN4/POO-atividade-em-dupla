from projeto.models.endereco import Endereco
from projeto.models.enums.estadoCivil import EstadoCivil
from projeto.models.enums.generos import Generos
from projeto.models.funcionario import Funcionario
from projeto.models.enums.setores import Setores

class Advogado(Funcionario): 
    def __init__(self, id: str, nome: str, telefone: str, email: str, CPF: str, RG: str, matricula: str, setor: Setores, 
                 salario: str, endereco: Endereco, dataNascimento: str, genero: Generos, 
                 estadoCivil: EstadoCivil, OAB: str):
        super().__init__(id, nome, telefone, email, CPF, RG, matricula, setor, salario, endereco, dataNascimento,
                          genero, estadoCivil)
        self.OAB = OAB

    def _verificar_id(self, id: int) -> int:
        return super()._verificar_id(id)


    def __str__(self) -> str:
        return super().__str__()
    def __str__(self) -> str:
        return (f"\nOAB: {self.oab}")
        