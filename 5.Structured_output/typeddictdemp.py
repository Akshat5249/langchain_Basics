from typing import TypedDict

class Person(TypedDict):
    name:str
    age:int

new_per : Person = {'name':'nitish','age':18}

print(new_per)