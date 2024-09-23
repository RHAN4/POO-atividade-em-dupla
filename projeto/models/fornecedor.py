class Produto:
    def __init__(self, produto) -> None:
        self.produto = produto

    def __str__(self) -> str:
        return(f"Produto: {self.produto}")