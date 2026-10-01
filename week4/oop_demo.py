"""
Demo: object-oriented programming (classes and objects) for DS 2500
"""


# --- A class is a BLUEPRINT; an object (instance) is one thing built from it ---
# A class bundles together:
#   attributes: the data an object holds (brand, model, ...)
#   methods:    the behavior an object has (functions defined inside the class)

class Car:
    # __init__ is the CONSTRUCTOR: it runs automatically when you create a
    # new object, and sets up that object's attributes.
    # `self` is the object being built/used. It is always the first parameter,
    # and Python passes it in for you (you don't write it when calling).
    def __init__(self, brand, model, vin, price, mileage=0):
        self.brand = brand
        self.model = model
        self.vin = vin
        self.price = price
        self.mileage = mileage

    # a method: uses self to reach this particular object's data
    def get_price(self):
        return self.price

    def drive(self, miles):
        self.mileage += miles          # methods can CHANGE the object's data

    # __str__ controls what print() shows for the object.
    # without it, you'd get something unhelpful like <__main__.Car object at 0x...>
    def __str__(self):
        return f"{self.brand} {self.model} (VIN {self.vin}) - ${self.price}, {self.mileage} miles"


# --- Instantiation: calling the class creates an object ---
car1 = Car("Toyota", "Corolla", "1HGCM82633A004352", 18000)
car2 = Car("Honda", "Civic", "2T1BURHE0JC034461", 21000, mileage=500)

print(car1)                    # uses __str__
print(car2.get_price())        # 21000 -- calling a method with dot notation
print(car1.brand)              # attributes are also accessed with a dot

# each object has its OWN copy of the data
car1.drive(120)
print(car1.mileage)            # 120
print(car2.mileage)            # 500 -- unaffected by car1.drive()

# `car1.drive(120)` is really shorthand for `Car.drive(car1, 120)` --
# that's where self comes from.


# --- Second example: a Student class for a registrar ---
class Student:
    def __init__(self, name, student_id, major):
        self.name = name
        self.student_id = student_id
        self.major = major
        self.courses = []              # attributes can start as empty containers

    def enroll(self, course):
        self.courses.append(course)

    def change_major(self, new_major):
        self.major = new_major

    def __str__(self):
        return f"{self.name} (ID {self.student_id}), {self.major}, courses: {self.courses}"

vance = Student("Vance", 12345, "Data Science")
vance.enroll("DS 2500")
vance.enroll("CS 1800")
print(vance)

# forgetting self.courses (writing just `courses`) would make it a plain
# local variable that vanishes when __init__ ends -- a scope bug from earlier!


# --- Encapsulation: hide the internals, expose a clean interface ---
# convention: a leading underscore means "internal -- please don't touch directly"
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self._balance = balance        # internal detail

    def deposit(self, amount):
        if amount <= 0:                # raising errors ties back to error handling
            raise ValueError("deposit must be positive")
        self._balance += amount

    def get_balance(self):
        return self._balance

acct = BankAccount("Vance", 100)
acct.deposit(50)
print(acct.get_balance())      # 150
# Code outside the class only uses deposit() / get_balance(). If we later
# changed how the balance is stored, that outside code wouldn't break --
# that's the benefit of encapsulation.
try:
    acct.deposit(-20)
except ValueError as e:
    print("Error:", e)


# --- Exercise from lecture: a Gene class for DNA sequences ---
class Gene:
    def __init__(self, name, sequence):
        self.name = name
        self.sequence = sequence.upper()      # normalize to uppercase

    def length(self):
        return len(self.sequence)

    def gc_content(self):
        # fraction of bases that are G or C
        if len(self.sequence) == 0:
            return 0.0
        gc_count = self.sequence.count("G") + self.sequence.count("C")
        return gc_count / len(self.sequence)

    def __str__(self):
        return f"Gene {self.name}: {self.sequence} (length {self.length()}, GC {self.gc_content():.0%})"

brca = Gene("BRCA1", "atgcgcgta")
print(brca)                       # Gene BRCA1: ATGCGCGTA (length 9, GC 56%)
print(brca.length())              # 9
print(round(brca.gc_content(), 3))  # 0.556

# objects work great inside lists, so you can combine OOP with earlier topics
genes = [Gene("geneA", "ATGC"), Gene("geneB", "GGGCCC"), Gene("geneC", "ATAT")]
by_gc = sorted(genes, key=lambda g: g.gc_content(), reverse=True)   # lambda!
for g in by_gc:
    print(g)
