"""
Demo: Python sets for DS 2500
"""

# --- Creating a set ---
fruits = {"apple", "banana", "cherry"}
print(fruits)              # order is not guaranteed! sets are unordered

# duplicates are automatically removed
numbers = {1, 2, 2, 3, 3, 3}
print(numbers)              # {1, 2, 3}

# empty set MUST use set(), not {} (that makes an empty dict)
empty = set()
print(type(empty))

# from a list -- a common way to dedupe data
raw = [1, 5, 5, 2, 2, 2, 8]
unique_values = set(raw)
print(unique_values)        # {1, 2, 5, 8}


# --- Adding / removing elements ---
fruits.add("mango")
fruits.remove("banana")     # raises an error if "banana" isn't there
fruits.discard("kiwi")      # no error even if "kiwi" isn't there
print(fruits)


# --- Membership testing (this is what sets are best at) ---
print("apple" in fruits)    # True -- O(1) lookup, much faster than checking a list


# --- Set math: the real reason sets exist ---
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print(a | b)   # union: all elements in either set        -> {1,2,3,4,5,6}
print(a & b)   # intersection: elements in both            -> {3,4}
print(a - b)   # difference: in a but not in b             -> {1,2}
print(a ^ b)   # symmetric difference: in one but not both -> {1,2,5,6}


# --- A practical example: comparing two rosters ---
class_a = {"Vance", "Maya", "Jon", "Priya"}
class_b = {"Jon", "Priya", "Sam"}

print("In both classes:", class_a & class_b)
print("Only in class A:", class_a - class_b)
print("All students combined:", class_a | class_b)
