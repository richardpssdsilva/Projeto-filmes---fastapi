# pip install fastapi uvicorn mysql-connector-python dotenv
import mysql.connector
from dotenv import load_dotenv
import os

#Carregar .env
load_dotenv()


def conector():
    try:
        conexao = mysql.connector.connect(
            database=os.getenv("DB_NAME"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            host=os.getenv("DB_HOST"),
            port=os.getenv("DB_PORT")
        )
        cursor = conexao.cursor()
        return conexao, cursor
    except Exception as erro:
        print(f"Erro de conexao: {erro}")
        return None, None

conector()
    
