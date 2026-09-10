from langchain_core.tools import tool

#custom tools

@tool
def multiply(a: int, b:int) ->int :
    """Multiply a and b """
    return a * b

@tool
def add(a: int, b:int) ->int :
    """Add a and b """
    return a + b

class MathToolkit :
    def get_tools(self) :
        return [multiply, add]

toolkit = MathToolkit()
tools = toolkit.get_tools()

for tool in tools :
    print(f"Tool Name : {tool.name}")
    print(f"Tool Description : {tool.description}")
    print(f"Tool Args : {tool.args}")
    print(f"Tool Args Schema : {tool.args_schema.model_json_schema()}")
    