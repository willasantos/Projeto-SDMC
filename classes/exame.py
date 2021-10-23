class Exame():
    def __init__(self, id_paciente, nome_paciente,data_hora, exame, cpf_paciente, telefone_paciente):
        self.id_paciente = id_paciente
        self.nome_paciente = nome_paciente
        self.data_hora = data_hora
        self.exame = exame
        self.cpf_paciente = cpf_paciente
        self.telefone_paciente = telefone_paciente

    def print(self):
        inf = [self.nome_paciente, self.data_hora, self.exame, self.cpf_paciente, self.telefone_paciente] 
        print(inf)

    def getInf(self):
        inf = [self.nome_paciente]
        return inf     