class SobreExame():
    def __init__(self, id_exame, nome_exame, data_exame, tipo):
        self.id_exame = id_exame
        self.nome_exame = nome_exame
        self.data_exame = data_exame
        self.tipo = tipo

    def getId(self):
        return self.id_exame

    def getNome(self):
        return self.nome_exame

    def getData(self):
        return self.data_exame

    def getexame(self):
        return self.tipo                