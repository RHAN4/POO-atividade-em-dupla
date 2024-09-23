from abc import ABC, abstractmethod
from projeto.models.enums.setores import Setores
class Funcionario(ABC):
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