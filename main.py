from src.text_summarization_transformers.logging import logger
from src.text_summarization_transformers.pipeline.stage_1_data_ingestion_pipeline import DataIngestionTrainingPipeline
from src.text_summarization_transformers.pipeline.stage_2_data_transformation_pipeline import DataTransformationTrainingPipeline

STAGE_NAME = "Data Ingestion Stage"

try:
    logger.info(f"stage {STAGE_NAME} initiated")
    data_ingestion_pipeline = DataIngestionTrainingPipeline()
    data_ingestion_pipeline.initiate_data_ingestion()
    logger.info(f">>>>> stage {STAGE_NAME} completed!<<<<<\n\nx==========x")

except Exception as e:
    logger.error(f"Error occurred in stage {STAGE_NAME}: {e}")
    raise e


STAGE_NAME = "Data Transformation Stage"

try:
    logger.info(f"stage {STAGE_NAME} initiated")
    data_transformation_pipeline = DataTransformationTrainingPipeline()
    data_transformation_pipeline.initiate_data_transformation()
    logger.info(f">>>>> stage {STAGE_NAME} completed!<<<<<\n\nx==========x")

except Exception as e:
    logger.error(f"Error occurred in stage {STAGE_NAME}: {e}")
    raise e

