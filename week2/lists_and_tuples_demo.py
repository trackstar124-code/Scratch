"""
Demo: lists and tuples for DS 2500
"""

# --- Creating lists ---
fruits = ["apple", "banana", "cherry"]
empty = []

# nested lists -- a list of lists, useful for grids/matrices/tables
matrix = [
    [1, 2, 3],
    [4, 5, 6],
]
print(matrix[0])        # [1, 2, 3] -- the first ROW
print(matrix[0][1])     # 2 -- row 0, column 1

# initializing with repeated values using *
zeros = [0] * 5
print(zeros)             # [0, 0, 0, 0, 0]

# careful with nested lists + * -- this repeats REFERENCES to the SAME
# inner list, which can cause surprising bugs when you mutate one row
grid = [[0] * 3] * 2
grid[0][0] = 99
print(grid)              # [[99, 0, 0], [99, 0, 0]] -- BOTH rows changed!


# --- Indexing (zero-based, same as strings) ---
print(fruits[0])         # 'apple' -- first element
print(fruits[-1])        # 'cherry' -- last element, counting from the end


# --- Slicing: fruits[start:stop] -- stop is EXCLUSIVE ---
numbers = [10, 20, 30, 40, 50]
print(numbers[1:3])      # [20, 30] -- index 1 up to (not including) 3
print(numbers[:2])       # [10, 20]
print(numbers[2:])       # [30, 40, 50]
print(numbers[:])        # a full copy of the list


# --- Modifying elements ---
fruits[1] = "blueberry"          # direct assignment by index
print(fruits)

fruits.append("mango")            # adds ONE item to the end
print(fruits)

fruits.extend(["kiwi", "grape"])  # adds MULTIPLE items from another list
print(fruits)                     # (fruits.append(["kiwi","grape"]) would
                                   # instead add one nested list -- a common mixup)

fruits.insert(1, "orange")        # inserts at a specific position
print(fruits)


# --- Removing elements: three different tools ---
fruits.remove("orange")           # removes by VALUE (first match found)
print(fruits)

last_item = fruits.pop()          # removes and RETURNS the last item
print(last_item, fruits)

second_item = fruits.pop(1)       # pop can also take an index
print(second_item, fruits)

del fruits[0]                     # removes by index, no return value
print(fruits)


# --- Membership: in ---
print("mango" in fruits)
print("apple" in fruits)


# --- Concatenation with + ---
a = [1, 2, 3]
b = [4, 5, 6]
combined = a + b
print(combined)          # [1, 2, 3, 4, 5, 6] -- a NEW list, a and b unchanged
print(a)


# --- Tuples: like lists, but IMMUTABLE ---
point = (3, 7)
rgb_color = (255, 0, 128)

print(point[0])           # indexing works just like a list
# point[0] = 99            # TypeError -- tuples can't be modified after creation

# why use a tuple instead of a list?
# 1. it signals "this shouldn't change" -- coordinates, RGB values, etc.
#    are naturally fixed-size and fixed-content
# 2. tuples can be used as DICTIONARY KEYS -- lists cannot, because dict
#    keys must be immutable
locations = {
    (0, 0): "origin",
    (1, 1): "diagonal",
}
print(locations[(0, 0)])

# unpacking a tuple into separate variables
x, y = point
print(x, y)


# --- Code readability: naming and comments ---
# GOOD variable names describe WHAT something is, reducing the need for
# comments to explain the obvious:
student_count = 25          # clear on its own -- no comment needed

# comments are most valuable when they explain WHY, not what -- e.g. a
# non-obvious design decision or the reasoning behind a workaround:
# using pop(0) here instead of remove() because duplicate values are
# possible, and we specifically want to drop the OLDEST entry
queue = [10, 20, 20, 30]
oldest = queue.pop(0)

# avoid comments that just restate the code -- this adds noise, not value:
count = 0        # BAD comment would be: "set count to 0"
