from src.text_summarization_transformers.logging import logger
from src.text_summarization_transformers.pipeline.stage_1_data_ingestion_pipeline import DataIngestionTrainingPipeline


STAGE_NAME = "Data Ingestion Stage"

try:
    logger.info(f"stage {STAGE_NAME} initiated")
    data_ingestion_pipeline = DataIngestionTrainingPipeline()
    data_ingestion_pipeline.initiate_data_ingestion()
    logger.info(f">>>>> stage {STAGE_NAME} completed!<<<<<\n\nx==========x")

except Exception as e:
    logger.error(f"Error occurred in stage {STAGE_NAME}: {e}")
    raise e

