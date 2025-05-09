import sqlite3
import tkinter as tk
from tkinter import messagebox
import os

# Cria uma janela oculta só para exibir os alertas
root = tk.Tk()
root.withdraw()

# Caminho absoluto do diretório do script atual
base_dir = os.path.dirname(os.path.abspath(__file__))

try:
    # Caminho absoluto do arquivo SQL
    sql_path = os.path.join(base_dir, "script-sqlite.sql")

    # Lê o script SQL
    with open(sql_path, "r", encoding="utf-8") as f:
        sql_script = f.read()

    # Cria o banco de dados no mesmo diretório
    db_path = os.path.join(base_dir, "cvm-dados.db")
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Executa o script
    cursor.executescript(sql_script)
    conn.commit()
    conn.close()

    print("✅ Banco de dados criado com sucesso!")
    messagebox.showinfo("Sucesso", "Banco de dados criado com sucesso!")

except Exception as e:
    print("❌ Ocorreu um erro ao criar o banco de dados:")
    print(e)
    messagebox.showerror("Erro", f"Ocorreu um erro:\n{str(e)}")
