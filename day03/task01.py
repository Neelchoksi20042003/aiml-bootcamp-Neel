from functools import reduce
from itertools import chain, accumulate

# TASK 01
# Given a list of numbers, return the squares of only the odd ones

nums = [1, 2, 3, 4, 5, 6, 7]

# Loop version
out_loop = []

for n in nums:
    if n % 2 == 1:
        out_loop.append(n * n)

print("Task 01 - Loop:", out_loop)

# Functional version
out_functional = [
    n * n
    for n in nums
    if n % 2 == 1
]

print("Task 01 - Functional:", out_functional)

# Preference: I prefer the functional version because it is shorter
# while still being easy to understand.
# TASK 02
# Given a list of names, uppercase and strip whitespace

names = [" alice ", "BOB ", " charlie", " David "]

# Loop version
out_loop = []

for name in names:
    out_loop.append(name.strip().upper())

print("\nTask 02 - Loop:", out_loop)

# Functional version
out_functional = [
    name.strip().upper()
    for name in names
]

print("Task 02 - Functional:", out_functional)

# Preference: I prefer the functional version because the transformation
# is simple and can be clearly expressed in one line.
# TASK 03
# Given two lists of equal length, return pairwise products

a = [1, 2, 3, 4]
b = [10, 20, 30, 40]

# Loop version
out_loop = []

for x, y in zip(a, b):
    out_loop.append(x * y)

print("\nTask 03 - Loop:", out_loop)

# Functional version
out_functional = [
    x * y
    for x, y in zip(a, b)
]

print("Task 03 - Functional:", out_functional)

# Preference: I prefer the functional version because zip makes the
# pairwise operation very clear.
# TASK 04
# Given a list of words, return only those longer than 4 characters

words = [
    "cat",
    "python",
    "data",
    "machine",
    "AI",
    "model"
]

# Loop version
out_loop = []

for word in words:
    if len(word) > 4:
        out_loop.append(word)

print("\nTask 04 - Loop:", out_loop)

# Functional version
out_functional = [
    word
    for word in words
    if len(word) > 4
]

print("Task 04 - Functional:", out_functional)

# Preference: I prefer the functional version because filtering a list
# with one condition is very readable as a comprehension.
# TASK 05
# Given a list of numbers, find the product of all numbers
# Must use reduce

nums = [1, 2, 3, 4, 5]

# Loop version
product_loop = 1

for n in nums:
    product_loop *= n

print("\nTask 05 - Loop:", product_loop)


# Functional version
product_functional = reduce(
    lambda x, y: x * y,
    nums
)

print("Task 05 - Functional:", product_functional)

# Preference: I prefer the loop version because multiplication with
# reduce is less immediately readable for beginners.
# TASK 06
# Given a list of dictionaries with a "price" key,
# return the total price

products = [
    {"name": "Laptop", "price": 50000},
    {"name": "Mouse", "price": 1000},
    {"name": "Keyboard", "price": 2000},
    {"name": "Monitor", "price": 15000}
]

# Loop version
total_loop = 0

for product in products:
    total_loop += product["price"]

print("\nTask 06 - Loop:", total_loop)

# Functional version
total_functional = sum(
    product["price"]
    for product in products
)

print("Task 06 - Functional:", total_functional)

# Preference: I prefer the functional version because sum directly
# communicates that we are adding all prices.
# TASK 07
# Flatten [[1,2],[3,4],[5]] to [1,2,3,4,5]

nested = [
    [1, 2],
    [3, 4],
    [5]
]

# Loop version
out_loop = []

for sublist in nested:
    for item in sublist:
        out_loop.append(item)

print("\nTask 07 - Loop:", out_loop)

# Functional version using itertools.chain
out_functional = list(chain.from_iterable(nested))

print("Task 07 - Functional:", out_functional)

# Preference: I prefer chain.from_iterable because it directly expresses
# the operation of flattening one level of nested lists.
# TASK 08
# Given a list of strings, return a dict mapping each string to its length

strings = [
    "python",
    "AI",
    "machine",
    "data"
]

# Loop version
out_loop = {}

for string in strings:
    out_loop[string] = len(string)

print("\nTask 08 - Loop:", out_loop)

# Functional-style version
out_functional = {
    string: len(string)
    for string in strings
}

print("Task 08 - Functional:", out_functional)

# Preference: I prefer the dictionary comprehension because the key-value
# relationship is immediately visible.
# TASK 09
# Given mixed values, drop everything falsy

values = [
    10,
    0,
    "hello",
    "",
    None,
    [],
    [1, 2],
    False,
    25
]

# Loop version
out_loop = []

for value in values:
    if value:
        out_loop.append(value)

print("\nTask 09 - Loop:", out_loop)

# Functional version
out_functional = [
    value
    for value in values
    if value
]

print("Task 09 - Functional:", out_functional)

# Preference: I prefer the functional version because the condition
# "if value" clearly communicates that falsy values are removed.
# TASK 10
# Running total: [1,2,3] -> [1,3,6]

nums = [1, 2, 3]

# Loop version
out_loop = []
running_total = 0

for n in nums:
    running_total += n
    out_loop.append(running_total)

print("\nTask 10 - Loop:", out_loop)

# Functional version using itertools.accumulate
out_functional = list(accumulate(nums))
print("Task 10 - Functional:", out_functional)

# Preference: I prefer accumulate because running totals are exactly
# what accumulate is designed to calculate.
# FINAL CHECK

print("\n========================================")
print("ALL TASKS COMPLETED")
print("========================================")