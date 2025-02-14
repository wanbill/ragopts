from typing import Any, Dict, List, Union, Generator
from abc import ABC
from enum import Enum



class OutputType(Enum):
    Normal = 0
    Stream = 1
    KeepStream = 2

class AgentType(Enum):
    Tool = 0
    Agent = 1



class BaseAgent(ABC):
    def __init__(self, agent_type: AgentType, name: str = "") -> None:
        super().__init__()
        self._stream: OutputType = OutputType.Normal
        self.agent_type: AgentType = agent_type
        self.name: str = name
    
    def completion(self) -> Union[str, Generator]:
        pass

    def __call__(self, *args, **kwargs) -> Any:
        pass

    def stream(self, keep: bool = False) -> "BaseAgent":
        self._stream = OutputType.KeepStream if keep else OutputType.Stream
        return self
