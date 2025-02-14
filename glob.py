from parser.table_parser import TableParser
from vectordb import Chroma
from chromadb.utils import embedding_functions
import chromadb
import pickle
from pathlib import Path

global graph


f = Path("data/graph.pkl")
embd = embedding_functions.DefaultEmbeddingFunction()
client = chromadb.PersistentClient(path="data")
db = Chroma(client=client, embedding_function=embd, persist_directory='data')
if f.exists():
    graph = pickle.load(open("data/graph.pkl", "rb"))
    graph.vector_db = db
else:
    parser = TableParser()
    graph = parser.from_file("raw_data/AAPL_balance_sheet.json")
    graph.add_sementic_edges(db, top_k=3, threshold=0.1)
    graph.vector_db = None
    pickle.dump(graph, open("data/graph.pkl", "wb"))
    graph.vector_db = db

