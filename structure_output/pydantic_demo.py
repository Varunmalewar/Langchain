from pydantic import BaseModel,EmailStr, Field
from typing import Optional

class Student(BaseModel):
    name : str
    age : Optional[int] = 22
    email : EmailStr
    cgpa : float = Field(gt=0, lt=10, description="CGPA must be between 0 and 10",default = 7)

new_student = {'name' : 'Varun', 'email' : 'abc@gmail.com'}

student = Student(**new_student)

print(student)
print(type(student))
student_dict = dict(student)
print(student_dict['age'])

student_json = student.model_dump_json()
print(student_json)