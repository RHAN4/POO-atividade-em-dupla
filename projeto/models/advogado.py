from projeto.models.funcionario import Funcionario

class Advogado(Funcionario): 
    def __init__(self, CPF: str, RG: str, matricula: str, setor: Setores, salario: int) -> None:
        super().__init__(CPF, RG, matricula, setor, salario)
   
    @abstractmethod
     def __init__(self, oab: str ) -> None:
         self.oab = oab
    
     def __str__(self) -> str:
         return (f"\nOAB: {self.oab}")
        