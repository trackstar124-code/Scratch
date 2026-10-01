#start with a list [1, 9, 7, 7, 6] and return a list of unique elements sorted in reverse order

data = ([1, 9, 7, 7, 6])

term = set(data)
result = sorted(term, reverse=True)

print(result)

