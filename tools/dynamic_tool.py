import json
from llama_index.core.tools import FunctionTool
from pydantic import BaseModel, Field, create_model
from wasmtime import Store, Module, Instance

store=Store()

with open("tools.json") as f:
    config = json.load(f)

def get_tool_by_name(name: str) -> FunctionTool:
    for tool_config in config["tools"]:
        if tool_config["name"] == name:
            module=Module.from_file(store.engine, tool_config["wasm_file"])
            instance=Instance(store,module,[])
            wasm_fn = instance.exports(store)[tool_config["exported_function"]]

            def tool_fn(a:int, b:int):
                return wasm_fn(store, a, b)
            
            # Create a dynamic Pydantic model for the parameters
            params = {param["name"]: (int, Field(..., description=param["description"])) for param in tool_config["params"]}
            DynamicParams = create_model(tool_config["name"] + "Params", **params)
            
            return FunctionTool.from_defaults(fn=tool_fn, description=tool_config.get("description",))