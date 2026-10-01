"""
Demo: error handling and defensive programming for DS 2500
"""


# --- The three types of errors ---
# 1. Syntax errors: easiest to find -- Python refuses to run the code at all
# 2. Runtime errors (exceptions): moderate -- code starts, then crashes mid-run
# 3. Logical errors: hardest -- code runs fine but gives the WRONG answer
#
# Syntax error (would stop the whole file from running, so it's commented out):
# print("hello"          # SyntaxError: '(' was never closed

# Runtime errors -- each of these crashes the program when it executes:
# int("abc")             # ValueError
# 10 / 0                 # ZeroDivisionError
# [1, 2, 3][10]          # IndexError
# {"a": 1}["b"]          # KeyError

# Logical error -- no crash, but the result is wrong:
def average(nums):
    return sum(nums) / len(nums) + 1     # oops, the "+ 1" is a bug

print(average([2, 4, 6]))   # prints 5.0, but the real average is 4.0


# --- try-except: handle a runtime error instead of crashing ---
try:
    value = int("abc")
    print("converted:", value)       # skipped -- the error happens on the line above
except ValueError:
    print("That wasn't a valid number")

print("program keeps running!")     # without try-except, we'd never reach this


# --- Multiple except clauses: handle different errors differently ---
def safe_divide(a, b):
    try:
        result = int(a) / int(b)
        return result
    except ValueError:
        print("Both inputs must be numbers")
    except ZeroDivisionError:
        print("Can't divide by zero")
    except Exception as e:
        # generic fallback for anything unexpected -- keep it LAST, since
        # Python uses the first except clause that matches
        print("Something unexpected happened:", e)

print(safe_divide(10, 2))       # 5.0
print(safe_divide("ten", 2))    # ValueError branch -> None
print(safe_divide(10, 0))       # ZeroDivisionError branch -> None
print(safe_divide(None, 2))     # TypeError -> caught by the generic handler


# --- else and finally ---
# else: runs only if NO exception happened
# finally: runs no matter what (good for cleanup, like closing files)
try:
    number = int("42")
except ValueError:
    print("bad input")
else:
    print("success, got", number)
finally:
    print("this always runs")


# --- Partial execution: errors only stop what comes AFTER them ---
# with try-except inside a loop, one bad item doesn't ruin the whole run
raw_values = ["3", "7", "oops", "10", "n/a", "5"]
clean_values = []
for item in raw_values:
    try:
        clean_values.append(int(item))
    except ValueError:
        print(f"skipping bad value: {item!r}")
print(clean_values)             # [3, 7, 10, 5]


# --- Raising errors: escalate a problem to the caller ---
# sometimes a function shouldn't try to fix the problem itself -- it should
# tell whoever called it that something went wrong
def get_percentage(part, whole):
    if whole == 0:
        raise ValueError("whole cannot be zero")
    if part > whole:
        raise ValueError("part cannot be larger than whole")
    return part / whole * 100

try:
    print(get_percentage(5, 20))    # 25.0
    print(get_percentage(5, 0))     # raises -> jumps to except
except ValueError as e:
    print("Caught error from get_percentage:", e)


# --- assert: check that a condition is True, else raise AssertionError ---
# assert condition, "message shown if the condition is False"
# commonly used for unit tests and auto-graders
def add(a, b):
    return a + b

assert add(2, 3) == 5, "add(2, 3) should be 5"
assert add(-1, 1) == 0, "add(-1, 1) should be 0"
print("all asserts passed")

# a failing assert crashes with AssertionError -- here we catch it to show it:
try:
    assert add(2, 2) == 5, "add(2, 2) should be 5"
except AssertionError as e:
    print("Assertion failed:", e)

# NOTE: raise is for errors your program should handle at runtime (bad user
# input, missing files); assert is for sanity-checking your own code.
