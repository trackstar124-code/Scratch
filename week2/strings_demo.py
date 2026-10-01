"""
Demo: strings for DS 2500
"""

# --- Creating strings ---
single = 'hello'
double = "hello"      # single and double quotes are equivalent in Python

# triple quotes for multi-line strings
multi_line = """This spans
multiple lines
in the source code."""
print(multi_line)


# --- Concatenation ---
first = "Data"
second = "Science"
print(first + " " + second)          # + operator

parts = ["Data", "Science", "2500"]
print(" ".join(parts))               # .join() -- better for combining
                                      # many pieces, especially from a list


# --- Length ---
word = "python"
print(len(word))     # 6


# --- Indexing ---
# each character has a position, starting at 0
print(word[0])       # 'p' -- first character
print(word[5])       # 'n' -- last character

# negative indices count from the END
print(word[-1])      # 'n' -- last character (cleaner than word[len(word)-1])
print(word[-2])      # 'o' -- second to last


# --- Slicing: word[start:stop] -- stop is EXCLUSIVE, same rule as range() ---
print(word[0:3])     # 'pyt'
print(word[2:])      # 'thon' -- omit stop to go to the end
print(word[:3])      # 'pyt' -- omit start to go from the beginning
print(word[:])       # 'python' -- a full copy of the string
print(word[-3:])     # 'hon' -- last 3 characters


# --- Strings are immutable ---
# you CANNOT change a character in place -- this would raise a TypeError:
# word[0] = "P"
# instead, build a NEW string and reassign it to the variable
word = "P" + word[1:]
print(word)           # 'Python' -- word now points to a brand-new string


# --- Membership: in ---
sentence = "the quick brown fox"
print("quick" in sentence)     # True
print("slow" in sentence)      # False


# --- startswith / endswith ---
filename = "report.csv"
print(filename.startswith("report"))   # True
print(filename.endswith(".csv"))       # True
print(filename.endswith(".txt"))       # False


# --- Case conversion ---
text = "Hello World"
print(text.upper())        # 'HELLO WORLD'
print(text.lower())        # 'hello world'
print(text.capitalize())   # 'Hello world' -- only first letter of whole string
print(text.title())        # 'Hello World' -- first letter of EVERY word

# remember: these all return a NEW string, they don't modify `text` itself
print(text)                 # still 'Hello World'


# --- Stripping whitespace ---
messy = "   padded text   \n"
print(repr(messy.strip()))    # removes whitespace from BOTH ends
print(repr(messy.lstrip()))   # only the LEFT side
print(repr(messy.rstrip()))   # only the RIGHT side


# --- find / index: locating a substring ---
phrase = "the cat sat on the mat"
print(phrase.find("cat"))      # 4 -- index where "cat" starts
print(phrase.find("dog"))      # -1 -- not found, .find() returns -1
# print(phrase.index("dog"))   # would raise a ValueError instead of -1


# --- count ---
print(phrase.count("at"))      # 3 -- "cat", "sat", "mat" all contain "at"
print(phrase.count("the"))     # 2


# --- replace ---
print(phrase.replace("cat", "dog"))    # replaces ALL occurrences
print(phrase)                           # unchanged -- replace() returns new string


# --- split: breaking a string into a list of pieces ---
csv_line = "Vance,22,DS"
print(csv_line.split(","))       # ['Vance', '22', 'DS']

sentence2 = "the quick brown fox"
print(sentence2.split())          # splits on whitespace by default
                                   # -> ['the', 'quick', 'brown', 'fox']


# --- String formatting: three approaches ---
name = "Vance"
age = 22

# 1. f-strings -- modern, most readable, recommended
print(f"{name} is {age} years old")
print(f"Next year: {age + 1}")            # expressions work directly inside {}
print(f"{3.14159:.2f}")                   # formatting a float to 2 decimal places

# 2. .format() -- older, still common in existing code
print("{} is {} years old".format(name, age))

# 3. % operator -- oldest style, from before .format()/f-strings existed
print("%s is %d years old" % (name, age))
