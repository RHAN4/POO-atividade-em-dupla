from projeto.models.funcionario import Funcionario

class Motoboy(Funcionario):
    def __init__(self, cnh: str) -> None:
        self.cnh = cnh
    
    def __str__(self) -> str:
        return (f"\nCnh: {self.cnh}")
