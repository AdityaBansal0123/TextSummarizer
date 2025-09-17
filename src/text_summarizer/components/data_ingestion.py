import os
import urllib.request as request
import zipfile
from src.text_summarizer.logging import logger
from src.text_summarizer.entity.config_entity import DataIngestionConfig

class DataIngestion:
    def __init__(self,config: DataIngestionConfig):
        self.config = config

    def download_file(self):
        try:
            if not os.path.exists(self.config.local_data_file):
                logger.info(f"Downloading file from {self.config.source_URL}...")
                request.urlretrieve(self.config.source_URL, self.config.local_data_file)
                logger.info("Download completed.")
            else:
                logger.info("File already exists.")
        except Exception as e:
            logger.error(f"Error occurred while downloading file: {e}")

    def extract_zip_file(self):
        try:
            logger.info(f"Extracting zip file {self.config.local_data_file}...")
            with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
                zip_ref.extractall(self.config.unzip_dir)
            logger.info("Extraction completed.")
        except Exception as e:
            logger.error(f"Error occurred while extracting file: {e}")