import os
import tkinter as tk
from tkinter import messagebox, ttk
from datetime import datetime
import threading
from collectors.coletor import Coletor
from utils.logger import logger, escrever_linha_em_branco, escrever_linha_separador

# Empresas ---------------------------------------------------------------------------------------------------------------------
from service.empresas_service import process_csv_files
from repository.empresas_repository import ConexaoBanco

def atualizar_barra_progresso(progress_bar, status_label, status_text, max_value=100):
    status_label.config(text=status_text)
    progress_bar['value'] = 0
    for i in range(max_value + 1):
        progress_bar['value'] = i
        progress_bar.update_idletasks()
        threading.Event().wait(0.05)

def baixar_dados(progress_bar, status_label):
    def task():
        try:
            atualizar_barra_progresso(progress_bar, status_label, "Baixando dados...", 50)
            escrever_linha_separador(logger)
            logger.info("Iniciando processo de coleta de dados...")
            
            coletor = Coletor()
            coletor.collect_data()
            
            atualizar_barra_progresso(progress_bar, status_label, "Finalizando...", 100)
            logger.info("Coleta de dados concluída com sucesso!")
            messagebox.showinfo("Sucesso", "Dados baixados com sucesso!")
        except Exception as e:
            logger.error(f"Erro durante a coleta de dados: {str(e)}", exc_info=True)
            messagebox.showerror("Erro", f"Erro ao baixar dados: {str(e)}")
        finally:
            progress_bar['value'] = 0
            status_label.config(text="Pronto")
    threading.Thread(target=task, daemon=True).start()

def cadastrar_atualizar_empresas(progress_bar, status_label):
    def task():
        try:
            atualizar_barra_progresso(progress_bar, status_label, "Atualizando empresas...", 50)
            escrever_linha_separador(logger)
            logger.info("Processo iniciado de cadastro/atualização de Empresas.")
            
            base_path = os.path.join('data_extraido', 'FCA', 'sucesso')
            empresas = process_csv_files(base_path)
            
            banco = ConexaoBanco(host='localhost', database='cvm_dados', user='root', password='31415')
            banco.conectar()
            
            for empresa in empresas:
                banco.inserir_ou_atualizar_empresa(empresa)
            
            atualizar_barra_progresso(progress_bar, status_label, "Finalizando...", 100)
            banco.desconectar()
            logger.info("Processo de cadastro/atualização de Empresas finalizado com sucesso.")
            messagebox.showinfo("Sucesso", "Cadastro/Atualização de Empresas concluído!")
        except Exception as e:
            logger.error(f"Erro durante o processo de cadastro/atualização de Empresas: {str(e)}", exc_info=True)
            messagebox.showerror("Erro", f"Erro ao cadastrar/atualizar empresas: {str(e)}")
        finally:
            progress_bar['value'] = 0
            status_label.config(text="Pronto")
    threading.Thread(target=task, daemon=True).start()

def criar_interface():
    root = tk.Tk()
    root.title("Gestão de Empresas")
    root.geometry("700x300")
    
    frame_top = tk.Frame(root)
    frame_top.pack(pady=10)
    
    label = tk.Label(frame_top, text="Gestão de Empresas", font=("Arial", 16, "bold"))
    label.pack()
    
    frame_buttons = tk.Frame(root)
    frame_buttons.pack(pady=10)
    
    status_label = tk.Label(root, text="Pronto", font=("Arial", 12))
    status_label.pack(pady=5)
    
    progress_bar = ttk.Progressbar(root, mode='determinate', length=400)
    progress_bar.pack(pady=5)
    
    btn_baixar = tk.Button(frame_buttons, text="Baixar Dados", command=lambda: baixar_dados(progress_bar, status_label), font=("Arial", 12), width=20)
    btn_baixar.grid(row=0, column=0, padx=10, pady=5)
    
    btn_atualizar = tk.Button(frame_buttons, text="Atualizar Empresas", command=lambda: cadastrar_atualizar_empresas(progress_bar, status_label), font=("Arial", 12), width=20)
    btn_atualizar.grid(row=0, column=1, padx=10, pady=5)
    
    btn_sair = tk.Button(frame_buttons, text="Sair", command=root.quit, font=("Arial", 12), width=20)
    btn_sair.grid(row=0, column=2, padx=10, pady=5)
    
    root.mainloop()

def main():
    criar_interface()
    escrever_linha_em_branco(logger)

if __name__ == "__main__":
    main()
