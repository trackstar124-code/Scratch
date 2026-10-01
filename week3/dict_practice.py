inventory = {"apples": 12, "bananas": 5, "cherries": 30}

# 1. Print the number of bananas using a key lookup.
bannnas = inventory["bananas"]
print(bannnas)

# 2. Use .get() to print the count of "grapes" -- it's not in the
#    dictionary, so make it default to 0 instead of crashing.

print(inventory.get("grapes", 0))

# 3. Add "grapes" to inventory with a count of 20.
inventory["grapes"] = 20
print(inventory["grapes"])

# 4. Someone eats 3 apples. Update the "apples" value to reflect that
#    (don't just retype the number -- subtract from the existing value).

inventory["apples"] = inventory["apples"] - 3 
print(inventory["apples"])

# 5. Loop over inventory and print each item along with its count,
#    formatted like: "apples: 9"

for key, value in inventory.items():
    print(f"{key}: {value}")

# 6. Print the total count of all items combined (sum of all the values).

x = sum(inventory.values())
print(x)

# 7. Given this list of fruit purchases, build a NEW dictionary that
#    counts how many times each fruit appears (same pattern as the
#    word-counting example in dictionaries_demo.py).
purchases = ["apple", "banana", "apple", "cherry", "apple", "banana"]

count = {}
for purchase in purchases:
    count[purchase] = count.get(purchase, 0) + 1

print(count)
