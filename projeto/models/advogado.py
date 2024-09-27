from projeto.models.endereco import Endereco
from projeto.models.enums.estadoCivil import EstadoCivil
from projeto.models.enums.generos import Generos
from projeto.models.funcionario import Funcionario
from projeto.models.enums.setores import Setores

class Advogado(Funcionario): 
    def __init__(self, id: int, nome: str, telefone: str, email: str, CPF: str, RG: str, matricula: str, setor: Setores, 
                 salario: int, endereco: Endereco, dataNascimento: str, genero: Generos, 
                 estadoCivil: EstadoCivil, OAB: str):
        super().__init__(id, nome, telefone, email, CPF, RG, matricula, setor, salario, endereco, dataNascimento,
                          genero, estadoCivil)
        self.OAB = OAB

    # def _verificar_id(self, valor):
    #         """Método para verificação de idade com métodos auxiliares."""
    #         self._verificar_id_tipo_invalido(valor)
    #         self._verificar_id_negativa(valor)

    #         self.idade = valor
    #         return self.idade

    # def _verificar_id_negativa(self, valor):
    #         """Método auxiliar para verificação de idade negativa."""
    #         if valor <= 0:
    #             raise ValueError("O ID não pode ser negativa.")


    # def _verificar_id(self, id: int) -> int:
    #     return super()._verificar_id(id)


    def __str__(self) -> str:
        return super().__str__()
    def __str__(self) -> str:
        return (f"\nOAB: {self.oab}")
        