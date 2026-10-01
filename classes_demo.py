"""
Demo: Python classes for DS 2500
"""

# --- Defining a class ---
# a class is a blueprint for creating objects that bundle data (attributes)
# and behavior (methods) together
class Student:

    # __init__ runs automatically when you create a new Student
    # "self" refers to the specific object being created
    def __init__(self, name, age, major):
        self.name = name
        self.age = age
        self.major = major
        self.gpa = 0.0   # a default value, not passed in

    # a regular method -- takes self, plus any other arguments it needs
    def set_gpa(self, gpa):
        self.gpa = gpa

    def has_graduated_age(self):
        return self.age >= 22

    # __str__ controls what print() shows for this object
    def __str__(self):
        return f"{self.name} ({self.major}), age {self.age}, GPA {self.gpa}"


# --- Creating (instantiating) objects ---
s1 = Student("Vance", 22, "Data Science")
s2 = Student("Maya", 20, "Biology")

print(s1.name)     # access an attribute
print(s2.major)

s1.set_gpa(3.7)     # call a method
print(s1.gpa)

print(s1.has_graduated_age())   # True
print(s2.has_graduated_age())   # False

print(s1)           # uses __str__ automatically


# --- Each object has its own independent data ---
s1.gpa = 3.9
print(s1.gpa)       # 3.9
print(s2.gpa)        # still 0.0 -- changing s1 doesn't touch s2


# --- A list of objects (common pattern in DS 2500) ---
roster = [s1, s2, Student("Jon", 24, "CS")]

for student in roster:
    print(student)                      # uses __str__ for each

names_over_22 = [s.name for s in roster if s.has_graduated_age()]
print(names_over_22)
