from src.text_summarizer.logging import logger
from src.text_summarizer.pipeline.data_ingestion_pipeline import DataIngestionTrainingPipeline
from src.text_summarizer.pipeline.data_transformation_pipeline import DataTransformationPipeline
from src.text_summarizer.pipeline.model_trainer_pipeline import ModelTrainerTrainingPipeline
from src.text_summarizer.pipeline.model_evaluation_pipeline import ModelEvaluationPipeline

STAGE_NAME = "Data Ingestion Stage"

try:
    logger.info(f"{STAGE_NAME} started")
    obj = DataIngestionTrainingPipeline()
    obj.initiate_data_ingestion()
    logger.info(f"{STAGE_NAME} completed")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Data Transformation Stage"

try:
    logger.info(f"{STAGE_NAME} started")
    obj = DataTransformationPipeline()
    obj.initiate_data_transformation()
    logger.info(f"{STAGE_NAME} completed")
except Exception as e:
    logger.exception(e)
    raise e

# STAGE_NAME = "Model Trainer Stage"

# try:
#     logger.info(f"{STAGE_NAME} started")
#     obj = ModelTrainerTrainingPipeline()
#     obj.initiate_model_trainer()
#     logger.info(f"{STAGE_NAME} completed")
# except Exception as e:
#     logger.exception(e)
#     raise e

STAGE_NAME = "Model Evaluation Stage"

try:
    logger.info(f"{STAGE_NAME} started")
    obj = ModelEvaluationPipeline()
    obj.initiate_model_evaluation()
    logger.info(f"{STAGE_NAME} completed")
except Exception as e:
    logger.exception(e)
    raise e