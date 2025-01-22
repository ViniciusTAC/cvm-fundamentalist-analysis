import zipfile
import os
import requests
from datetime import datetime
from bs4 import BeautifulSoup
import logging
from collectors.coletor_cvm import Coletor_cvm  # Importa a classe Coletor_cvm
from utils.logger import escrever_linha_em_branco, escrever_linha_separador
from extractor.extrator import extrair_arquivo_zip  # Função de extração

class Coletor:
    def __init__(self, base_dir="data", extracted_dir="data_extraido"):
        self.base_dir = os.path.join(os.getcwd(), base_dir)
        self.extracted_dir = os.path.join(os.getcwd(), extracted_dir)
        self.logger = self._setup_logger()
        self.DATA_URLS = self._get_data_urls()

    def _get_data_urls(self):
        data_types = ["FCA", "DFP", "ITR", "FRE", "IPE"]
        return dict(zip(data_types, Coletor_cvm.links_cvm))

    def _setup_logger(self):
        os.makedirs("logs", exist_ok=True)
        log_filename = f"logs/{datetime.now().strftime('%Y-%m-%d')}.log"
        logging.basicConfig(
            level=logging.INFO,
            format="%(asctime)s - %(levelname)s - %(message)s",
            handlers=[
                logging.FileHandler(log_filename, encoding="utf-8"),
                logging.StreamHandler()
            ]
        )
        return logging.getLogger(__name__)

    def create_directory(self, path):
        if not os.path.exists(path):
            os.makedirs(path)

    def download_file(self, url, dest):
        try:
            response = requests.get(url, stream=True)
            response.raise_for_status()

            filename = os.path.basename(url)
            filepath = os.path.join(dest, filename)

            with open(filepath, "wb") as file:
                for chunk in response.iter_content(chunk_size=8192):
                    file.write(chunk)

            self.logger.info(f"Arquivo salvo em: {filepath}")
            return filepath  # Retorna o caminho do arquivo baixado
        except requests.RequestException as e:
            self.logger.error(f"Erro ao baixar {url}: {e}")
            return None

    def get_files_from_url(self, base_url):
        try:
            response = requests.get(base_url)
            response.raise_for_status()

            soup = BeautifulSoup(response.text, "html.parser")
            files = [a["href"] for a in soup.find_all("a") if a["href"].endswith(".zip")]
            return files
        except requests.RequestException as e:
            self.logger.error(f"Erro ao acessar {base_url}: {e}")
            return []

    def collect_data(self):
        today = datetime.today().strftime("%Y-%m-%d")

        for data_type, base_url in self.DATA_URLS.items():
            escrever_linha_em_branco()
            escrever_linha_separador()
            escrever_linha_em_branco()
            self.logger.info(f"Iniciando download dos dados do tipo: {data_type}")
            download_dir = os.path.join(self.base_dir, data_type, today)
            extract_dir = os.path.join(self.extracted_dir, data_type)  # Diretório para arquivos extraídos
            self.create_directory(download_dir)
            self.create_directory(extract_dir)

            files = self.get_files_from_url(base_url)

            if not files:
                self.logger.warning(f"Nenhum arquivo encontrado para {data_type} em {base_url}")
                continue

            # Realiza o download de todos os arquivos ZIP
            zip_paths = []
            for file in files:
                file_url = f"{base_url}{file}"
                zip_path = self.download_file(file_url, download_dir)
                if zip_path:
                    zip_paths.append(zip_path)

            # Após o download, realiza a extração dos arquivos ZIP
            escrever_linha_em_branco()
            self.logger.info(f"Iniciando extração dos arquivos baixados de {data_type}")
            for zip_path in zip_paths:
                try:
                    self.logger.info(f"Extraindo {zip_path}")
                    extrair_arquivo_zip(zip_path, extract_dir)  # Extrai para o diretório por tipo
                    self.logger.info(f"Extração concluída: {zip_path}")
                except zipfile.BadZipFile:
                    self.logger.error(f"Erro: O arquivo {zip_path} está corrompido.")
        
        escrever_linha_em_branco()
        self.logger.info("Coleta e extração de dados concluídas.")
