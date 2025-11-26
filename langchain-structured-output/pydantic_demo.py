from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class Student(BaseModel):
    name: str = "Default"
    age : Optional[int] = None
    email : EmailStr
    cgpa : float = Field(..., ge=0.0, le=4.0, description="CGPA must be between 0.0 and 4.0")   

st = {"name": "Masumi",'age':'29', 'email':'tbd@gmail.com', 'cgpa':3.8}
student =  Student(**st)

dictionary = student.__dict__
json = student.json()
print(dictionary['email'])
print(json)
