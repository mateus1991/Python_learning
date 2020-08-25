import os
import sqlite3
import sys

def conectar():
    con = sqlite3.connect("cartas.db")
    return con

def cria_cursor(con):
    cur = con.cursor()
    return cur

def cria_tabela(cur):
    try:
        sql_create = " CREATE TABLE Cartas"\
                    " (nome varchar(100) primary key, "\
                    "preco real, "\
                    "qtd integer, "\
                    "estado varchar(2))"
        cur.execute(sql_create)
    except sqlite3.OperationalError:
        pass

def escolher():
    print ("[1] Adicionar carta \n[2] "\
        "Excluir carta \n[3] Editar carta \n[4] Buscar carta "\
        "\n[5] Ver todas as cartas \n[6] Sair")
    escolha = int(input("\n Escolha o que fazer: "))
    return escolha

def adicionar_carta(cur,carta):
    try:
        sql_insert = "insert into Cartas values (?,?,?,?)"
        registro = [carta.nome, carta.preco, carta.qtd, carta.estado]
        cur.execute(sql_insert,registro)
        con.commit()
        print("Carta adicionada com sucesso!")

    except sqlite3.OperationalError:
        print("Não foi possível adicionar a carta")

def excluir_carta(cur, nome):
    try:
        sql_remove = "delete from Cartas where nome=?"
        cur.execute(sql_remove,nome)
        con.commit()
        print("Carta deletada com sucesso!")

    except sqlite3.OperationalError:
        print("Carta não encontrada!")
    

def editar_carta(cur):
    pass

def buscar_carta(cur):
    pass

def listar_cartas(cur):
    try:
        sql_select = "select * from Cartas"
        cur.execute (sql_select)
        dados = cur.fetchall()
        print(dados)

    except sqlite3.OperationalError:
        print("Nenhuma carta encontrada!")

class Carta:
    def __init__(self, nome = None, preco = 0.0, qtd = 0, estado = None):
        self.nome = nome
        self.preco = preco
        self.qtd = qtd
        self.estado = estado

    def setNome(self, nome):
        self.nome = nome

    def setPreco(self, preco):
        self.preco = preco

    def setQtd(self, qtd):
        self.qtd = qtd

    def setEstado(self, estado):
        self.estado = estado

    def getNome(self):
        return self.nome

    def getPreco(self):
        return self.preco

    def getQtd(self):
        return self.qtd

    def getEstado(self):
        return self.estado

con = conectar()
cur = cria_cursor(con)
cria_tabela(cur)

while (True):

    escolha = escolher()

    if (escolha == 1):
        nome = input("Entre com o nome da carta: ")
        preco = float(input("Entre com o preço da carta: "))
        qtd = int(input("Entre com a quantidade de cartas: "))
        estado = input("Entre com o estado da carta: ")
        c1 = Carta(nome, preco, qtd, estado)
        adicionar_carta(cur,c1)

    elif (escolha == 2):
        nome = input("Entre com o nome da carta que você quer excluir: ")
        excluir_carta(cur, nome)
    elif (escolha == 3):
        pass
    elif (escolha == 4):
        pass
    elif (escolha == 5):
        listar_cartas(cur)
    elif (escolha == 6):
        con.close()
        print("Adeus!")
        sys.exit()
    else:
        print("Opção inválida")

