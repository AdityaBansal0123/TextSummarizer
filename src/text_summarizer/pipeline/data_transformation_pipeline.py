from src.text_summarizer.components.data_transformation import DataTransformation
from src.text_summarizer.config.configuration import ConfigurationManager


class DataTransformationPipeline:
    def __init__(self):
        pass

    def initiate_data_transformation(self):
        config = ConfigurationManager()
        data_transformation_config = config.get_data_transformation_config()
        data_transformation =DataTransformation(data_transformation_config)
        data_transformation.convert()