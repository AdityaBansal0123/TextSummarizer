from src.text_summarizer.constants import *
from src.text_summarizer.entity.config_entity import DataIngestionConfig,DataTransformationConfig,ModelTrainerConfig,ModelEvaluationConfig
from src.text_summarizer.utils.common import read_yaml, create_directories

class ConfigurationManager:
    def __init__(self,
                config_path=CONFIG_FILE_PATH,
                params_filepath=PARAMS_FILE_PATH):
        self.config = read_yaml(str(config_path))
        self.params = read_yaml(str(params_filepath))
        create_directories([self.config.artifacts_root])

    def get_data_ingestion_config(self)->DataIngestionConfig:
        config = self.config.data_ingestion
        create_directories([config.root_dir])

        data_ingestion_config = DataIngestionConfig(
            root_dir = config.root_dir,
            source_URL = config.source_URL,
            local_data_file = config.local_data_file,
            unzip_dir = config.unzip_dir
        )
        return data_ingestion_config
    
    def get_data_transformation_config(self)->DataTransformationConfig:
        config = self.config.data_transformation
        create_directories([config.root_dir])

        data_transformation_config = DataTransformationConfig(
            root_dir = config.root_dir,
            data_path = config.data_path,
            tokenizer_name = config.tokenizer_name
        )
        return data_transformation_config

    def get_model_trainer_config(self) -> ModelTrainerConfig:
        config = self.config.model_trainer
        params = self.params.model_trainer
        create_directories([config.root_dir])

        model_trainer_config = ModelTrainerConfig(
            root_dir = config.root_dir,
            model_ckpt = config.model_ckpt,
            data_path = config.data_path,
            num_train_epochs = params.num_train_epochs,
            warmup_steps = params.warmup_steps,
            per_device_train_batch_size = params.per_device_train_batch_size,
            weight_decay = params.weight_decay,
            logging_steps = params.logging_steps,
            evaluation_strategy = params.evaluation_strategy,
            eval_steps = params.eval_steps,
            save_steps = params.save_steps,
            gradient_accumulation_steps = params.gradient_accumulation_steps
        )
        return model_trainer_config
    
    def get_model_evaluation_config(self)-> ModelEvaluationConfig:
        config = self.config.model_evaluation
        create_directories([config.root_dir])

        model_evaluation_config = ModelEvaluationConfig(
            root_dir = config.root_dir,
            data_path = config.data_path,
            model_path= config.model_path,
            metric_file_name = config.metric_file_name
        )
        return model_evaluation_config