from src.text_summarization_transformers.config.configuration import ConfiguartionManager
from src.text_summarization_transformers.components.data_transformation import DataTransformation
from src.text_summarization_transformers.logging import logger

class DataTransformationTrainingPipeline:
    def __init__(self):
        pass

    def initiate_data_transformation(self):
        config = ConfiguartionManager()
        data_transformation_config = config.get_data_transformation_config()
        data_transformation = DataTransformation(config=data_transformation_config)
        data_transformation.convert()