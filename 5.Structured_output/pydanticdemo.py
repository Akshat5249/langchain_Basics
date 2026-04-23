from pydantic import BaseModel



class student(BaseModel):
    name : str

new_student = {'name':'akshat'}

student = student(**new_student)

print(type(student))