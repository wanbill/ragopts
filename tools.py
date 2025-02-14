from gptfunction import gptfunction
import math
import numpy as np
from typing import Any
from glob import graph

@gptfunction
def add(a: str, b: str) -> int:
    """
    add two numbers.

    :param a: first number.
    :param b: second number
    """
    return int(a) + int(b)

@gptfunction
def run_python(code: str) -> Any:
    """
    Run python code using `exec`.  The content in local variable 'ans' will be returned, so you MUST put what you need to be returned in varible `ans`.

    :param code: python code you wanna run.
    :return: The value of the variable 'ans' after executing the code.
    """
    try:
        local_vars = dict()
        exec(code, {"math": math, "np": np}, local_vars)
        return local_vars.get("ans", None)
    except Exception as e:
        raise e
        return str(e)
    
@gptfunction
def retrieve_table(key_word: str) -> str:
    """
    Retrive rows from table.

    :param key_word: key word to search.
    """
    global graph
    return str(
        graph.search_in_graph(key_word)
    )
    