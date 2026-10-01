"""
Demo: Python fundamentals -- expressions, variables, and data types
for DS 2500
"""

# --- Running Python code ---
# two main ways:
# 1. the interactive interpreter/terminal (type `python3` with no file,
#    or use a REPL) -- good for quick one-off checks, nothing is saved
# 2. a source file, like this one (`python3 python_basics_demo.py`) --
#    good for anything you want to save, reuse, or share


# --- Expressions: Python evaluates them and produces a value ---
print(3 + 4)
print(10 / 3)
print(2 ** 5)        # exponent -- 2 to the 5th power
print(17 % 5)        # modulo -- remainder after division


# --- Variables: named containers for values ---
# Python is DYNAMICALLY typed -- you never declare a type up front like
# you would in Java or C++ (e.g. no "int x = 5;"). The type is inferred
# automatically from whatever value you assign
age = 22             # Python infers this is an int
price = 9.99         # inferred as a float
name = "Vance"       # inferred as a str

print(type(age))
print(type(price))
print(type(name))

# a variable can be REASSIGNED to a different type entirely -- Python
# doesn't stop you (unlike a statically typed language)
age = "twenty-two"
print(type(age))     # now a str


# --- Variable naming conventions ---
# GOOD: lowercase with underscores ("snake_case"), descriptive names
student_age = 22
total_price = 49.99

# BAD (avoid, even though some of these are technically legal):
# x = 22                  -- single letters/ambiguous names hurt readability
# 2nd_place = "Maya"      -- ILLEGAL: can't start with a number
# class = "DS 2500"       -- ILLEGAL: "class" is a reserved Python keyword

# checking Python's reserved keywords:
import keyword
print(keyword.kwlist[:5], "...")   # just a sample -- there are ~35 total


# --- Arithmetic operators and precedence ---
# standard math order of operations applies: parentheses, exponents,
# then multiplication/division, then addition/subtraction (left to right)
result = 2 + 3 * 4
print(result)         # 14, NOT 20 -- multiplication happens before addition

result = (2 + 3) * 4
print(result)         # 20 -- parentheses force addition first

# when an expression gets complicated, use parentheses for CLARITY even
# if they're not strictly required -- it prevents mistakes and makes the
# intended order obvious to someone reading it later
result = (10 + 5) / (3 - 1) ** 2
print(result)


# --- Primitive data types ---
whole_number = 42            # int
decimal_number = 3.14        # float
is_valid = True              # bool -- True or False (capitalized!)
nothing = None                # None -- represents "no value at all"

print(type(whole_number))
print(type(decimal_number))
print(type(is_valid))
print(type(nothing))

# None is NOT the same as 0, False, or an empty string -- it specifically
# means "there is no value here"
value = None
print(value == 0)       # False
print(value is None)    # True -- this is the correct way to check for None


# --- Floating-point precision issues ---
# floats can't always represent decimal numbers EXACTLY in binary,
# leading to tiny rounding errors
print(0.1 + 0.2)               # 0.30000000000000004, not exactly 0.3
print(0.1 + 0.2 == 0.3)        # False! -- a classic gotcha

# for money or anything needing exact precision, round explicitly when
# comparing or displaying:
print(round(0.1 + 0.2, 2) == 0.3)   # True


# --- Type conversion functions ---
text_number = "17"
print(int(text_number) + 3)     # 20 -- str converted to int

whole = 9
print(float(whole))             # 9.0 -- int converted to float

number = 3.999
print(int(number))              # 3 -- float converted to int TRUNCATES
                                 # (doesn't round!) toward zero

print(str(42) + " items")       # int converted to str, for concatenation

print(bool(0))                  # False
print(bool(1))                  # True
print(bool(""))                 # False -- empty string is falsy
print(bool("hi"))                # True -- any non-empty string is truthy
