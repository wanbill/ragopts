from typing import Any, Dict, List
from .base_config import BaseConfig
from pathlib import Path
import yaml
from .loader import Loader



class YAMLConfig(BaseConfig):
    def __init__(self, file_path: str) -> None:
        super().__init__(file_path)
        tmp = Path(self.file_path)
        if tmp.suffix != ".yaml":
            raise ValueError("File must be a YAML file.")
        if not tmp.exists():
            raise FileNotFoundError("File does not exist.")
        
    def load(self) -> None:
        with open(self.file_path, "r") as file:
            self.config = yaml.load(file, Loader=Loader)
    
    def save(self) -> None:
        with open(self.file_path, "w") as file:
            yaml.dump(self.config, file)