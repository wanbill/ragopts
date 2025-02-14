from typing import Dict, Union
# from .edge import Edge
from abc import ABC

class Node(ABC): # value -> dict if need more info, str for actual number in balance sheet
    def __init__(self, title: str, value: Union[Dict[str, str], str]) -> None:
        self.title = title.lower()
        self.value = value
        
    def __str__(self) -> str:
        return f"Node: {self.title} with value: {self.value}"
        