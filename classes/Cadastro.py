class Cadastro:
    def __init__(self, nome, cpf, cartao_sus, telefone, endereco):
        self.nome = nome
        self.cpf = cpf
        self.cartao_sus = cartao_sus
        self.telefone = telefone
        self.endereco = endereco

    def imprimir(self):
        inf = [self.nome, self.cpf, self.cartao_sus, self.telefone, self.endereco] 
        print(inf)

    def getInf(self):
        inf = [self.nome]
        return inf        
        