import sqlite3

conexao = sqlite3.connect("clientes.db")
cursor = conexao.cursor()

cursor.executemany("""
INSERT INTO clientes (nome, sobrenome, email, telefone, datanasc)
VALUES (?, ?, ?, ?, ?)
""", [
    ("Enzo","Rocha", "enzoba.selva@gmail.com","(62)98285-1012","2011-06-27"),
    ("Luciana","Antunes","lucianarochaantunes@gmail.com","(62)98141-6742","1964-03-08")
])

conexao.commit() 
conexao.close()


