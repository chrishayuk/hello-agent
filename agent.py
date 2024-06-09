from dotenv import load_dotenv

from llama_index.agent.openai import OpenAIAgent
from llama_index.llms.openai import OpenAI

from tools.add_tool import add_tool
from tools.multiply_tool import multiply_tool
from tools.square_tool import square_tool
from tools.dynamic_tool import get_tool_by_name

load_dotenv()

from llama_index.core import VectorStoreIndex, SimpleDirectoryReader
documents = SimpleDirectoryReader("data").load_data()
index = VectorStoreIndex.from_documents(documents)

query = "25 added to 7"
query_engine = index.as_query_engine()
response = query_engine.query(f"give a list of tools that i can use to satisfy this query: '{query}'\n just return the tool_names")
tool_name = str(response)

matched_tool = get_tool_by_name(tool_name)

llm = OpenAI(model="gpt-4o")

agent = OpenAIAgent.from_tools([matched_tool], llm=llm, verbose=True)

response = agent.chat(query)
print(response)