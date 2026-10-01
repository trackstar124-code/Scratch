"""
Demo: comprehensions for DS 2500
"""

# --- The problem comprehensions solve ---
# the "long way": build an empty list, loop, append each result
squares_long = []
for num in range(1, 6):
    squares_long.append(num ** 2)
print(squares_long)

# the comprehension way: same result, one line
# [ expression  for item in iterable ]
squares = [num ** 2 for num in range(1, 6)]
print(squares)


# --- Exercise 1: 0 for even values, 1 for odd values ---
numbers = [4, 7, 10, 13, 8, 5]

flags_long = []
for n in numbers:
    if n % 2 == 0:
        flags_long.append(0)
    else:
        flags_long.append(1)
print(flags_long)

# comprehension with an if/else EXPRESSION (not a filter -- every
# element produces SOMETHING, just a different value depending on the
# condition)
flags = [0 if n % 2 == 0 else 1 for n in numbers]
print(flags)


# --- Exercise 2: Boolean list for even/odd ---
is_even = [n % 2 == 0 for n in numbers]
print(is_even)


# --- Exercise 3: length of each word ---
words = ["data", "science", "python", "ds2500"]
word_lengths = [len(word) for word in words]
print(word_lengths)


# --- Filtering with if (this DROPS elements, unlike if/else above) ---
# [ expression  for item in iterable  if condition ]
evens_only = [n for n in numbers if n % 2 == 0]
print(evens_only)      # only the even numbers make it into the new list

long_words = [word for word in words if len(word) > 4]
print(long_words)


# --- Set comprehension: curly braces, automatically deduplicated ---
values = [1, 2, 2, 3, 3, 3, 4]
unique_squares = {n ** 2 for n in values}
print(unique_squares)   # duplicates collapse -- and order isn't guaranteed,
                         # since sets are stored as a hash table, not a sequence


# --- Dictionary comprehension: { key_expr: value_expr  for item in iterable } ---
# dicts preserve INSERTION order (unlike sets)
word_to_length = {word: len(word) for word in words}
print(word_to_length)

# with a condition, same as list comprehension filtering
long_word_lengths = {word: len(word) for word in words if len(word) > 4}
print(long_word_lengths)


# --- Nested comprehension: multiple for clauses, for multi-dimensional data ---
# flattening a 2D list (list of lists) into a single flat list
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]

# the long way, with nested for loops:
flat_long = []
for row in matrix:
    for value in row:
        flat_long.append(value)
print(flat_long)

# the comprehension way -- read the "for" clauses LEFT TO RIGHT in the
# same order you'd nest them as loops (outer loop first, inner loop second)
flat = [value for row in matrix for value in row]
print(flat)

# you can combine nested comprehension with a condition too
flat_evens = [value for row in matrix for value in row if value % 2 == 0]
print(flat_evens)
