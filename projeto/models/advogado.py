from projeto.models.funcionario import Funcionario

class Advogado(Funcionario): 
    def __init__(self, oab: str ) -> None:
        self.oab = oab
    
    def __str__(self) -> str:
        return (f"\nOab: {self.oab}")
        