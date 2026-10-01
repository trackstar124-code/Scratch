"""
Demo: Conditional execution (if/elif/else) for DS 2500
"""

# --- Basic if ---
age = 22

if age >= 18:
    print("You are an adult")


# --- if / else ---
temperature = 45

if temperature > 60:
    print("It's warm")
else:
    print("It's cold")


# --- if / elif / else ---
# elif is checked only if the ones above it were False
# only ONE branch runs, even if multiple conditions would be True
score = 85

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
else:
    grade = "F"

print(grade)   # "B" -- even though score >= 70 is also True, it never gets checked


# --- Comparison operators ---
print(5 == 5)     # equal
print(5 != 3)     # not equal
print(5 > 3)
print(5 < 3)
print(5 >= 5)
print(5 <= 4)


# --- Combining conditions: and / or / not ---
gpa = 3.5
credits = 100

if gpa >= 3.0 and credits >= 90:
    print("Eligible for honors")     # both must be True

if gpa >= 3.5 or credits >= 120:
    print("Eligible for something")  # at least one must be True

if not (gpa < 2.0):
    print("Not on probation")


# --- Truthy / falsy values ---
# these are all treated as False in an if-statement:
#   0, 0.0, "", [], {}, set(), None
# everything else is treated as True
name = ""

if name:
    print(f"Hello, {name}")
else:
    print("No name provided")        # this runs -- empty string is falsy

my_list = []
if my_list:
    print("List has items")
else:
    print("List is empty")           # this runs -- empty list is falsy


# --- Nested conditionals ---
weather = "rainy"
has_umbrella = False

if weather == "rainy":
    if has_umbrella:
        print("Go outside, you're covered")
    else:
        print("Stay in, or you'll get wet")
else:
    print("Enjoy the weather")


# --- A practical example: classifying values in a loop ---
numbers = [-5, 0, 3, -2, 8, 0, -1]

for n in numbers:
    if n > 0:
        print(n, "is positive")
    elif n < 0:
        print(n, "is negative")
    else:
        print(n, "is zero")


# --- Short-circuit evaluation ---
# Python stops evaluating an `and`/`or` chain as soon as the result is
# already decided -- the rest never even runs

def expensive_check():
    print("expensive_check() ran")
    return True

# `and` short-circuits on the first False -- expensive_check() is never called
if False and expensive_check():
    pass

# `or` short-circuits on the first True -- expensive_check() is never called
if True or expensive_check():
    pass

# this is also why a pattern like this is SAFE from crashing:
my_dict = {}
if "key" in my_dict and my_dict["key"] > 5:
    print("big value")     # if "key" isn't there, the left side is False,
                            # so Python never even evaluates my_dict["key"]


# --- Type considerations when comparing ---
user_input = "10"      # input() always returns a string
threshold = 5

# print(user_input > threshold)   # TypeError: can't compare str to int
print(int(user_input) > threshold)   # convert first -- True


# --- Identity operators: is / is not ---
# == checks if VALUES are equal. `is` checks if two variables point to
# the EXACT SAME object in memory. For most everyday comparisons you want ==.
# `is` is mainly used for comparing to None.
value = None

if value is None:
    print("value was never set")

if value is not None:
    print("value has something in it")
else:
    print("still nothing")


# --- Ternary operator: a compact if/else for simple assignments ---
age = 16
# long form:
if age >= 18:
    status = "adult"
else:
    status = "minor"

# equivalent one-liner (ternary):
status = "adult" if age >= 18 else "minor"
print(status)


# --- Practical patterns: input validation + defensive programming ---
scores = [88, 92, 75]

# defensive check BEFORE indexing -- avoids an IndexError
index = 5
if index < len(scores):
    print(scores[index])
else:
    print("No score at that position")

# providing a default value if something is missing/invalid
raw_input_value = ""
name = raw_input_value if raw_input_value else "Guest"
print(name)   # "Guest" -- empty string is falsy, so the default kicks in
