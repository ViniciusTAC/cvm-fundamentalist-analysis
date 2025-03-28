import mysql.connector
import tkinter as tk
from tkinter import messagebox

# Cria uma janela oculta só para os alertas
root = tk.Tk()
root.withdraw()

try:
    # Lê o script SQL
    with open("script-mysql-workbench.sql", "r", encoding="utf-8") as f:
        sql_script = f.read()

    # Conecta ao servidor MySQL (ajuste os dados conforme necessário)
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="31415"
    )
    cursor = conn.cursor()

    # # Cria o banco de dados (se necessário)
    # cursor.execute("CREATE DATABASE IF NOT EXISTS cvm_dados_teste;")
    # cursor.execute("USE cvm_dados_teste;")

    # Divide e executa os comandos SQL
    for statement in sql_script.split(';'):
        stmt = statement.strip()
        if stmt:
            cursor.execute(stmt)

    conn.commit()
    cursor.close()
    conn.close()

    # Mensagem de sucesso
    print("✅ Banco de dados MySQL criado com sucesso!")
    messagebox.showinfo("Sucesso", "Banco de dados MySQL criado com sucesso!")

except Exception as e:
    print("❌ Ocorreu um erro ao criar o banco de dados:")
    print(e)
    messagebox.showerror("Erro", f"Ocorreu um erro:\n{str(e)}")
