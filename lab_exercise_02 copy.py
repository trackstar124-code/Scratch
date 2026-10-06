# LAB EXERCISE 02

# PROBLEM 01

sum_1_1000 = 0
for i in range(1, 1001):
    sum_1_1000 += i
print(sum_1_1000)

sum_odd_1_2501 = 0
for i in range(1, 2502, 2):
    sum_odd_1_2501 += i
print(sum_odd_1_2501)

# PROBLEM 02

fruits = ["apple", "pear", "grapes", "peach"]

letter2fruits = {}

for fruit in fruits:
    letter = fruit[0]

    if letter in letter2fruits:
        letter2fruits[letter].append(fruit)
    else:
        letter2fruits[letter] = [fruit]

common_letters = []

for letter in fruits[0]:
    if letter not in common_letters and all(letter in fruit for fruit in fruits[1:]):
        common_letters.append(letter)


# PROBLEM 03
numbers = [6, 7, 8, 9, 10]

total_sum = 0
i = 0

while i < len(numbers) and total_sum < 2500:
    total_sum += numbers[i]
    i += 1

numbers = [1, 2, 3, 4, 5, 6]

limited_sum = 0
i = 0

while i < len(numbers):
    if numbers[i] % 2 == 0:
        break
    else:
        limited_sum += numbers[i]
        i += 1


# PROBLEM 04

### SETUP BEGINS -- DO NOT MODIFY

course_description = "Offers intermediate to advanced Python programming for data science. Covers object oriented design patterns using Python, including encapsulation, composition,  and inheritance. Advanced programming skills cover software architecture, recursion, profiling, unit testing and  debugging, lineage and data provenance, using advanced integrated development environments, and software  control systems. Uses case studies to survey key concepts in data science with an emphasis on machine learning (classification,  clustering, deep learning); data visualization; and natural language processing. Additional assigned readings survey topics in Ethics, Model Bias, and Data Privacy pertinent to todays Big Data  world. Offers students an opportunity to prepare for more advanced courses in data science and to enable practical contributions to software  development and data science projects  in  a  commercial setting. "

### SETUP ENDS -- DO NOT MODIFY

import string

cleaned = course_description.lower()
for char in string.punctuation:
    cleaned = cleaned.replace(char, "")

words = cleaned.split(" ")

word2count = {}
for word in words:
    if word != "":
        if word in word2count:
            word2count[word] += 1
        else:
            word2count[word] = 1

print(words)
print(word2count)