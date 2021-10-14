class Historico():
    def __init__(self, id_cliente, nome_cliente, data_consulta, especialidade_medico):
        self.id_cliente = id_cliente
        self.nome_cliente = nome_cliente
        self.data_consulta = data_consulta
        self.especialidade_medico = especialidade_medico

    def getId(self):
        return self.id_cliente

    def getNome(self):
        return self.nome_cliente

    def getData(self):
        return self.data_consulta

    def getEspecialidade(self):
        return self.especialidade_medico            