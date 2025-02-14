from abc import ABC
from .node import Node
from enum import Enum

class EdgeType(Enum):
    Logical = 0
    Sementic = 1
    PossibleRelation = 2

class Edge(ABC):
    def __init__(self, src: Node, trg: Node, reason: str, edge_type: EdgeType) -> None:
        super().__init__()
        self.src = src
        self.trg = trg
        self.reason = reason
        self.edge_type = edge_type
        
    def __str__(self) -> str:
        return f"Edge from {self.src.title} -> {self.trg.title} with reason: {self.reason}, Node value: {self.trg.value}"

    