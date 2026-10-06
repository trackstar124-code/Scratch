# LAB EXERCISE 03

# SET UP BEGINS - Do Not Modify
employees = [
        {"name": "Alice", "department": "Engineering", "years_experience": 5},
        {"name": "Ann", "department": "Marketing", "years_experience": 4},
        {"name": "Ben", "department": "Engineering", "years_experience": 2},
        {"name": "Bob", "department": "Engineering", "years_experience": 6},
        {"name": "Eve", "department": "HR", "years_experience": 3},
    ]

pairs = [(5, 2), (1, 4), (3, 1), (2, 9)]
# SET UP ENDS - Do Not Modify

# PROBLEM 01
def count_ints(lst, target):
    """Return the number of times the target appears in the list"""
    count = 0
    for row in lst:
        for value in row:
            if value == target:
                count += 1
    return count

# PROBLEM 02
def remove_duplicates(lst):
    """returns a new list that removes the duplicates from the order"""
    result = []
    for item in lst:
        if item not in result:
            result.append(item)
    return result

# PROBLEM 03
def filter_employees(emps):
    """Returns the employees with at least more than 3 years of experience"""
    return [e["name"] for e in emps
            if e["department"] == "Engineering" and e["years_experience"] > 3]

# PROBLEM 04
def function_p4(tuples):
    """Return a list of (a, b, a*b) tuples for each (a, b) pair"""
    return [(a, b, a * b) for a, b in tuples]

# PROBLEM 05
def function_p5(tuples):
    """Returns a list of tuples soreted ascending by each tuple's second element"""
    return sorted(tuples, key=lambda t: t[1])

# PROBLEM 06
def function_p6(tuples):
    """Return the list of tuples sorted descending by the sum of each tuple."""
    return sorted(tuples, key=lambda t: sum(t), reverse=True)

def main():
    print(count_ints([[-1, -2, -3], [4, 5, 6]], 8))
    print(count_ints([[-1, -2, -3], [-1, 5, 6]], -1))
    print(count_ints([[-1, -2, -3, 4, 4], [4, 5, 6]], 4))
    print(remove_duplicates([1, 1]))
    print(remove_duplicates([1, 2, 3]))
    print(remove_duplicates([3, 1, 2, 3, 2]))
    print(filter_employees(employees))
    print(function_p4(pairs))
    print(function_p5(pairs))
    print(function_p6(pairs))

if __name__ == "__main__":
    main()




