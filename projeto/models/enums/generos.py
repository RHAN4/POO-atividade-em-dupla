from enum import Enum

class Generos(enumerate):
    FEMININO = ("Feminino", "F")
    MASCULINO = ("Masculino", "M")

    def __init__(self, caractere: str, texto: str) -> None:
        self._caractere = caractere
        self._texto = texto

    @property
    def caractere(self) -> str:
        return self._caractere
    
    @property
    def texto(self) -> str:
        return self._texto