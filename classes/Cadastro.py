class Cadastro:
    def __init__(self, nome, cpf, cartao_sus, telefone, endereco, data, data_nascimento):
        self.nome = nome
        self.cpf = cpf
        self.cartao_sus = cartao_sus
        self.telefone = telefone
        self.endereco = endereco
        self.data = data
        self.data_nascimento = data_nascimento

    def imprimir(self):
        inf = [self.nome, self.cpf, self.cartao_sus, self.telefone, self.endereco, self.data_nascimento] 
        print(inf)

    def getInf(self):
        inf = [self.nome]
        return inf        
        