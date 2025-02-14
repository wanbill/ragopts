from typing import Any, Dict, List
from abc import ABC


class BaseConfig(ABC):
    def __init__(self, file_path: str) -> None:
        super().__init__()
        self.file_path = file_path
        self.config: Dict[str, Any] = dict()
        
    def load(self) -> None:
        raise NotImplementedError
    
    def save(self) -> None:
        raise NotImplementedError
    
    def get(self, key: str, default: Any = None) -> Any:
        return self.config.get(key, default)
    
    def __getitem__(self, key: str) -> Any:
        return self.config.get(key, None)
    
    def __getattr__(self, name: str) -> Any:
        config = getattr(self, "config")
        if name in config:
            return config[name]
        return self.__dict__.get(name, None)