import logging
from datetime import datetime
import os

# Garante que a pasta 'logs' exista
os.makedirs("logs", exist_ok=True)

# Define o nome do arquivo com base na data atual
log_filename = f"logs/{datetime.now().strftime('%Y-%m-%d')}.log"

# Criação do FileHandler com codificação UTF-8
file_handler = logging.FileHandler(log_filename, encoding="utf-8")

# Configuração do formato de log
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
file_handler.setFormatter(formatter)

# Configuração do logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
logger.addHandler(file_handler)

# Adiciona um StreamHandler para exibir no console
console_handler = logging.StreamHandler()
console_handler.setFormatter(formatter)
logger.addHandler(console_handler)

# Exemplos de mensagens de log
# Log de inicialização do sistema

# logger.handlers[0].stream.write("\n")  # Escreve uma linha em branco diretamente no arquivo ou console
# logger.info("=== Sistema iniciado ===")
# logger.debug("Este é um log de depuração (não aparecerá porque o nível é INFO).")
# logger.info("Esta é uma mensagem informativa.")
# logger.warning("Este é um aviso.")
# logger.error("Este é um erro.")
# logger.critical("Mensagem de falha crítica.")

def escrever_linha_em_branco():
    """Escreve uma linha em branco no stream do handler do arquivo."""
    for handler in logger.handlers:
        if isinstance(handler, logging.FileHandler):  # Apenas para FileHandler
            handler.stream.write("\n")
            handler.stream.flush()  # Garante que a linha seja gravada no arquivo

def escrever_linha_separador():
    """Escreve uma linha de separador (------------------)."""
    for handler in logger.handlers:
        if isinstance(handler, logging.FileHandler):  # Apenas para FileHandler
            handler.stream.write("------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
            handler.stream.flush()  # Garante que a linha seja gravada no arquivo