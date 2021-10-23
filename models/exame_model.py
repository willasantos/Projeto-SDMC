from classes.exame import Exame
import database.database as db

def gettExame():
    conn = db.connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM exame;")
    lista_exame = []
    for e in cursor.fetchall():
        id_paciente = e[0]
        nome_paciente = e[1]
        data_hora = e[2]
        exame = e[3]
        cpf_paciente = e[4]
        telefone_paciente = e[5]
        novoExame = Exame(id_paciente, nome_paciente, data_hora, exame, cpf_paciente, telefone_paciente)
        lista_exame.append(novoExame)
    conn.close()
    return lista_exame

def getExame(id_paciente):
    conn = db.connect_db()
    cursor = conn.cursor()
    sql = """SELECT * FROM exame WHERE id_paciente = ?;"""
    cursor.execute(sql, [id_paciente])

    ponto = cursor.fetchall()[0]
    id_paciente = ponto[0]
    nome_paciente = ponto[1]
    data_hora = ponto[2]
    exame = ponto[3]
    cpf_paciente = ponto[4]
    telefone_paciente = ponto[5]
    novoExame = Exame(id_paciente, nome_paciente, data_hora, exame, cpf_paciente, telefone_paciente)
    conn.close()
    return novoExame

def addExame(exame):
    conn = db.connect_db()
    cursor = conn.cursor()
    sql = """INSERT INTO exame (nome_paciente, data_hora, exame, cpf_paciente, telefone_paciente)
                      VALUES (?, ?, ?, ?, ?)"""
    cursor.execute(sql, [exame.nome_paciente, exame.data_hora, exame.exame, exame.cpf_paciente, exame.telefone_paciente])
    conn.commit()
    conn.close()

def editExame(exame):
    conn = db.connect_db()
    cursor = conn.cursor()
    sql = """UPDATE exame SET nome_paciente=?, data_hora =?, exame =?, cpf_paciente = ?, telefone_paciente=?  WHERE id_paciente =?"""
    cursor.execute(sql,[exame.nome_paciente, exame.data_hora, exame.exame, exame.cpf_paciente, exame.telefone_paciente, exame.id_paciente])  
    conn.commit()
    conn.close()

def delExame(id_paciente):
    conn = db.connect_db()
    cursor = conn.cursor()
    sql = """DELETE FROM exame WHERE id_paciente = ?"""
    cursor.execute(sql, [id_paciente]) 
    conn.commit()
    conn.close()              
