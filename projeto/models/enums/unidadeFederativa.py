from enum import Enum

class UF(enumerate):
    BAHIA = "Bahia"
    SAO_PAULO = "São Paulo"
    RIO_DE_JANEIRO = "Rio de Janeiro"

    def __init__(self, caractere: str, texto: str) -> None:
        self._caractere = caractere
        self._texto = texto

    @property
    def caractere(self) -> str:
        return self._caractere
    
    @property
    def texto(self) -> str:
        return self._texto