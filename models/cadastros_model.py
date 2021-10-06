from classes.Cadastro import Cadastro
import database.database as DB

def getCadastro():
    conn = DB.connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM cadastro;")
    lista_cadastro  =[]
    for c in cursor.fetchall():
        id = c[0]
        nome = c[1]
        cpf = c[2]
        cartao_sus = c[3]
        telefone = c[4]
        endereco = c[5]
        novoCadastro = Cadastro(id, nome, cpf, cartao_sus, telefone, endereco)
        lista_cadastro.append(novoCadastro)

    conn.close()
    return lista_cadastro

def getCadastro(id):
    conn = DB.connect_db()
    cursor = conn.cursor()
    sql = """SELECT * FROM cadastro WHERE id = :"""
    cursor.execute(sql, [id])

    ponto = cursor.fetchall()[0]
    id = ponto[0]
    nome = ponto[1]
    cpf = ponto [2]
    cartao_sus = ponto[3]
    telefone = ponto[4]
    endereco = ponto[5]
    novoCadastro = Cadastro(id, nome, cpf, cartao_sus, telefone, endereco)
    conn.close()
    return novoCadastro    

def addCadastro(cadastro):
    conn = DB.connect_db()
    cursor = conn.cursor()
    sql = """INSERT INTO cadastro (nome, cpf, cartao_sus, telefone, endereco)
                      VALUES (?, ?, ?, ?, ?)"""
    cursor.execute(sql, [cadastro.nome, cadastro.cpf, cadastro.cartao_sus, cadastro.telefone, cadastro.endereco])
    conn.commit()
    conn.close()

def editCadastro(cadastro):
    conn = DB.connect_db()
    cursor = conn.cursor()
    sql = """UPDATE cadastro SET nome=?, cpf=?, cartao_sus=?, telefone=?, endereco=? WHERE id=?"""
    cursor.execute(sql[cadastro.nome, cadastro.cpf, cadastro.cartao_sus, cadastro.telefone, cadastro.endreco, cadastro.id])
    conn.commit()
    conn.close()

def delCadastro(id):
    conn = DB.connect_db()
    cursor = conn.cursor()
    sql = """DELETE FROM cadastro WHERE id = ?"""
    cursor.execute(sql, [id]) 
    conn.commit()
    conn.close()               