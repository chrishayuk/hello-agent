from llama_index.core.tools import FunctionTool

def add(a:int, b:int) -> int:
    """ Add two integers and the result integer"""
    return a + b

add_tool = FunctionTool.from_defaults(fn=add)