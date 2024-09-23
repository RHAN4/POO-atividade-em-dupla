class Pessoa:
    def __init__(self, nome: str, idade: int) -> None:
        self.nome = nome
        self.idade = self._verificar_idade(idade)

    def _verificar_idade(self, idade):
        if idade < 0:
            raise ValueError("Idade não pode ser negativa.")
        if not isinstance(idade, int):
            raise TypeError("Idade deve conter apenas números.")
        return idade

    def __str__(self) -> str:
        return (f"\nNome: {self.nome}"
                f"\nIdade: {self.idade}")