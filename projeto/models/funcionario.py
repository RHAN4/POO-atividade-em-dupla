from abc import ABC, abstractmethod
from projeto.models.enums.setores import Setores
from projeto.models.pessoaFisica import PessoaFisica
from projeto.models.enums.generos import Generos
from projeto.models.enums.estadoCivil import EstadoCivil

class Funcionario(PessoaFisica, ABC):
    @abstractmethod
    def __init__(self, dataNascimento: str, genero: Generos, estadoCivil: EstadoCivil):
        super().__init__(dataNascimento, genero, estadoCivil)

    def __init__(self, CPF: str, RG: str, matricula: str, setor: Setores, salario: int) -> None:
        self.CPF = CPF
        self.RG = RG
        self.matricula = matricula
        self.setor = setor
        self.salario = salario

    def __str__(self) -> str:
        return (f"\nCPF: {self.CPF}"
                f"\nRG: {self.RG}"
                f"\nNúmero de matricula: {self.matricula}"
                f"\nSetor: {self.setor}"
                f"\nSalário: {self.salario}")