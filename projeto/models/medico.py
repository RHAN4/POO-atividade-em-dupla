from projeto.models.endereco import Endereco
from projeto.models.enums.estadoCivil import EstadoCivil
from projeto.models.enums.generos import Generos
from projeto.models.funcionario import Funcionario
from projeto.models.enums.setores import Setores

class Medico(Funcionario): 
    def __init__(self, id: str, nome: str, telefone: str, email: str, CPF: str, RG: str, matricula: str, setor: Setores, 
                 salario: str, endereco: Endereco, dataNascimento: str, genero: Generos, estadoCivil: EstadoCivil, CRM: str):
        super().__init__(id, nome, telefone, email, CPF, RG, matricula, setor, salario, endereco, dataNascimento, 
                         genero, estadoCivil)
        self.CRM = CRM 

    def __str__(self) -> str:
        return (f"\nCRM: {self.crm}")
        
    

        