import sqlite3
import tkinter as tk
from tkinter import messagebox

# Cria uma janela oculta só para exibir os alertas
root = tk.Tk()
root.withdraw()

try:
    # Lê o script SQL
    with open("script-sqlite.sql", "r", encoding="utf-8") as f:
        sql_script = f.read()

    # Cria o banco de dados
    conn = sqlite3.connect("cvm-dados.db")
    cursor = conn.cursor()

    # Executa o script
    cursor.executescript(sql_script)
    conn.commit()
    conn.close()

    # Mensagem de sucesso
    print("✅ Banco de dados criado com sucesso!")
    messagebox.showinfo("Sucesso", "Banco de dados criado com sucesso!")

except Exception as e:
    # Mensagem de erro no terminal e em janela gráfica
    print("❌ Ocorreu um erro ao criar o banco de dados:")
    print(e)
    messagebox.showerror("Erro", f"Ocorreu um erro:\n{str(e)}")
