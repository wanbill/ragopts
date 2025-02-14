import json
from ast import literal_eval
from gptfunction import gptfunction


def json2dict(json_str: str) -> dict:
    json_str = json_str.strip()
    if not json_str.startswith("{"):
        json_str = "{" + json_str
    if not json_str.endswith("}"):
        json_str = json_str + "}"
    try:
        return json.loads(json_str)
    except json.JSONDecodeError:
        # print("json.JSONDecodeError")
        return literal_eval(json_str)
    except Exception as e:
        # print(e)
        return eval(json_str)
    # finally:
    #     return None