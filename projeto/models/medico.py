from projeto.models.funcionario import Funcionario

class Medico(Funcionario): 
    def __init__(self, crm: str) -> None:
        self.crm = crm 

    def __str__(self) -> str:
        return (f"\nCrm: {self.crm}")
        
    

        