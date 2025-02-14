from prompt import PromptTemplate
from config.base_config import BaseConfig
from llm import OpenAILLM
from .base import *
from .base import AgentType, OutputType
from openai.types.chat.chat_completion import ChatCompletionMessage
from typing import Union
import json
from .utils import json2dict
# __all__ = ["AgentWU"]



class AgentWU(BaseAgent):
    def __init__(self, config: BaseConfig, prompt: PromptTemplate = None, format_args: Dict[str, str] = dict()) -> None:
        super().__init__(agent_type=1, name=config.get("name", ""))
        self.config = config
        self._stream: OutputType = OutputType.Normal
        self.llm: OpenAILLM = OpenAILLM(
            config.get("default_config", dict()),
            config.get("client_config", dict())
            )
        self.history: List[Union[Dict[str, str]], ChatCompletionMessage] = []
        if (prompt := prompt or config.get("prompt", None)):
            self.history.append({"role": "system", "content": prompt.format(**format_args)})
        self.functions = {i['name'] : i['tool'] for i in config.get("tools", [])}
    
    def completion(self, inp: str) -> Union[str, Generator]:
        if inp:
            self.history.append({"role": "user", "content": inp})
        if self._stream == OutputType.Normal:
            resp: ChatCompletionMessage = self.llm.completion(
                messages=self.history,
                functions=[j.schema()['function'] for i, j in self.functions.items()]
            )
            self.history.append(resp)    
            return resp       
        else:
            if self.stream == OutputType.Stream:
                self.stream = OutputType.Normal
            self.history.append({"role": "assistant", "content": ""})
            return self.llm.stream(
                history=self.history,
                messages=self.history,
                functions=[j.schema()['function'] for i, j in self.functions.items()]
            )

    def process(self) -> Any:
        target = self.history[-1]
        # # print(target)
        # if isinstance(target, dict): # stream
        #     func = json2dict(target['content'])
        #     print(func)
        # else:
        if target.function_call:
            name, args = target.function_call.name, target.function_call.arguments
            func = self.functions.get(name, None)
            if func:
                try:
                    args = json2dict(args)
                    content = func(**args)
                    self.history.append({
                        "role": "function", 
                        "name": name,
                        "content": str(content),
                        })
                    return content
                except Exception as e:
                    self.history.append({
                        "role": "function", 
                        "name": name,
                        "content": str(e),
                        })
                    return e
            else:
                self.history.append({
                    "role": "user", 
                    "name": name,
                    "content": f"Function {name} not found",
                    })
                return f"Function {name} not found"
                
            
            
    
    def __call__(self, *args, **kwargs) -> Any:
        pass

    def stream(self, keep: bool = False) -> "BaseAgent":
        self._stream = OutputType.KeepStream if keep else OutputType.Stream
        return self
