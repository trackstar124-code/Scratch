"""
Demo: while loops for DS 2500
"""

# --- Basic while loop ---
# the condition is checked BEFORE each pass through the loop body.
# if it's False right away, the loop body never runs at all.
count = 0

while count < 5:
    print(count)
    count += 1     # without this, count never changes -> infinite loop

print("done with basic loop")


# --- The classic bug: forgetting to update the condition variable ---
# this is commented out on purpose -- uncommenting it would hang forever,
# since `count` never changes inside the loop
#
# count = 0
# while count < 5:
#     print(count)     # count is never incremented -> runs forever


# --- while vs for ---
# use a `for` loop when you know how many times you're looping (e.g. over
# a list, or range(5)). Use a `while` loop when you don't know in advance
# how many iterations it'll take -- you're waiting for some CONDITION to
# become true/false instead.


# --- break: exit the loop immediately, skipping whatever is left ---
n = 0
while True:            # an intentional infinite loop -- break is what stops it
    if n == 3:
        break
    print("n is", n)
    n += 1

print("broke out when n hit 3")


# --- continue: skip the rest of this iteration, go to the next one ---
i = 0
while i < 6:
    i += 1
    if i % 2 == 0:
        continue        # skip printing even numbers
    print(i, "is odd")


# --- Sentinel-controlled loop: a very common DS 2500 pattern ---
# keep looping until the user enters a specific "stop" value
# (this is commented out so the file can run without pausing for input --
#  uncomment it to try it interactively)
#
# total = 0
# entry = input("Enter a number (or 'done' to stop): ")
# while entry != "done":
#     total += int(entry)
#     entry = input("Enter a number (or 'done' to stop): ")
# print("Total:", total)


# --- Input validation loop: keep asking until the input is valid ---
# also commented out since it needs real input -- try it yourself
#
# age = int(input("Enter your age: "))
# while age < 0:
#     print("Age can't be negative, try again")
#     age = int(input("Enter your age: "))
# print("Thanks, your age is", age)


# --- Nested while loops ---
row = 1
while row <= 3:
    col = 1
    while col <= 3:
        print(f"({row},{col})", end=" ")
        col += 1
    print()          # newline after each row
    row += 1


# --- A practical example: processing a list without a for loop ---
# (you'd normally use a for loop for this -- but this shows how while
# loops let you control the index manually, e.g. to skip around or
# stop early based on a condition)
data = [4, 8, 15, 16, 23, 42]
index = 0
total = 0

while index < len(data) and total < 30:
    total += data[index]
    index += 1

print("Stopped at index", index, "with total", total)


# --- Classic example: how long to double an investment? ---
# this is the shape of problem while loops are perfect for -- we don't
# know in advance how many years it'll take, we just know the condition
# we're waiting for (balance doubling)
balance = 1000.0
target = balance * 2
rate = 0.07
years = 0

while balance < target:
    balance = balance * (1 + rate)
    years += 1

print(f"It takes {years} years to double $1000 at 7% annual interest")
print(f"Final balance: ${balance:.2f}")


# --- Countdown exercise ---
# initialize -> check condition -> update, the three things every
# while loop needs to terminate correctly
countdown = 5

while countdown > 0:
    print(countdown)
    countdown -= 1

print("Liftoff!")
