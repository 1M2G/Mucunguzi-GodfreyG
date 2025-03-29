# Basic for loop iterating through a list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
# Output:
# apple
# banana
# cherry

print("-" * 20)

# For loop with range() to iterate a specific number of times
for i in range(5):  # Generates numbers from 0 to 4
    print(i)
# Output:
# 0
# 1
# 2
# 3
# 4

print("-" * 20)

# For loop with range() specifying start and end
for i in range(2, 7):  # Generates numbers from 2 to 6
    print(i)
# Output:
# 2
# 3
# 4
# 5
# 6

print("-" * 20)

# For loop with range() specifying start, end, and step
for i in range(0, 10, 2):  # Generates even numbers from 0 to 8
    print(i)
# Output:
# 0
# 2
# 4
# 6
# 8

print("-" * 20)

# For loop iterating through a string (each character)
message = "Hello"
for char in message:
    print(char)
# Output:
# H
# e
# l
# l
# o

print("-" * 20)

# For loop with an else block (executes after the loop finishes normally)
for i in range(3):
    print(f"Loop iteration: {i}")
else:
    print("Loop finished without any breaks.")
# Output:
# Loop iteration: 0
# Loop iteration: 1
# Loop iteration: 2
# Loop finished without any breaks.

print("-" * 20)

# For loop with break statement (exits the loop prematurely)
numbers = [1, 2, 3, 4, 5]
for num in numbers:
    if num == 3:
        print("Found 3! Exiting loop.")
        break
    print(f"Checking number: {num}")
# Output:
# Checking number: 1
# Checking number: 2
# Found 3! Exiting loop.

print("-" * 20)

# For loop with continue statement (skips the current iteration)
numbers = [1, 2, 3, 4, 5]
for num in numbers:
    if num == 3:
        print("Skipping 3.")
        continue
    print(f"Processing number: {num}")
# Output:
# Processing number: 1
# Processing number: 2
# Skipping 3.
# Processing number: 4
# Processing number: 5

print("-" * 20)

# Nested for loops (loop inside another loop)
for i in range(2):
    for j in range(3):
        print(f"i: {i}, j: {j}")
# Output:
# i: 0, j: 0
# i: 0, j: 1
# i: 0, j: 2
# i: 1, j: 0
# i: 1, j: 1
# i: 1, j: 2

print("-" * 20)

# Iterating through a dictionary (keys by default)
student = {"name": "Alice", "age": 20, "major": "Computer Science"}
for key in student:
    print(key)
# Output:
# name
# age
# major

print("-" * 20)

# Iterating through dictionary items (key-value pairs)
for key, value in student.items():
    print(f"Key: {key}, Value: {value}")
# Output:
# Key: name, Value: Alice
# Key: age, Value: 20
# Key: major, Value: Computer Science

print("-" * 20)

# Iterating through dictionary values
for value in student.values():
    print(value)
# Output:
# Alice
# 20
# Computer Science

print("-" * 20)

# Using enumerate to get both index and value
colors = ["red", "green", "blue"]
for index, color in enumerate(colors):
    print(f"Index: {index}, Color: {color}")
# Output:
# Index: 0, Color: red
# Index: 1, Color: green
# Index: 2, Color: blue
