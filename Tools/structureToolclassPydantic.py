from langchain_community.tools import StructuredTool
from pydantic import BaseModel , Field

class MultiplyInput(BaseModel):
    a: int = Field(..., description="The first number to multiply")
    b: int = Field(..., description="The second number to multiply")


def multiply(a: int, b:int) ->int :
    """Multiply a and b """
    return a * b



multiply_tool = StructuredTool.from_function(
    func = multiply,
    name = "multiply",
    description = "Multiply two numbers",
    args_schema = MultiplyInput
)

results = multiply_tool.invoke({"a": 5, "b": 10})
print(results)
print(multiply_tool.name)
print(multiply_tool.description)
print(multiply_tool.args_schema)
