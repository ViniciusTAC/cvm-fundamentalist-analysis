import os
import sys
import shutil
import subprocess
import threading
import tkinter as tk
from tkinter import messagebox

from utils.logger import logger, escrever_linha_em_branco, escrever_linha_separador
from collectors.coletor import Coletor

from service.empresas_service import process_csv_files as process_empresas
from repository.empresas_repository import ConexaoBanco as BancoEmpresas

from service.periodicos_eventuais_service import process_csv_files as process_ipe
from repository.periodicos_eventuais_repository import ConexaoBanco as BancoIPE

from service.formulario_referencia_service import process_csv_files as process_fre
from repository.formulario_referencia_repository import ConexaoBanco as BancoFRE

from service.parecer_demonstrativo_service import process_csv_files as process_parecer_demo
from repository.parecer_demonstrativo_repository import ConexaoBanco as BancoParecerDemo

from service.parecer_trimestral_service import process_csv_files as process_parecer_trim
from repository.parecer_trimestral_repository import ConexaoBanco as BancoParecerTrim

from service.numeros_acoes_service import process_csv_files as process_num_acoes
from repository.numeros_acoes_repository import ConexaoBanco as BancoNumAcoes

from service.demostrativo_financeiro_service import process_dfp_files as process_dfp
from repository.demostrativo_financeiro_repository import ConexaoBanco as BancoDemostrativo

from service.informacao_trimestral_service import process_dfp_files as process_itr
from repository.informacao_trimestral_repository import ConexaoBanco as BancoInformacaoTri

CAMINHO_BANCO = os.path.join("sqlite-projeto", "cvm-dados.db")
cancelar_evento = threading.Event()

ETIQUETAS = {
    "coletar": "Coletar e Extrair Dados",
    "empresas": "Empresas",
    "ipe": "Periódicos Eventuais",
    "fre": "Formulários de Referência",
    "parecer_demo": "Parecer - Demonst. Financeiros",
    "parecer_trim": "Parecer - Inf. Trimestrais",
    "num_acoes": "Número de Ações",
    "dfp": "Demonstrativos Financeiros",
    "itr": "Informações Trimestrais",
}

def executar_script_inicial():
    if os.path.exists(CAMINHO_BANCO):
        messagebox.showinfo("Banco de Dados", "Banco de dados já existe. Pulando execução do script.")
        return

    try:
        subprocess.run(
            [sys.executable, "sqlite-projeto/script-automatizar-sqlite.py"],
            check=True
        )
        messagebox.showinfo("Sucesso", "✅ Script de automação executado com sucesso.")
    except subprocess.CalledProcessError as e:
        logger.error(f"Erro no script inicial: {str(e)}", exc_info=True)
        messagebox.showerror("Erro", f"❌ Erro ao executar o script:\n{str(e)}")
        sys.exit(1)

def executar_etapa(nome, base_path, processar, repositorio_cls, metodo_insercao, extras=None):
    try:
        escrever_linha_separador(logger)
        logger.info(f"Iniciando etapa: {nome}")

        dados = processar(base_path) if extras is None else processar(base_path, *extras)
        banco = repositorio_cls(db_path=CAMINHO_BANCO)
        banco.conectar()

        conn = banco.connection  # <- substituto correto
        conn.execute("BEGIN")

        sucesso = 0
        falha = 0
        erros = []

        for dado in dados:
            if cancelar_evento.is_set():
                conn.rollback()
                banco.desconectar()
                logger.warning(f"{nome} abortado com rollback.")
                return f"{nome} abortado pelo usuário."
            try:
                getattr(banco, metodo_insercao)(dado)
                sucesso += 1
            except Exception as e:
                falha += 1
                erros.append(str(e))
                logger.warning(f"Erro ao inserir {dado}: {str(e)}")

        conn.commit()
        banco.desconectar()
        logger.info(f"{nome} finalizado com sucesso. Inseridos: {sucesso}, Falhas: {falha}")

        if falha:
            return f"{nome}: {sucesso} inseridos, {falha} com erro.\nExemplos de erro: {erros[:3]}"
        else:
            return f"{nome}: Todos os {sucesso} registros inseridos com sucesso."

    except Exception as e:
        logger.error(f"Erro na etapa {nome}: {str(e)}", exc_info=True)
        if 'banco' in locals():
            try:
                conn.rollback()
            except:
                pass
            banco.desconectar()
        escrever_linha_em_branco(logger)
        return f"Erro fatal em {nome}: {str(e)}"


def run_processos_selecionados(root, vars, status_label):
    status_label.config(text="🔄 Executando...", fg="blue")
    root.update()

    try:
        mensagens = []
        executar_script_inicial()

        if vars["coletar"].get():
            coletor = Coletor()
            coletor.collect_data()
            mensagens.append("Coleta e extração concluídas.")
            
        etapas = [
            ("empresas", "Empresas", "data_extraido/FCA/sucesso", process_empresas, BancoEmpresas, "inserir_ou_atualizar_empresa"),
            ("ipe", "Periódicos Eventuais", "data_extraido/IPE/sucesso", process_ipe, BancoIPE, "inserir_periodicos_eventuais"),
            ("fre", "Formulários de Referência", "data_extraido/FRE/sucesso", process_fre, BancoFRE, "inserir_formulario_referencia"),
            ("parecer_demo", "Parecer - Demonst. Financeiros", "data_extraido/DFP/sucesso", process_parecer_demo, BancoParecerDemo, "inserir_parecer_demonstrativo"),
            ("parecer_trim", "Parecer - Inf. Trimestrais", "data_extraido/ITR/sucesso", process_parecer_trim, BancoParecerTrim, "inserir_parecer_trimestral"),
            
        ]

        for chave, nome, caminho, func, banco_cls, metodo in etapas:
            if vars[chave].get():
                mensagem = executar_etapa(nome, caminho, func, banco_cls, metodo) or f"{nome}: Nenhuma ação executada."
                mensagens.append(mensagem)

        if vars["num_acoes"].get():
            try:
                escrever_linha_separador(logger)
                logger.info("Iniciando etapa: Número de Ações")
                # show_message("Processo iniciado", "🔄 Número de Ações")

                dfp = process_num_acoes(os.path.join("data_extraido", "DFP", "sucesso"), "DFP")
                itr = process_num_acoes(os.path.join("data_extraido", "ITR", "sucesso"), "ITR")
                dados = dfp + itr

                banco = BancoNumAcoes(db_path=CAMINHO_BANCO)
                banco.conectar()

                sucesso = 0
                falha = 0
                erros = []

                conn = banco.connection
                conn.execute("BEGIN")

                for dado in dados:
                    if cancelar_evento.is_set():
                        conn.rollback()
                        banco.desconectar()
                        logger.warning("Número de Ações abortado com rollback.")
                        mensagens.append("Número de Ações abortado pelo usuário.")
                        break
                    try:
                        banco.inserir_numeros_acoes(dado)
                        sucesso += 1
                    except Exception as e:
                        falha += 1
                        erros.append(str(e))
                        logger.warning(f"Erro ao inserir {dado}: {str(e)}")

                conn.commit()
                banco.desconectar()

                logger.info(f"Número de Ações finalizado com sucesso. Inseridos: {sucesso}, Falhas: {falha}")

                if falha:
                    mensagens.append(f"Número de Ações: {sucesso} inseridos, {falha} com erro.\nExemplos de erro: {erros[:3]}")
                else:
                    mensagens.append(f"Número de Ações: Todos os {sucesso} registros inseridos com sucesso.")

            except Exception as e:
                logger.error(f"Erro na etapa Número de Ações: {str(e)}", exc_info=True)
                mensagens.append(f"Erro fatal em Número de Ações: {str(e)}")
                escrever_linha_em_branco(logger)

        
        if vars["dfp"].get():
            try:
                escrever_linha_separador(logger)
                logger.info("Iniciando etapa: Demonstrativos Financeiros")
                # show_message("Processo iniciado", "🔄 Demonstrativos Financeiros")

                banco = BancoDemostrativo(db_path=CAMINHO_BANCO)
                banco.conectar()

                conn = banco.connection
                conn.execute("BEGIN")

                dados = process_dfp("data_extraido/DFP/sucesso", banco)

                sucesso = 0
                falha = 0
                erros = []

                for dado in dados:
                    if cancelar_evento.is_set():
                        conn.rollback()
                        banco.desconectar()
                        logger.warning("Demonstrativos Financeiros abortado com rollback.")
                        mensagens.append("Demonstrativos Financeiros abortado pelo usuário.")
                        break
                    try:
                        banco.inserir_ou_atualizar_demonstrativo(dado)
                        sucesso += 1
                    except Exception as e:
                        falha += 1
                        erros.append(str(e))
                        logger.warning(f"Erro ao inserir {dado}: {str(e)}")

                conn.commit()
                banco.desconectar()

                logger.info(f"Demonstrativos Financeiros finalizado. Inseridos: {sucesso}, Falhas: {falha}")
                if falha:
                    mensagens.append(f"Demonstrativos Financeiros: {sucesso} inseridos, {falha} com erro.\nExemplos: {erros[:3]}")
                else:
                    mensagens.append(f"Demonstrativos Financeiros: Todos os {sucesso} registros inseridos com sucesso.")
            except Exception as e:
                logger.error(f"Erro em Demonstrativos Financeiros: {str(e)}", exc_info=True)
                mensagens.append(f"Erro fatal em Demonstrativos Financeiros: {str(e)}")
                escrever_linha_em_branco(logger)

        if vars["itr"].get():
            try:
                escrever_linha_separador(logger)
                logger.info("Iniciando etapa: Informações Trimestrais")
                # show_message("Processo iniciado", "🔄 Informações Trimestrais")

                banco = BancoInformacaoTri(db_path=CAMINHO_BANCO)
                banco.conectar()

                conn = banco.connection
                conn.execute("BEGIN")

                dados = process_itr("data_extraido/ITR/sucesso", banco)

                sucesso = 0
                falha = 0
                erros = []

                for dado in dados:
                    if cancelar_evento.is_set():
                        conn.rollback()
                        banco.desconectar()
                        logger.warning("Informações Trimestrais abortado com rollback.")
                        mensagens.append("Informações Trimestrais abortado pelo usuário.")
                        break
                    try:
                        banco.inserir_ou_atualizar_informacao_tri(dado)
                        sucesso += 1
                    except Exception as e:
                        falha += 1
                        erros.append(str(e))
                        logger.warning(f"Erro ao inserir {dado}: {str(e)}")

                conn.commit()
                banco.desconectar()

                logger.info(f"Informações Trimestrais finalizado. Inseridos: {sucesso}, Falhas: {falha}")
                if falha:
                    mensagens.append(f"Informações Trimestrais: {sucesso} inseridos, {falha} com erro.\nExemplos: {erros[:3]}")
                else:
                    mensagens.append(f"Informações Trimestrais: Todos os {sucesso} registros inseridos com sucesso.")
            except Exception as e:
                logger.error(f"Erro em Informações Trimestrais: {str(e)}", exc_info=True)
                mensagens.append(f"Erro fatal em Informações Trimestrais: {str(e)}")
                escrever_linha_em_branco(logger)


        status_label.config(text="✅ Finalizado com sucesso", fg="green")

        resumo_texto = "\n\n".join(mensagens)
        with open("resumo_execucao.log", "w", encoding="utf-8") as f:
            f.write(resumo_texto)

        resumo_window = tk.Toplevel(root)
        resumo_window.title("Resumo da Execução")
        resumo_window.geometry("600x400")

        texto = tk.Text(resumo_window, wrap="word")
        texto.insert("1.0", resumo_texto)
        texto.config(state="disabled")
        texto.pack(fill="both", expand=True)

        scrollbar = tk.Scrollbar(resumo_window, command=texto.yview)
        texto.config(yscrollcommand=scrollbar.set)
        scrollbar.pack(side="right", fill="y")

    except Exception as e:
        status_label.config(text=f"❌ Erro: {str(e)}", fg="red")
        logger.error("Erro geral no processamento", exc_info=True)

    pasta_data = os.path.join(os.getcwd(), "data")
    pasta_extraido = os.path.join(os.getcwd(), "data_extraido")
    if os.path.exists(pasta_extraido):
        if messagebox.askyesno("Limpeza", "Deseja remover as pastas temporárias 'data' e 'data_extraido'?"):
            try:
                shutil.rmtree(pasta_extraido)
                logger.info("Pasta 'data_extraido' removida.")
                if os.path.exists(pasta_data):
                    shutil.rmtree(pasta_data)
                    logger.info("Pasta 'data' removida.")
            except Exception as e:
                logger.warning(f"Erro ao remover pastas: {str(e)}")

def criar_interface():
    root = tk.Tk()
    root.title("Atualizador CVM")

    vars = {chave: tk.BooleanVar(value=True) for chave in ETIQUETAS.keys()}

    tk.Label(root, text="Selecione as etapas a executar:", font=("Arial", 12, "bold")).pack(pady=10)

    checkbox_frame = tk.Frame(root)
    checkbox_frame.pack()

    for chave, var in vars.items():
        label = ETIQUETAS[chave]
        tk.Checkbutton(checkbox_frame, text=label, variable=var).pack(anchor='w')

    status_label = tk.Label(root, text="Aguardando execução...", fg="gray")
    status_label.pack(pady=10)

    def on_run():
        cancelar_evento.clear()
        threading.Thread(target=run_processos_selecionados, args=(root, vars, status_label), daemon=True).start()

    def on_abort():
        if messagebox.askyesno("Confirmar Abortamento", "Deseja realmente cancelar a execução? Os dados parciais serão descartados."):
            cancelar_evento.set()
            status_label.config(text="⏹ Execução cancelada pelo usuário", fg="orange")

    tk.Button(root, text="Executar", command=on_run, bg="green", fg="white").pack(pady=5)
    tk.Button(root, text="Abortar", command=on_abort, bg="red", fg="white").pack()

    root.mainloop()

if __name__ == "__main__":
    criar_interface()
