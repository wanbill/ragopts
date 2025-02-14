from vectordb import Chroma
from chromadb.utils import embedding_functions
import os
os.environ ["OPENAI_API_KEY"] = "sk-"
import chromadb
from config import YAMLConfig
from parser import TableParser
from agent import AgentWU
from tools import *

# global GRAPH
# from agent.agent_wu import add

if __name__ == '__main__':
    # print(run_python.schema()['function'])
    # embd = embedding_functions.DefaultEmbeddingFunction()
    # exit(0)
    # client = chromadb.PersistentClient(path="data")
    # db = Chroma(client=client, embedding_function=embd, persist_directory='data')
    # db.add_texts(["Hello, World!"], [{}])
    # print(db.similarity_search_with_score("Hello, World!", k=1))
    conf = YAMLConfig(file_path="data/main.yaml")
    conf.load()
    
    # parser = TableParser()
    # graph = parser.from_file("raw_data/AAPL_balance_sheet.json")
    # GRAPH = graph

    # print(conf.config)
    # print(conf)
    # print(conf.config)
    # print(conf.name)

    
    # globals()["graph"] = graph
    # for i in retrieve_table("share issued"):
    #     print(i)
    # print("\n"*5)
    # for i in graph.edges:
    #     print(i)
    # print("\n"*5)
    # for i in graph.search_in_graph("Share Issued"):
    #     print(i)
    # exit(0)

    
    my_agent = AgentWU(config=conf)
    my_agent.stream(keep=True)
    
    
    while True:
        user_input = input("User: ")
        if user_input == "exit":
            break
        for i in my_agent.completion(user_input):
            print(i, end='',flush=True)
        print("")
        my_agent.process()
        # print(my_agent.history)
        # input()
        while isinstance(my_agent.history[-1], dict) and my_agent.history[-1]["role"] == "function":
            print(f"Function Call: {my_agent.history[-1]['name']} -> {my_agent.history[-1]['content']}")
            for i in my_agent.completion(""):
                print(i, end='',flush=True)
            print("")
            my_agent.process()          


    print(my_agent.history)
        
# tell me the info for Share Issued in the table
# tell me the info for share issued in the table
# 预测接下来几年的数据