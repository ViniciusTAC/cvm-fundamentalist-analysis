import zipfile
import os
import requests
from datetime import datetime
from bs4 import BeautifulSoup
import logging
from collectors.coletor_cvm import Coletor_cvm
from utils.logger import escrever_linha_em_branco, escrever_linha_separador
from extractor.extrator import extrair_arquivo_zip


class Coletor:
    def __init__(
        self,
        base_dir="data",
        extracted_dir="data_extraido",
        log_dir="logs",
        nivel=logging.INFO,
    ):
        self.base_dir = os.path.join(os.getcwd(), base_dir)
        self.extracted_dir = os.path.join(os.getcwd(), extracted_dir)
        self.log_download_dir = os.path.join(os.getcwd(), log_dir, "logs_download")
        self.log_extraction_dir = os.path.join(os.getcwd(), log_dir, "logs_extracao")
        self.DATA_URLS = self._get_data_urls()
        self.nivel_log = nivel

        # Cria os diretórios principais
        self.create_directory(self.base_dir)
        self.create_directory(self.extracted_dir)
        self.create_directory(self.log_download_dir)
        self.create_directory(self.log_extraction_dir)

    def _get_data_urls(self):
        data_types = ["FCA", "DFP", "ITR", "FRE", "IPE"]
        return dict(zip(data_types, Coletor_cvm.links_cvm))

    def _setup_logger(self, log_dir, log_type="download", nivel=logging.INFO):
        today = datetime.now().strftime("%Y-%m-%d")
        log_data_dir = os.path.join(log_dir, today)

        self.create_directory(log_data_dir)

        formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")

        sucesso_logger = logging.getLogger(f"{log_type}_sucesso")
        sucesso_logger.setLevel(nivel)
        if not sucesso_logger.handlers:
            sucesso_handler = logging.FileHandler(
                os.path.join(log_data_dir, "sucesso.log"), encoding="utf-8"
            )
            sucesso_handler.setFormatter(formatter)
            sucesso_logger.addHandler(sucesso_handler)

        erro_logger = logging.getLogger(f"{log_type}_erro")
        erro_logger.setLevel(nivel)
        if not erro_logger.handlers:
            erro_handler = logging.FileHandler(
                os.path.join(log_data_dir, "erro.log"), encoding="utf-8"
            )
            erro_handler.setFormatter(formatter)
            erro_logger.addHandler(erro_handler)

        return sucesso_logger, erro_logger

    def create_directory(self, path):
        if not os.path.exists(path):
            os.makedirs(path)

    def download_file(self, url, dest, sucesso_logger, erro_logger):
        try:
            response = requests.get(url, stream=True)
            response.raise_for_status()

            filename = os.path.basename(url)
            filepath = os.path.join(dest, filename)

            with open(filepath, "wb") as file:
                for chunk in response.iter_content(chunk_size=8192):
                    file.write(chunk)

            sucesso_logger.info(f"Download realizado com sucesso: {filepath}")
            return filepath
        except requests.RequestException as e:
            erro_logger.error(f"Erro ao baixar {url}: {e}")
            return None

    def get_files_from_url(self, base_url, erro_logger):
        try:
            response = requests.get(base_url)
            response.raise_for_status()

            soup = BeautifulSoup(response.text, "html.parser")
            files = [
                a["href"] for a in soup.find_all("a") if a["href"].endswith(".zip")
            ]
            return files
        except requests.RequestException as e:
            erro_logger.error(f"Erro ao acessar {base_url}: {e}")
            return []

    def collect_data(self):
        today = datetime.today().strftime("%Y-%m-%d")

        for data_type, base_url in self.DATA_URLS.items():
            download_sucesso_logger, download_erro_logger = self._setup_logger(
                self.log_download_dir, "download", self.nivel_log
            )
            extracao_sucesso_logger, extracao_erro_logger = self._setup_logger(
                self.log_extraction_dir, "extracao", self.nivel_log
            )

            download_dir = os.path.join(self.base_dir, data_type, today)
            extract_success_dir = os.path.join(self.extracted_dir, data_type, "sucesso")
            extract_error_dir = os.path.join(self.extracted_dir, data_type, "erro")

            self.create_directory(download_dir)
            self.create_directory(extract_success_dir)
            self.create_directory(extract_error_dir)

            escrever_linha_em_branco(download_sucesso_logger)
            escrever_linha_separador(download_sucesso_logger, "-", 150)
            escrever_linha_em_branco(download_sucesso_logger)
            download_sucesso_logger.info(
                f"Iniciando download dos dados do tipo: {data_type}"
            )

            files = self.get_files_from_url(base_url, download_erro_logger)

            if not files:
                escrever_linha_em_branco(download_erro_logger)
                escrever_linha_separador(download_erro_logger)
                escrever_linha_em_branco(download_erro_logger)
                download_erro_logger.warning(
                    f"Nenhum arquivo encontrado para {data_type} em {base_url}"
                )
                continue

            zip_paths = []
            for file in files:
                file_url = f"{base_url}{file}"
                zip_path = self.download_file(
                    file_url,
                    download_dir,
                    download_sucesso_logger,
                    download_erro_logger,
                )
                if zip_path:
                    zip_paths.append(zip_path)

            escrever_linha_em_branco(extracao_sucesso_logger, nivel=self.nivel_log)
            escrever_linha_separador(extracao_sucesso_logger, "-", 150, nivel=self.nivel_log)
            escrever_linha_em_branco(extracao_sucesso_logger, nivel=self.nivel_log)
            extracao_sucesso_logger.info(
                f"Iniciando extração dos arquivos baixados de {data_type}"
            )

            for zip_path in zip_paths:
                try:
                    extracao_sucesso_logger.info(f"Extraindo {zip_path}")
                    extrair_arquivo_zip(zip_path, extract_success_dir)
                    extracao_sucesso_logger.info(f"Extração concluída: {zip_path}")
                except zipfile.BadZipFile:
                    escrever_linha_em_branco(extracao_erro_logger)
                    escrever_linha_separador(extracao_erro_logger, "-", 150)
                    escrever_linha_em_branco(extracao_erro_logger)
                    extracao_erro_logger.error(
                        f"Erro: O arquivo {zip_path} está corrompido."
                    )
                    errored_file_path = os.path.join(
                        extract_error_dir, os.path.basename(zip_path)
                    )
                    os.rename(zip_path, errored_file_path)
                    escrever_linha_em_branco(extracao_erro_logger)
                    escrever_linha_separador(extracao_erro_logger, "-", 150)
                    escrever_linha_em_branco(extracao_erro_logger)
                    extracao_erro_logger.info(
                        f"Arquivo movido para erro: {errored_file_path}"
                    )

        escrever_linha_em_branco(download_sucesso_logger)
        download_sucesso_logger.info("Download de dados concluído.")
        escrever_linha_em_branco(download_sucesso_logger)

        escrever_linha_em_branco(extracao_sucesso_logger, nivel=self.nivel_log)
        extracao_sucesso_logger.info("Extração de dados concluída.")
        escrever_linha_em_branco(extracao_sucesso_logger, nivel=self.nivel_log)
