from abc import ABC
from projeto.models.pessoa import Pessoa
from projeto.models.enums.generos import Generos
from projeto.models.enums.estadoCivil import EstadoCivil

class PessoaFisica(Pessoa):
    def __init__(self, dataNascimento, genero: Generos, estadoCivil: EstadoCivil) -> None:
        self.dataNascimento = dataNascimento
        self.genero = genero
        self.estadoCivil = estadoCivil

    def __str__(self) -> str:
        return (f"\nData de nascimento: {self.dataNascimento}"
                f"\nGênero: {self.genero}")
