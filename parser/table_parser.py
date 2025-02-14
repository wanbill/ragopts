from .base_parser import BaseParser
from pathlib import Path
from typing import Dict, Any
import pandas as pd
import json
from datetime import datetime
from graph import Graph, Node, Edge



class TableParser(BaseParser):
    def __init__(self) -> None:
        super().__init__()

    def process(self, path: Path) -> Graph:
        with open(path, 'r') as f:
            data = json.load(f)
        # for i in data:
        #     print(i)
        data = {datetime.fromtimestamp(int(i) // 1000).strftime("%Y/%m") : j for i, j in data.items()}
        ans = {i : {} for i in list(data.values())[0].keys()}
        for i, j in data.items():
            for k, w in j.items():
                ans[k][i] = w
        graph = Graph("test", "test")
        nodes = [Node(i, j) for i, j in ans.items()]
        list(map(graph.add_node, nodes))
        return graph
        # print(graph.nodes)

        
    


        


