class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print(f"Name: {self.name}")
        print(f"Marks: {self.marks}")

    def is_pass(self):
        return self.marks >= 40


# Creating object
s1 = Student("Aastha", 85)

s1.display()

if s1.is_pass():
    print("Result: Pass")
else:
    print("Result: Fail")