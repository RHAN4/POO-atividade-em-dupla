import enum

class UnidadeFederativa(Enum): 

    BAHIA = ("Bahia", "BA")
    SAO_PAULO = ("São Paulo", "SP")
    RIO_DE_JANEIRO = ("Rio de Janeiro", "Rj")


    def __init__(self, caractere: str, texto: str):
        self._caractere = caractere
        self._texto = texto

    @property
    def caractere(self) -> str:
        return self._caractere

    @property
    def texto(self) -> str:
        return self._texto


