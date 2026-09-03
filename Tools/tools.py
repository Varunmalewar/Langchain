from langchain_community.tools import DuckDuckGoSearchRun
from langchain_community.tools import ShellTool



# DUCKDUCKGO SEARCH TOOL
search_tool = DuckDuckGoSearchRun()

results = search_tool.invoke("who is age of abhishek sharma girlfriend? ")

print(results)



# Shell Tool 
shell_tool = ShellTool()
# results = shell_tool.invoke("whoami")
# print(results)



#Custom Tools 

#step 1: Define a function that performs the desired action

# def multiply(a,b) :
#     """Multiply a and b """
#     return a * b


# # Step 2 : add type hints
# def multiply(a: int, b:int) ->int :
#     """Multiply a and b """
#     return a * b

#step 3 : add tool decorator 
from langchain_core.tools import tool

@tool
def multiply(a: int, b:int) ->int :
    """Multiply a and b """
    return a * b

results = multiply.invoke({"a": 5, "b": 10})

# print(results)
# print(multiply.name)
# print(multiply.description)
# print(multiply.args)
# print(multiply.args_schema.model_json_schema())