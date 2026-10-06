counts = {}
for word in ["cat", "dog", "cat", "bird", "cat"]:
    if word in counts:
        counts[word] += 1
    else:
        counts[word] = 1
print(counts["cat"], len(counts))