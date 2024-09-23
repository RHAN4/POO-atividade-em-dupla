from projeto.models.pessoaFisica import PessoaFisica

class Cliente(PessoaFisica):
    def __init__(self, protocoloAtendimento) -> None:
        self.protocoloAtendimento = protocoloAtendimento

    def __str__(self) -> str:
        return (f"\nNúmero de protocolo: {self.protocoloAtendimento}")