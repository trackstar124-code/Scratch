"""
Demo: for loops (definite loops) for DS 2500
"""

# --- for loops vs while loops ---
# use a for loop when the number of iterations is KNOWN in advance
# (looping over a list, a fixed range, characters in a string, etc.)
# use a while loop when you're waiting for a condition, and don't know
# ahead of time how many passes it'll take.


# --- range(): the three versions ---
# range(stop)               -- 0 up to (not including) stop
# range(start, stop)        -- start up to (not including) stop
# range(start, stop, step)  -- start up to (not including) stop, by step
# in all cases, the stop value is EXCLUSIVE -- never included

for i in range(5):
    print(i)                 # 0, 1, 2, 3, 4 -- 5 is NOT included

print("---")

for i in range(2, 6):
    print(i)                 # 2, 3, 4, 5

print("---")

for i in range(0, 10, 2):
    print(i)                 # 0, 2, 4, 6, 8

print("---")

for i in range(10, 0, -2):   # negative step counts DOWN
    print(i)                 # 10, 8, 6, 4, 2


# --- Iterating over sequences with "in" ---
fruits = ["apple", "banana", "cherry"]

for fruit in fruits:          # iterates over a LIST
    print(fruit)

coordinates = (3, 7)
for value in coordinates:     # iterates over a TUPLE
    print(value)

for letter in "hi":            # iterates over a STRING, one char at a time
    print(letter)

grades = {"math": 90, "bio": 85}
for subject in grades:         # iterating a DICT gives you the KEYS
    print(subject, grades[subject])


# --- Best practice: iterate directly, don't loop by index ---
# BAD -- indexing manually when you don't need to:
for i in range(len(fruits)):
    print(fruits[i])

# GOOD -- iterate over the elements directly:
for fruit in fruits:
    print(fruit)

# use enumerate() when you need BOTH the index and the value
for index, fruit in enumerate(fruits):
    print(index, fruit)


# --- break and continue (same behavior as in while loops) ---
for n in range(10):
    if n == 5:
        break                 # stop the loop entirely
    print("break demo:", n)

for n in range(6):
    if n % 2 == 0:
        continue              # skip the rest of this pass, go to next n
    print("continue demo:", n)


# --- Nested loops: for processing multidimensional data ---
# e.g. a grid, a matrix, or an image (rows of pixels)
grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]

for row in grid:
    for value in row:
        print(value, end=" ")
    print()                   # newline after each row


# --- Practical example: nested loops + dict + conditionals ---
# processing gene expression data: for each sample, flag genes that are
# "highly expressed" (over a threshold)
gene_expression = {
    "sample_1": {"geneA": 12, "geneB": 45, "geneC": 3},
    "sample_2": {"geneA": 50, "geneB": 8, "geneC": 60},
}
threshold = 40

for sample, genes in gene_expression.items():
    for gene, level in genes.items():
        if level > threshold:
            print(f"{sample}: {gene} is highly expressed ({level})")


# --- Boolean flags to break out of nested loops ---
# a `break` only exits the INNERMOST loop -- a flag lets you escape both
found = False
target = 5

for row in grid:
    for value in row:
        if value == target:
            found = True
            break             # only breaks the inner loop
    if found:
        break                 # this breaks the outer loop too

print("Found target:", found)


# --- for/else: the else runs only if the loop NEVER hit a break ---
def is_prime(number):
    for divisor in range(2, number):
        if number % divisor == 0:
            return False       # found a factor -- not prime
    else:
        return True            # loop finished with no break -- it's prime

print(is_prime(7))    # True
print(is_prime(10))   # False

# same idea written with an explicit for/else instead of return, to show
# the else clause directly:
num = 13
for divisor in range(2, num):
    if num % divisor == 0:
        print(num, "is not prime, divisible by", divisor)
        break
else:
    print(num, "is prime")     # runs because the loop never broke
