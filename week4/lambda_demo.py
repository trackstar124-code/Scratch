"""
Demo: lambda functions and higher-order functions for DS 2500
"""

from functools import reduce


# --- Lambda syntax: an anonymous, single-expression function ---
# lambda arguments: expression
square = lambda x: x ** 2
print(square(5))          # 25

add = lambda a, b: a + b
print(add(3, 4))          # 7

# NOTE: assigning a lambda to a variable like this works, but it kind of
# defeats the purpose -- if you need a name for it, just use a regular
# `def` function instead. Lambdas shine as throwaway, INLINE arguments
# to other functions (map, filter, sorted, reduce), which is what the
# rest of this file focuses on.


# --- map(): apply a function to every item in an iterable ---
numbers = [1, 2, 3, 4, 5]

squared = map(lambda x: x ** 2, numbers)
print(list(squared))       # map() returns a lazy map object -- wrap in
                            # list() to see/use the actual results

doubled = list(map(lambda x: x * 2, numbers))
print(doubled)


# --- filter(): keep only items where the function returns True ---
evens = filter(lambda x: x % 2 == 0, numbers)
print(list(evens))         # same idea -- wrap in list() to materialize it

words = ["cat", "elephant", "dog", "hippopotamus"]
short_words = list(filter(lambda w: len(w) <= 3, words))
print(short_words)


# --- reduce(): combine all items into ONE aggregated result ---
# unlike map/filter, reduce is not a built-in -- it comes from functools
total = reduce(lambda acc, x: acc + x, numbers)
print(total)               # 15 -- same as sum(numbers), just via reduce

product = reduce(lambda acc, x: acc * x, numbers)
print(product)             # 120 -- 1*2*3*4*5


# --- sorted() with a lambda key function ---
# `key=` tells sorted() WHAT to sort by, instead of comparing items directly
colors = ["blue", "red", "chartreuse", "tan"]
sorted_by_length = sorted(colors, key=lambda c: len(c))
print(sorted_by_length)     # shortest to longest

# sorting a list of dicts by one specific field
people = [
    {"name": "Vance", "age": 22},
    {"name": "Maya", "age": 20},
    {"name": "Jon", "age": 24},
]
sorted_by_age = sorted(people, key=lambda person: person["age"])
print(sorted_by_age)

# reverse=True works here too, same as with any sorted() call
oldest_first = sorted(people, key=lambda person: person["age"], reverse=True)
print(oldest_first)


# --- Lambda limitations ---
# lambdas can only hold a SINGLE expression -- no loops, no multiple
# statements, no assignment statements inside them. This would NOT work:
#
# bad = lambda x: for i in range(x): print(i)     # SyntaxError
#
# anything beyond a simple expression needs a real `def` function instead:
def print_range(x):
    for i in range(x):
        print(i)


# --- Combined exercise: dict comprehension + lambda ---
# filter genes with expression > 20, then sort ascending by expression value
gene_expression = {
    "geneA": 12,
    "geneB": 45,
    "geneC": 30,
    "geneD": 8,
    "geneE": 22,
}

# step 1: filter with a dict comprehension (keep only expression > 20)
high_expression = {gene: level for gene, level in gene_expression.items() if level > 20}
print(high_expression)

# step 2: sort those items ascending by expression value using a lambda key
# .items() gives (gene, level) tuples -- sort by the second element (index 1)
sorted_high_expression = sorted(high_expression.items(), key=lambda pair: pair[1])
print(sorted_high_expression)   # a list of (gene, level) tuples, low to high
