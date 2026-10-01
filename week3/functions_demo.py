"""
Demo: functions for DS 2500
"""

# --- Defining a function ---
# def, name, parameters in (), an optional docstring, a body, and an
# optional return statement
def greet(name):
    """Print a greeting for the given name."""
    print(f"Hello, {name}!")

greet("Vance")


# --- return vs print ---
# print() just displays something -- it doesn't give the caller a value
# to use. return sends a value BACK to wherever the function was called,
# so it can be stored in a variable or used in further calculations.
def add(a, b):
    return a + b

result = add(3, 4)
print(result)       # 7 -- we captured the returned value


# --- Returning multiple values ---
# separate them with commas -- Python packs them into a tuple automatically
def min_and_max(numbers):
    return min(numbers), max(numbers)

low, high = min_and_max([4, 8, 1, 9, 3])
print(low, high)


# --- Required vs optional (default) parameters ---
def power(base, exponent=2):     # exponent is optional, defaults to 2
    return base ** exponent

print(power(5))         # 25 -- uses the default exponent
print(power(5, 3))      # 125 -- overrides the default


# --- Positional vs keyword arguments ---
def describe_pet(name, animal_type, age):
    print(f"{name} is a {age}-year-old {animal_type}")

describe_pet("Rex", "dog", 3)                          # positional -- order matters
describe_pet(name="Rex", age=3, animal_type="dog")     # keyword -- order doesn't matter
describe_pet("Rex", age=3, animal_type="dog")          # mixing both is fine,
                                                        # as long as positional args come first


# --- Immutable arguments: changes inside the function DON'T escape ---
# ints, strings, tuples, floats, bools are immutable
def try_to_change_number(n):
    n = n + 100          # this only changes the LOCAL copy of n
    print("inside function:", n)

x = 5
try_to_change_number(x)
print("outside function:", x)   # still 5 -- untouched


# --- Mutable arguments: changes inside the function DO show up outside ---
# lists, dicts, sets are mutable -- the function receives a reference to
# the SAME object, not a copy
def add_item(shopping_list):
    shopping_list.append("milk")    # modifies the ORIGINAL list

groceries = ["eggs", "bread"]
add_item(groceries)
print(groceries)        # ['eggs', 'bread', 'milk'] -- the original changed


# --- Avoiding unintended side effects on mutable arguments ---
# if you DON'T want to modify the caller's original list, build a new one
# instead of mutating the one you were given
def add_item_safely(shopping_list):
    new_list = shopping_list.copy()
    new_list.append("milk")
    return new_list

original = ["eggs", "bread"]
updated = add_item_safely(original)
print(original)   # ['eggs', 'bread'] -- unchanged
print(updated)     # ['eggs', 'bread', 'milk'] -- the new one has the addition


# --- THE big gotcha: never use a mutable default parameter ---
# Python evaluates default values ONCE, when the function is defined --
# not every time it's called. A mutable default gets reused and quietly
# accumulates state across calls.

# BAD:
def add_to_list_bad(item, target=[]):     # this [] is created ONCE, ever
    target.append(item)
    return target

print(add_to_list_bad("a"))   # ['a']
print(add_to_list_bad("b"))   # ['a', 'b']  <- surprise! same list as before

# GOOD: use None as the default, create a fresh list inside the function
def add_to_list_good(item, target=None):
    if target is None:
        target = []
    target.append(item)
    return target

print(add_to_list_good("a"))   # ['a']
print(add_to_list_good("b"))   # ['b']  <- fresh list each time, as expected


# --- Debugging practice: spot the bug in each version ---
# these mirror the kinds of mistakes covered in lecture -- inches to
# meters conversion, each with one bug. Try to spot each bug BEFORE
# reading the fixed version below it.

# Bug 1: missing return statement -- function computes the value but
# never sends it back, so the caller gets None
def inches_to_meters_v1(inches):
    meters = inches * 0.0254
    # no return! calling this always gives you None

print(inches_to_meters_v1(10))    # None -- bug

def inches_to_meters_v1_fixed(inches):
    meters = inches * 0.0254
    return meters

print(inches_to_meters_v1_fixed(10))   # 0.254 -- fixed


# Bug 2: undefined variable -- typo'd variable name inside the function
def inches_to_meters_v2(inches):
    result = inches * 0.0254
    return reslt        # typo -- NameError, "reslt" was never defined

try:
    print(inches_to_meters_v2(10))
except NameError as e:
    print("Bug 2 error:", e)

def inches_to_meters_v2_fixed(inches):
    result = inches * 0.0254
    return result

print(inches_to_meters_v2_fixed(10))   # 0.254 -- fixed


# Bug 3: incorrect indentation -- return is INSIDE something it shouldn't
# be nested in, so it only sometimes runs (or errors), instead of always
def inches_to_meters_v3(inches):
    if inches > 0:
        meters = inches * 0.0254
        return meters
    # if inches <= 0, there's no return at all -- falls through to None

print(inches_to_meters_v3(10))    # 0.254 -- works for positive input
print(inches_to_meters_v3(-5))    # None -- bug: silently returns nothing

def inches_to_meters_v3_fixed(inches):
    meters = inches * 0.0254
    return meters               # return lives at the function's top level,
                                 # so it always runs regardless of the if

print(inches_to_meters_v3_fixed(-5))   # -0.127 -- fixed


# Bug 4: mutable default parameter -- storing conversion history the
# same buggy way as add_to_list_bad() above
def inches_to_meters_v4(inches, history=[]):
    meters = inches * 0.0254
    history.append(meters)
    return meters, history

result1, hist1 = inches_to_meters_v4(10)
result2, hist2 = inches_to_meters_v4(20)
print("Bug 4 history:", hist2)   # contains BOTH results, not just this call's

def inches_to_meters_v4_fixed(inches, history=None):
    if history is None:
        history = []
    meters = inches * 0.0254
    history.append(meters)
    return meters, history

result1, hist1 = inches_to_meters_v4_fixed(10)
result2, hist2 = inches_to_meters_v4_fixed(20)
print("Bug 4 fixed history:", hist2)   # only this call's result
