class Info:
    def __init__(self, medico, area , nome_paciente):
        self.medico = medico
        self.area = area
        self.nome_paciente = nome_paciente

    def getMedico(self):
        return self.medico

    def getArea(self):
        return self.area 

    def getNome(self):
        return self.nome_paciente      