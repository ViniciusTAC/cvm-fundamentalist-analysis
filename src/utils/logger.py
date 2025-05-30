import logging
from datetime import datetime
import os


def configurar_logger(nivel=logging.INFO):
    """Configura e retorna um logger com FileHandler e StreamHandler."""
    log_dir = os.path.join(os.getcwd(), "logs")
    os.makedirs(log_dir, exist_ok=True)

    log_filename = f"{log_dir}/{datetime.now().strftime('%Y-%m-%d')}.log"

    formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")

    logger = logging.getLogger("cvm_logger")
    logger.setLevel(nivel)

    # Evita adicionar múltiplos handlers
    if not logger.handlers:
        file_handler = logging.FileHandler(log_filename, encoding="utf-8")
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)

    return logger


def escrever_linha_em_branco(logger, nivel=logging.INFO):
    """Escreve uma linha em branco apenas se o nível estiver habilitado."""
    if nivel == logging.INFO and logger.isEnabledFor(logging.INFO):
        logger.log(nivel, "")


def escrever_linha_separador(logger, caractere="-", comprimento=80, nivel=logging.INFO):
    """Escreve uma linha de separador apenas se o nível estiver habilitado."""
    if nivel == logging.INFO and logger.isEnabledFor(logging.INFO):
        separador = caractere * comprimento
        logger.log(nivel, separador)
