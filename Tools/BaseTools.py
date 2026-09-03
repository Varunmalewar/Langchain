from langchain_community.tools import BaseTool
from openai import BaseModel
from pydantic import BaseModel , Field
from typing import Type

#arg schema using pydantic 
class MultiplyInput(BaseModel):
    a: int = Field(..., description="The first number to multiply")
    b: int = Field(..., description="The second number to multiply")

class MultiplyTool(BaseTool):
    name: str = "multiply"
    description : str = "Multiply two numbers"

    args_schema : Type[BaseModel] = MultiplyInput

    def _run(self, a: int, b:int) -> int:
        """Multiply a and b """
        return a * b

multiply_tool = MultiplyTool()

result = multiply_tool.invoke({"a": 5, "b": 10})
print(result)