#importing dataclass
from dataclasses import dataclass

#using the dataclass decorator
@dataclass

#creating class student
class Student:

    #listing the variables and their datatypes
    name:str
    college_id: int
    GPA: float

def main():
    #adding  students with their name, id and gpa
    ahmed = Student('Ahmed', 768903, 3.5)
    ali = Student('Ali', 234156, 2.0)
    john = Student('John', 167209, 2.85)
    jane = Student('Jane',509127, 4.0)
    alisha = Student('Alisha', 309217, 3.85 )


    print(ahmed)
    print(ali)
    print(john)
    print(jane)
    print(alisha)

main()    


