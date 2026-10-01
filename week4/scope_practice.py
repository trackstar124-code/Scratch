"""
Practice: variable scope + sensor filtering for DS 2500
Fill in each TODO, then run the file. Asserts tell you what you got wrong.
(Worked examples are in scope_demo.py -- try without peeking first!)
"""


# --- Part 1: predict the output ---
# Write your prediction in the string BEFORE running the code below it.
# Then uncomment the code and check.

# Q1
x = "global"
def f():
    x = "local"
f()
q1_prediction = "TODO"         # what does print(x) show?
assert q1_prediction == x, f"Q1: actually prints {x!r}"

# Q2
y = 5
def g(y):
    return y * 2
q2_prediction = None           # TODO: what does g(10) return?
assert q2_prediction == g(10), f"Q2: actually {g(10)}"
assert y == 5                  # and y itself is unchanged -- why?

# Q3: which scope (L, E, G, or B) does each name come from?
LIMIT = 100
def h(values):
    total = 0
    for v in values:
        total += v
    return min(total, LIMIT)
q3 = {
    "values": "TODO",          # L, E, G, or B
    "total": "TODO",
    "LIMIT": "TODO",
    "min": "TODO",
}
assert q3 == {"values": "L", "total": "L", "LIMIT": "G", "min": "B"}, "Q3: recheck LEGB"


# --- Part 2: write the functions ---

# Q4: return a function that multiplies its input by n (enclosing scope)
def make_multiplier(n):
    pass    # TODO: define an inner function that uses n, and return it

triple = make_multiplier(3)
assert triple(4) == 12, "Q4: make_multiplier(3)(4) should be 12"
assert make_multiplier(10)(2) == 20


# Q5: a counter that remembers its count between calls (nonlocal)
def make_counter():
    count = 0
    # TODO: define an inner function that increments count and returns it
    pass

c = make_counter()
c()
c()
assert c() == 3, "Q5: third call should return 3"


# Q6: fix the bug -- this should add 1 to the global `score`
score = 0
def add_point():
    pass    # TODO: one extra line is needed so score = score + 1 works

add_point()
add_point()
assert score == 2, "Q6: score should be 2 after two calls"


# --- Part 3: filter invalid sensor readings ---
# Readings arrive as strings. Convert each to a float with try-except and
# keep only the valid ones (skip junk like "ERR" or ""). Also drop anything
# above MAX_TEMP.
MAX_TEMP = 150.0

def filter_readings(raw_readings):
    valid = []
    # TODO: loop over raw_readings
    #   try to convert each reading to float
    #   on ValueError, skip it
    #   otherwise, append it if it is <= MAX_TEMP
    return valid

assert filter_readings(["72.5", "ERR", "70", "", "9999", "68.1"]) == [72.5, 70.0, 68.1], \
    "Q7: expected [72.5, 70.0, 68.1]"
assert filter_readings([]) == []
assert filter_readings(["bad", "worse"]) == []


# Q8 (stretch): change filter_readings to take max_temp as a parameter
# (default 150.0) instead of reading the global. Why is that more flexible?
# Then add an assert below showing a different cutoff works.

print("All checks passed!")
