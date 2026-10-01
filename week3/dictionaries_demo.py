"""
Demo: Python dictionaries for DS 2500
"""

# --- Creating a dictionary ---
# a dict stores key -> value pairs (unlike a set, which just stores values)
student = {"name": "Vance", "age": 22, "major": "DS"}
print(student)

# empty dict
empty = {}
print(type(empty))          # {} makes a dict, NOT a set -- opposite of what you'd expect


# --- Accessing values ---
print(student["name"])      # looks up by key -- fast, like a set's membership test

# .get() is safer than [] -- it returns None (or a default) instead of erroring
print(student.get("gpa"))            # None, no crash
print(student.get("gpa", "N/A"))     # "N/A" -- custom default


# --- Adding / updating ---
student["gpa"] = 3.7                 # adds a new key
student["age"] = 23                  # overwrites an existing key
print(student)


# --- Removing ---
del student["gpa"]
print(student)


# --- Checking for a key ---
print("major" in student)   # True -- checks KEYS by default, not values
print("DS" in student)      # False -- "DS" is a value, not a key


# --- Looping over a dictionary ---
grades = {"math": 90, "bio": 85, "cs": 97}

for key in grades:
    print(key)               # looping directly gives you the keys

for key, value in grades.items():
    print(key, "->", value)  # .items() gives you both

for value in grades.values():
    print(value)             # just the values


# --- A practical example: counting things ---
# dicts are the standard tool for counting/tallying in DS 2500
words = ["cat", "dog", "cat", "bird", "dog", "cat"]

counts = {}
for word in words:
    counts[word] = counts.get(word, 0) + 1

print(counts)   # {'cat': 3, 'dog': 2, 'bird': 1}


