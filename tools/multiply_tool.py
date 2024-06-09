from llama_index.core.tools import FunctionTool

def multiply(a:int, b:int) -> int:
    """ Multiply two integers and the result integer"""
    return a * b

multiply_tool = FunctionTool.from_defaults(fn=multiply)