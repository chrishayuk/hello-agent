from llama_index.core.tools import FunctionTool
from pydantic import BaseModel, Field
from wasmtime import Store, Module, Instance


class SquareParams(BaseModel):
    a: int = Field(...,description="The integer to be squared")

store=Store()
module=Module.from_file(store.engine, './tools/math.wat')
instance=Instance(store,module,[])
square_fn = instance.exports(store)['square']

square_tool = FunctionTool.from_defaults(fn=lambda a: square_fn(store, a), name="square_tool", description="calculates and returns the square of an integer")