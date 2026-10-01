"""
Demo: file input/output and CSV processing for DS 2500
"""

import csv


# --- Basic file writing: open() modes ---
# "w" = write (overwrites the file if it already exists, creates it if not)
# "a" = append (adds to the end, without erasing what's already there)
# "r" = read (the default mode if you don't specify one)

file = open("notes.txt", "w")
file.write("first line\n")
file.write("second line\n")
file.close()          # IMPORTANT: always close a file you opened manually,
                       # or writes may not actually be saved to disk


file = open("notes.txt", "a")
file.write("third line, appended\n")
file.close()


# --- Basic file reading: read(), readline(), and looping ---
file = open("notes.txt", "r")
whole_thing = file.read()     # reads the ENTIRE file as one string
file.close()
print(repr(whole_thing))

file = open("notes.txt", "r")
first_line = file.readline()  # reads just ONE line, including its "\n"
second_line = file.readline()
file.close()
print(repr(first_line))
print(repr(second_line))

file = open("notes.txt", "r")
for line in file:             # looping over a file gives you it line by line
    print(line.strip())       # .strip() removes the trailing "\n"
file.close()


# --- The professional standard: the "with" statement ---
# "with" automatically closes the file for you, even if an error happens
# partway through -- no risk of forgetting file.close() and leaking a
# file handle
with open("notes.txt", "r") as file:
    contents = file.read()
print(contents)
# the file is already closed here, as soon as we leave the "with" block


with open("notes.txt", "a") as file:
    file.write("fourth line, written with 'with'\n")
# again, automatically closed -- no explicit .close() needed


# --- CSV files: comma-separated tabular data ---
# a plain-text format where each line is a row, and commas separate the
# columns within that row. Special case: a value that itself CONTAINS a
# comma gets wrapped in double quotes, so the comma inside it isn't
# mistaken for a column separator. products.csv has one such row:
#   "Deluxe, Widget",3,45.00


# --- Method 1: naive string splitting (fragile) ---
print("\n--- naive split ---")
with open("products.csv", "r") as file:
    header = file.readline()               # skip/consume the header row
    for line in file:
        parts = line.strip().split(",")
        print(parts)
        # notice "Deluxe, Widget" gets INCORRECTLY split into two pieces
        # here -- naive splitting doesn't understand quoted commas


# --- Method 2: csv.reader (handles quoting correctly) ---
print("\n--- csv.reader ---")
with open("products.csv", "r") as file:
    reader = csv.reader(file)
    header = next(reader)                  # grab the header row
    print("header:", header)
    for row in reader:
        print(row)
        # "Deluxe, Widget" now stays as ONE field, correctly


# --- Method 3: csv.DictReader (most elegant) ---
# each row comes back as a dictionary, keyed by the column names from
# the header row -- no manual index tracking needed
print("\n--- csv.DictReader ---")
with open("products.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row)
        print(row["product"], row["quantity"], row["price"])


# --- Practical exercise: total revenue per product ---
print("\n--- total revenue per product ---")
with open("products.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        quantity = int(row["quantity"])
        price = float(row["price"])       # CSV values are always strings --
        revenue = quantity * price         # must convert before doing math
        print(f"{row['product']}: ${revenue:.2f}")
