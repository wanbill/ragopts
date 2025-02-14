from typing import Any, Dict, List, Generator
from abc import ABC

class BaseLLM(ABC):
    def __init__(self) -> None:
        super().__init__()

    def completion(self, *args, **kwargs) -> str:
        raise NotImplementedError
    
    def stream(self, *args, **kwargs) -> Generator:
        raise NotImplementedError

