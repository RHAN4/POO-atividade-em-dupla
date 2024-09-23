class PrestacaoServico:
    def __init__(self, contratoInicio: str, contratoFim: str) -> None:
        self.contratoInicio = contratoInicio
        self.contratoFim = contratoFim
    
    def __str__(self) -> str:
        return(f"\nInicio do contrato: {self.contratoInicio}"
               f"\nFim do contrato: {self.contratoFim}")