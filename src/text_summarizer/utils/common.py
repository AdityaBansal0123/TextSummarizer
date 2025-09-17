import os
from box.exceptions import BoxValueError
import yaml
from src.text_summarizer.logging import logger
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any

import os
import yaml
from src.text_summarizer.logging import logger
import json 
import joblib
from ensure import ensure_annotations
from box import Box, ConfigBox
from pathlib import Path
from typing import Any
from box.exceptions import BoxValueError

@ensure_annotations
def read_yaml(path_to_yaml: str) -> ConfigBox:
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
        
    except BoxValueError as e:
        raise ValueError(f"Error in reading yaml file: {path_to_yaml}. Error: {e}")
    except Exception as e:
        raise e
    
@ensure_annotations    
def create_directories(path_to_directories: list, verbose=True):
    """
    Create directories if they do not exist.
    """
    for dir_path in path_to_directories:
        os.makedirs(dir_path, exist_ok=True)
        if verbose:
            logger.info(f"Directory created: {dir_path}")
        
@ensure_annotations
def save_json(path: Path, data: dict):   
    with open(path, 'w') as f:
        json.dump(data,f,indent=4)
    logger.info(f"JSON file saved at: {path}")

@ensure_annotations
def load_json(path: Path) -> ConfigBox:
    with open(path) as f:
        content = json.load(f)
    logger.info(f"JSON file loaded from: {path}")
    return ConfigBox(content)     

@ensure_annotations
def save_model(data: Any, path: Path):
    joblib.dump(value=data, filename=path)
    logger.info(f"Model saved at: {path}")

@ensure_annotations
def load_model(path: Path)->Any:
    data = joblib.load(path)
    logger.info(f"Model loaded from: {path}")
    return data