from abc import ABC
from typing import Dict, Any, List, Optional, Union
from .edge import Edge, EdgeType
from .node import Node
from vectordb import Chroma

class Graph(ABC):
    def __init__(self, title: str, description: str) -> None:
        super().__init__()
        self.title = title
        self.description = description
        self.edges: List[Edge] = []
        self.nodes: List[Node] = []
        self.title2node: Dict[str, Node] = dict()
        self.vector_db = None

    def add_node(self, node: Node) -> None:
        self.nodes.append(node)
        self.title2node[node.title] = node

    def get_node(self, title: str) -> Optional[Node]:
        return self.title2node.get(title, None)
    
    def add_edge(self, src: str, trg: str, reason: str, edge_type: EdgeType) -> None:
        src, trg = self.get_node(src), self.get_node(trg)
        assert all([src, trg]), f"Src: {src}, Trg: {trg}"
        print(f"Adding edge from | {src.title} -> {trg.title} | with reason: {reason}")

        self.edges.append(Edge(src, trg, reason, edge_type))

    def get_connections(self, node: Union[Node, str]) -> List[Edge]:
        title = node.title if isinstance(node, Node) else node
        return [i for i in self.edges if i.src.title == title]
    
    def add_sementic_edges(self, vectordb: Chroma, top_k: int = 3, threshold: float = 1) -> "Graph":
        self.vector_db = vectordb
        # data, metadata = list(self.title2node.keys()), [{"title":0}] * len(self.title2node)
        # data = vectordb.add_texts(data, metadata)
        top_k = int(1e9) if top_k < 0 else top_k
        threshold = 1e9 if threshold < 0 else threshold
        assert top_k != 0 and threshold != 0, f"Top_k: {top_k}, Threshold: {threshold}"
        for i in self.title2node:
            tmp = vectordb.similarity_search_with_score(i, k= top_k + 1)[1:]
            for document, score in tmp:
                if score >= threshold and document.page_content in self.title2node:
                    self.add_edge(i, document.page_content, "Semantic Similarity", EdgeType.Sementic)
        return self
        
    def add_llm_edges(self, agent, top_k: int = 3, threshold: float = 1) -> "Graph":
        pass
        # data = list(self.title2node.keys())
        # top_k = int(1e9) if top_k < 0 else top_k
        # threshold = 1e9 if threshold < 0 else threshold
        # assert top_k != 0 and threshold != 0, f"Top_k: {top_k}, Threshold: {threshold}"
        # for i in self.title2node:
        #     tmp = agent(i, top_k + 1)[1:]
        #     for document, score in tmp:
        #         if score >= threshold and document in self.title2node:
        #             self.add_edge(i, document, "LLM Similarity", EdgeType.LLM)
        # return self

    def search_in_graph(self, query: str) -> List[str]:
        query = query.lower()
        node = self.get_node(query)
        if node is None:
            node_name = self.vector_db.similarity_search(query, k=1)[0].page_content
            node = self.get_node(node_name)
        ans = [str(node)]
        # print(self.get_connections(node))
        ans.extend(list(map(str, self.get_connections(node))))
        # for i in ans:
        #     print(i)
        return ans
        
        