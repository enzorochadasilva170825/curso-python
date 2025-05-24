import sqlite3
import requests
from config import WHATSAPP_URL, API_KEY

conexao = sqlite3.connect("clientes.db")
cursor = conexao.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS clientes (
    id INTEGER PRIMARY KEY AUTOINCREMENT, 
    nome TEXT NOT NULL,
    sobrenome TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    telefone TEXT,
    datanasc DATE
)
""")

def enviar_whatsapp(numero, texto):
    payload = {
        "number": numero,
        "text": texto
    }

    headers = {
        "content-type": "application/json",
        "apikey": API_KEY
    }

    try:
        response = requests.post(WHATSAPP_URL, json=payload, headers=headers)
        if response.status_code ==200:
            print(f'Mensagem enviada para {numero}')
        else:
            print(f'Erro ao enviar para {numero}: {response.status_code}-{response.text}')
    except Exception as e:
        print(f'Erro na requisição para {numero}: {e}')


enviar_whatsapp('5562982851012', 'teste simples')


conexao.commit()
conexao.close()


