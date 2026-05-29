from src.text_summarization_transformers.config.configuration import ConfiguartionManager
from src.text_summarization_transformers.components.data_ingestion import DataIngestion
from src.text_summarization_transformers.logging import logger

class DataIngestionTrainingPipeline:
    def __init__(self):
        self.config = ConfiguartionManager()
        self.data_ingestion_config = self.config.get_data_ingestion_config()
        self.data_ingestion = DataIngestion(config=self.data_ingestion_config)

    def initiate_data_ingestion(self):
        config = ConfiguartionManager()
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = DataIngestion(config=data_ingestion_config)

        data_ingestion.download_file()
        data_ingestion.extract_zip_file()