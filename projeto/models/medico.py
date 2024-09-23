from projeto.models.funcionario import Funcionario
from projeto.models.enums.setores import Setores

class Medico(Funcionario): 
    def __init__(self, CPF: str, RG: str, matricula: str, setor: Setores, salario: int):
     super().__init__(CPF, RG, matricula, setor, salario)

    def __init__(self, crm: str) -> None:
        self.crm = crm 

    def __str__(self) -> str:
        return (f"\nCRM: {self.crm}")
        
    

        