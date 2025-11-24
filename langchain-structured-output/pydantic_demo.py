from pydantic import BaseModel

class Student(BaseModel):
    name: str

st = {"name": "Bob"}
student =  Student(**st)
print(student)
