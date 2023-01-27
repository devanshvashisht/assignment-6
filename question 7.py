class Student:
    pass

class Marks:
    pass

devansh=Student()

devansh_s_marks=Marks()

print("devansh is an instance of class Student:",isinstance(devansh,Student))
print("devansh is an instance of class Marks:",isinstance(devansh,Marks))
print("devansh_s_marks is an instance of class Student:",isinstance(devansh_s_marks,Student))
print("devansh_s_marks is an instance of class Marks:",isinstance(devansh_s_marks,Marks))

print("Student is a subclass of class object:",issubclass(Student,object))
print("Marks is a subclass of class object:",issubclass(Marks,object))