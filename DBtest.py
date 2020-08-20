import sqlite3
import os

#Remove o DB caso exista
os.remove ("moradores.db") if os.path.exists("moradores.db") else None

#conecta no DB
con = sqlite3.connect("moradores.db")

#Cria o cursor para o DB
cur = con.cursor()


#Cria tabela SQL
sql_create = "create table apartamento"\
             "(id integer primary key, "\
             "morador varchar(100), "\
             "andar varchar(50))"

#Executar comando SQL no cursor
cur.execute(sql_create)

#Inserir registros na tabela criada
sql_insert = "insert into apartamento values (?,?,?)"

#Dados que serão inseridos
registros = [(100, "Ana Paula", "Térreo"),
            (101, "Mateus", "Primeiro"),
            (102, "Lucas Roberto", "Primeiro"),
            (202, "Malaquias", "Segundo")]

#Inserir registros
for registro in registros:
    cur.execute(sql_insert,registro)

#Sem o commit os dados não são salvos
con.commit()

#Seleciona todos os registros na tabela
sql_select = "select * from apartamento"
cur.execute(sql_select)

#Recuperar todos os dados e armazená-los
dados = cur.fetchall()

print(dados)

#Fecha conexão
con.close()
