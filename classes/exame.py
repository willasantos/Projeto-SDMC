class Exame():
    def __init__(self, Id, nome_paciente, exame):
        self.Id = Id
        self.nome_paciente = nome_paciente
        self.exame = exame

    def gitId(self):
        return self.Id

    def gitNome(self):
        return self.nome_paciente

    def gitExame(self):
        return self.exame            