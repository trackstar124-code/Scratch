"""
Demo: variable scope (LEGB) for DS 2500
"""


# --- Scope = where in the code a variable can be seen/used ---
# Python looks up a name in this order (LEGB):
#   L - Local:     inside the current function
#   E - Enclosing: inside any outer function (for nested functions)
#   G - Global:    defined at the top level of the file
#   B - Built-in:  Python's own names (print, len, sum, max, ...)
# The FIRST scope that has the name wins.


# --- Local scope: variables made inside a function stay inside it ---
def make_greeting():
    message = "hello"          # local to make_greeting
    print(message)

make_greeting()
# print(message)               # NameError: message doesn't exist out here


# --- Global scope: defined outside all functions, visible everywhere ---
# globals are typically used for CONSTANTS shared by many functions
# (convention: UPPER_CASE names)
FREEZING_F = 32

def is_freezing(temp_f):
    return temp_f <= FREEZING_F       # reads the global -- no problem

print(is_freezing(20))     # True
print(is_freezing(50))     # False


# --- Local beats global when names collide ---
x = 10                      # global

def show_x(x):
    # the parameter x is LOCAL, so it shadows the global x
    print("inside:", x)

show_x(99)                  # inside: 99
print("outside:", x)        # outside: 10 -- the global never changed


# --- Assigning inside a function makes a NEW local, not a change to the global ---
count = 0

def try_to_increment():
    count = 5               # creates a brand-new local variable named count
    print("inside:", count)

try_to_increment()
print("outside:", count)    # still 0

# to actually modify a global, you must declare it with `global`:
def really_increment():
    global count
    count = count + 1

really_increment()
print(count)                # 1
# NOTE: modifying globals this way is usually discouraged -- it makes bugs
# hard to track. Prefer passing values in as parameters and returning results.


# --- Common bug: reading a variable before assigning it locally ---
total = 100

def broken():
    # Python sees `total = ...` below, so it treats total as LOCAL for the
    # WHOLE function -- meaning this read happens before it has a value
    try:
        total = total + 1
    except UnboundLocalError as e:
        print("UnboundLocalError:", e)

broken()


# --- Enclosing scope: a nested function can see the outer function's variables ---
def outer():
    greeting = "hi"          # enclosing scope for inner()

    def inner():
        print(greeting)      # not local, so Python checks outer() next

    inner()

outer()

# to modify an enclosing variable from the inner function, use `nonlocal`
def counter():
    n = 0

    def add_one():
        nonlocal n
        n += 1
        return n

    add_one()
    add_one()
    return add_one()

print(counter())            # 3


# --- Built-in scope: Python's own names live here (checked LAST) ---
print(len([1, 2, 3]))       # 3 -- len comes from the built-in scope

# because built-ins are checked last, you can accidentally shadow them:
list_of_nums = [4, 8, 15]
sum = 0                     # oops: global `sum` now hides the built-in sum()
for n in list_of_nums:
    sum += n
print(sum)                  # 27
# print(sum(list_of_nums))  # TypeError: 'int' object is not callable
del sum                     # removing our global brings the built-in back
print(sum(list_of_nums))    # 27 -- works again
# lesson: don't name variables sum, max, min, list, str, len, id, etc.


# --- All four scopes at once ---
level = "global"

def show_levels():
    level = "enclosing"

    def inner():
        level = "local"
        print(level)         # local

    inner()
    print(level)             # enclosing

show_levels()
print(level)                 # global


# --- Practice exercise: filter invalid sensor readings ---
# raw readings come in as strings; some are junk. Keep only the valid floats.
MAX_VALID_TEMP = 150.0       # global constant shared by the function

def filter_readings(raw_readings):
    valid = []                       # local list -- built up and returned
    for reading in raw_readings:
        try:
            temp = float(reading)    # raises ValueError for junk like "ERR"
        except ValueError:
            print(f"skipping invalid reading: {reading!r}")
            continue                 # move on to the next reading
        if temp <= MAX_VALID_TEMP:
            valid.append(temp)
    return valid

readings = ["72.5", "68.1", "ERR", "70.0", "", "n/a", "75.3", "9999"]
valid_readings = filter_readings(readings)
print(valid_readings)        # [72.5, 68.1, 70.0, 75.3]
