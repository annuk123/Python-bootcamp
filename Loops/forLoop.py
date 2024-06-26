# The for loop is used to iterate over a sequence (list, tuple, string) and execute a block of code for each element in the sequence.
# The for loop does not require an indexing variable to set beforehand.
# The for loop can iterate over a sequence of numbers using the range() function.
# The range() function generates a sequence of numbers starting from 0 by default, and increments by 1 (by default), and stops before a specified number.
# The range() function can take up to three arguments: range(start, stop, step).
# The range() function can generate a sequence of numbers starting from the start argument, and increments by the step argument, and stops before the stop argument.

#syntax: for item in sequence:
# for item in sequence:
    # Do something with item

# item is a variable that takes the value of the current element in the sequence.
# sequence is the collection of items you are iterating over (like a list, tuple, string, or range).
# The indented block of code below the for statement is executed once for each item in the sequence.

# Example 1: Iterating over a list
# Iterate over a list of items and print each item.
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# Output
# apple
# banana
# cherry

# Example 2: Iterating over a string
# Iterate over a string and print each character.
for letter in "banana":
    print(letter)

# Output
# b
# a
# n
# a
# n
# a

# Example 3: Iterating over a tuple
# Iterate over a tuple of items and print each item.
colors = ("red", "green", "blue")
for color in colors:
    print(color)

# Output
# red
# green
# blue

# Example 4: Iterating over a range
# Iterate over a sequence of numbers using the range() function.
for number in range(5):
    print(number)

# Output
# 0
# 1
# 2
# 3
# 4

# Example 5: Iterating over a range with start and stop arguments
# Iterate over a sequence of numbers starting from 2 to 5 (exclusive).
for number in range(2, 5):
    print(number)

# Output
# 2
# 3
# 4

# Example 6: Iterating over a range with start, stop, and step arguments
# Iterate over a sequence of numbers starting from 1 to 10 (exclusive) by 2.
for number in range(1, 10, 2):
    print(number)

# Output
# 1
# 3
# 5
# 7
# 9

# Example 7: Iterating over a range in reverse
# Iterate over a sequence of numbers in reverse starting from 5 to 1.
for number in range(5, 0, -1):
    print(number)

# Output
# 5
# 4
# 3
# 2
# 1

# Example 8: Iterating over a list of tuples
# Iterate over a list of tuples and print each item in the tuple.
students = [("Alice", 25), ("Bob", 30), ("Charlie", 35)]
for student in students:
    name, age = student
    print(f"{name} is {age} years old.")

# Output
# Alice is 25 years old.
# Bob is 30 years old.
# Charlie is 35 years old.

# Example 9: Iterating over a dictionary
# Iterate over a dictionary and print each key-value pair.
person = {"name": "Alice", "age": 25}
for key, value in person.items():
    print(f"{key}: {value}")

# Output
# name: Alice
# age: 25

# Example 10: Iterating over a dictionary keys
# Iterate over a dictionary and print each key.

person = {"name": "Alice", "age": 25}
for key in person.keys():
    print(key)

# Output
# name
# age

# Example 11: Iterating over a dictionary values
# Iterate over a dictionary and print each value.
person = {"name": "Alice", "age": 25}
for value in person.values():
    print(value)

# Output
# Alice
# 25

# Example 12: Iterating over a dictionary keys and values
# Iterate over a dictionary and print each key and value.
person = {"name": "Alice", "age": 25}
for key, value in person.items():
    print(f"{key}: {value}")

# Output
# name: Alice
# age: 25

# Using enumerate()
# The enumerate() function adds a counter to an iterable and returns it as an enumerate object. This is useful when you need both the index and the value from the sequence.
# The enumerate() function takes two arguments: enumerate(iterable, start).
# The iterable is the sequence you want to iterate over.
# The start is an optional argument that specifies the start value of the counter. By default, it is 0.
# The enumerate object can be converted to a list of tuples using the list() function.
#syntax: for index, item in enumerate(sequence):
# for index, item in enumerate(sequence):
    # Do something with index and item

# Example 13: Using enumerate() with a list
# Iterate over a list of items and print the index and item.
fruits = ["apple", "banana", "cherry"]
for index, fruit in enumerate(fruits):
    print(index, fruit)

#     Using zip()
# The zip() function takes two or more iterables and returns an iterator that generates tuples of elements from the iterables.
# The zip() function stops when the shortest input iterable is exhausted.
# The zip() function can take any number of arguments, and it returns an iterator that generates tuples containing elements from each iterable.
# The zip() function can be converted to a list of tuples using the list() function.
#syntax: for item1, item2 in zip(sequence1, sequence2):
# for item1, item2 in zip(sequence1, sequence2):
    # Do something with item1 and item2

# Example 14: Using zip() with two lists
# Iterate over two lists of items and print the items.
fruits = ["apple", "banana", "cherry"]
colors = ["red", "yellow", "blue"]
for fruit, color in zip(fruits, colors):
    print(fruit, color)

# Output
# apple red
# banana yellow
# cherry blue

# Example 15: Using zip() with three lists
# Iterate over three lists of items and print the items.
fruits = ["apple", "banana", "cherry"]
colors = ["red", "yellow", "blue"]
weights = [100, 200, 300]
for fruit, color, weight in zip(fruits, colors, weights):
    print(fruit, color, weight)

# Output
# apple red 100
# banana yellow 200
# cherry blue 300

# Using reversed()
# The reversed() function returns an iterator that accesses the given sequence in the reverse order.
# The reversed() function can be used to iterate over a sequence in reverse.

# Example 16: Using reversed() with a list
# Iterate over a list of items in reverse.
fruits = ["apple", "banana", "cherry"]
for fruit in reversed(fruits):
    print(fruit)

# Output
# cherry
# banana
# apple

# Using sorted()
# The sorted() function returns a new sorted list from the elements of any iterable.
# The sorted() function can be used to iterate over a sequence in sorted order.

# Example 17: Using sorted() with a list
# Iterate over a list of items in sorted order.
fruits = ["banana", "cherry", "apple"]
for fruit in sorted(fruits):
    print(fruit)

# Output
# apple
# banana
# cherry

# Using set()
# The set() function returns a new set object from the elements of any iterable.
# The set() function can be used to iterate over a sequence of unique elements.

# Example 18: Using set() with a list
# Iterate over a list of unique items.
fruits = ["apple", "banana", "cherry", "apple"]
for fruit in set(fruits):
    print(fruit)

# Output
# cherry
# banana
# apple

# Using break
# The break statement is used to exit the loop prematurely.
# The break statement can be used to stop the loop before it has looped through all the items.
# The break statement can be used inside a loop to exit the loop when a certain condition is met.

# Example 19: Using break to exit the loop
# Iterate over a list of items and exit the loop when the item is "banana".
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
    if fruit == "banana":
        break

# Output
# apple
# banana

# Using continue
# The continue statement is used to skip the rest of the code inside a loop for the current iteration.
# The continue statement can be used to skip the current iteration and continue with the next iteration.
# The continue statement can be used inside a loop to skip the rest of the code inside the loop for the current iteration.

# Example 20: Using continue to skip the current iteration
# Iterate over a list of items and skip the item "banana".
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    if fruit == "banana":
        continue
    print(fruit)

# Output
# apple
# cherry

# Using else
# The else statement can be used in a loop to run a block of code once when the loop is finished.
# The else statement can be used to execute a block of code after the loop has finished iterating over the items.
# The else statement can be used in a loop to run a block of code once when the loop is finished, but not when the loop is terminated by a break statement.

# Example 21: Using else in a loop
# Iterate over a list of items and print a message when the loop has finished.
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
else:
    print("Finished!")

# Output
# apple
# banana
# cherry
# Finished!

# Example 22: Using else with a break statement
# Iterate over a list of items and print a message when the loop has finished.
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
    if fruit == "banana":
        break
else:
    print("Finished!")

# Output
# apple
# banana

# Using pass
# The pass statement is used as a placeholder for future code.
# The pass statement can be used to avoid getting an error when the code is empty.
# The pass statement can be used to avoid getting an error when the code is not implemented yet.

# Example 23: Using pass as a placeholder
# Iterate over a list of items and do nothing.
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    pass

# Output
# (no output)

# Nested for Loop
# A nested loop is a loop inside another loop.
# The inner loop will be executed one time for each iteration of the outer loop.
# The nested loop can be used to iterate over a sequence of items for each item in the outer loop.
#syntax: for item in sequence:
    # for item in sequence:
        # Do something with item

# Example 24: Using a nested for loop
# Iterate over a list of items and a list of colors.
fruits = ["apple", "banana", "cherry"]
colors = ["red", "yellow", "blue"]
for fruit in fruits:
    for color in colors:
        print(fruit, color)

# Output
# apple red
# apple yellow
# apple blue
# banana red
# banana yellow
# banana blue
# cherry red
# cherry yellow
# cherry blue

# Using List Comprehension
# List comprehension is a concise way to create lists in Python.
# List comprehension offers a shorter syntax when you want to create a new list by iterating over a sequence.
# List comprehension is faster than using a for loop to create a list.
#syntax: new_list = [expression for item in sequence]
# new_list: The new list you want to create.
# expression: The operation you want to perform on each item in the sequence.
# item: The variable representing each item in the sequence.

# Example 25: Using list comprehension
# Create a new list of items by iterating over a sequence.
fruits = ["apple", "banana", "cherry"]
new_list = [fruit.upper() for fruit in fruits]
print(new_list)

# Output
# ['APPLE', 'BANANA', 'CHERRY']

# Example 26: Using list comprehension with if condition
# Create a new list of items by iterating over a sequence and applying a condition.
fruits = ["apple", "banana", "cherry"]
new_list = [fruit for fruit in fruits if fruit != "banana"]
print(new_list)

# Output
# ['apple', 'cherry']

# Example 27: Using list comprehension with if else condition
# Create a new list of items by iterating over a sequence and applying a condition.
fruits = ["apple", "banana", "cherry"]
new_list = [fruit if fruit != "banana" else "orange" for fruit in fruits]
print(new_list)

# Output
# ['apple', 'orange', 'cherry']

# Example 28: Using list comprehension with nested for loop
# Create a new list of items by iterating over two sequences.
fruits = ["apple", "banana", "cherry"]
colors = ["red", "yellow", "blue"]
new_list = [(fruit, color) for fruit in fruits for color in colors]
print(new_list)

# Output
# [('apple', 'red'), ('apple', 'yellow'), ('apple', 'blue'), ('banana', 'red'), ('banana', 'yellow'), ('banana', 'blue'), ('cherry', 'red'), ('cherry', 'yellow'), ('cherry', 'blue')]
# In this example, we created a list of tuples containing each fruit and color combination using a nested for loop in list comprehension.

# Example 29: Using list comprehension with enumerate()
# Create a new list of items by iterating over a sequence with the index.
fruits = ["apple", "banana", "cherry"]
new_list = [(index, fruit) for index, fruit in enumerate(fruits)]
print(new_list)

# Output
# [(0, 'apple'), (1, 'banana'), (2, 'cherry')]
# In this example, we created a list of tuples containing the index and item using the enumerate() function in list comprehension.

# Example 30: Using list comprehension with zip()
# Create a new list of items by iterating over two sequences.
fruits = ["apple", "banana", "cherry"]
colors = ["red", "yellow", "blue"]
new_list = [(fruit, color) for fruit, color in zip(fruits, colors)]
print(new_list)

# Output
# [('apple', 'red'), ('banana', 'yellow'), ('cherry', 'blue')]
# In this example, we created a list of tuples containing each fruit and color combination using the zip() function in list comprehension.

# Example 31: Using list comprehension with if condition
# Create a new list of items by iterating over a sequence and applying a condition.
numbers = [1, 2, 3, 4, 5]
new_list = [number for number in numbers if number % 2 == 0]
print(new_list)

# Output
# [2, 4]
# In this example, we created a new list of even numbers by iterating over a sequence and applying a condition using list comprehension.

# Example 32: Using list comprehension with if else condition
# Create a new list of items by iterating over a sequence and applying a condition.
numbers = [1, 2, 3, 4, 5]
new_list = ["even" if number % 2 == 0 else "odd" for number in numbers]
print(new_list)

# Output
# ['odd', 'even', 'odd', 'even', 'odd']
# In this example, we created a new list of even and odd numbers by iterating over a sequence and applying a condition using list comprehension.

# Example 33: Using list comprehension with nested for loop
# Create a new list of items by iterating over two sequences.
numbers = [1, 2, 3]
colors = ["red", "white"]
new_list = [(number, color) for number in numbers for color in colors]
print(new_list)

# Output
# [(1, 'red'), (1, 'white'), (2, 'red'), (2, 'white'), (3, 'red'), (3, 'white')]
# In this example, we created a list of tuples containing each number and color combination using a nested for loop in list comprehension.


# Using map()
# The map() function applies a given function to each item of an iterable (list, tuple, etc.) and returns a list of the results.
# The map() function takes two arguments: map(function, iterable).
# The function is the operation you want to perform on each item in the iterable.
# The iterable is the sequence you want to iterate over.
# The map() function can be used to apply a function to each item in a sequence and return a list of the results.
#syntax: new_list = list(map(function, iterable))
# new_list: The new list you want to create.
# function: The operation you want to perform on each item in the iterable.
# iterable: The sequence you want to iterate over.

# Example 34: Using map() with a function
# Create a new list of items by applying a function to each item in a sequence.
def square(number):
    return number ** 2

numbers = [1, 2, 3, 4, 5]
new_list = list(map(square, numbers))
print(new_list)

# Output
# [1, 4, 9, 16, 25]
# In this example, we created a new list of squared numbers by applying the square() function to each item in the numbers list using the map() function.

# Example 35: Using map() with lambda function
# Create a new list of items by applying a lambda function to each item in a sequence.
numbers = [1, 2, 3, 4, 5]
new_list = list(map(lambda number: number ** 2, numbers))
print(new_list)

# Output
# [1, 4, 9, 16, 25]
# In this example, we created a new list of squared numbers by applying a lambda function to each item in the numbers list using the map() function.


# Using filter()
# The filter() function constructs an iterator from elements of an iterable for which a function returns true.
# The filter() function takes two arguments: filter(function, iterable).
# The function is the operation you want to perform on each item in the iterable.
# The iterable is the sequence you want to iterate over.
# The filter() function can be used to filter elements from a sequence based on a condition.
#syntax: new_list = list(filter(function, iterable))
# new_list: The new list you want to create.
# function: The operation you want to perform on each item in the iterable.
# iterable: The sequence you want to iterate over.

# Example 36: Using filter() with a function
# Create a new list of items by filtering elements from a sequence based on a condition.
def is_even(number):
    return number % 2 == 0

numbers = [1, 2, 3, 4, 5]
new_list = list(filter(is_even, numbers))
print(new_list)

# Output
# [2, 4]
# In this example, we created a new list of even numbers by filtering elements from the numbers list based on a condition using the filter() function.

# Example 37: Using filter() with lambda function
# Create a new list of items by filtering elements from a sequence based on a condition.
numbers = [1, 2, 3, 4, 5]
new_list = list(filter(lambda number: number % 2 == 0, numbers))
print(new_list)

# Output
# [2, 4]
# In this example, we created a new list of even numbers by filtering elements from the numbers list based on a condition using the filter() function.

# Using reduce()
# The reduce() function applies a rolling computation to sequential pairs of values in an iterable and returns a single result.
# The reduce() function is part of the functools module.
# The reduce() function takes two arguments: reduce(function, iterable).
# The function is the operation you want to perform on each item in the iterable.
# The iterable is the sequence you want to iterate over.
# The reduce() function can be used to apply a function to each item in a sequence and reduce the sequence to a single value.
#syntax: result = reduce(function, iterable)
# result: The single result you want to get.
# function: The operation you want to perform on each item in the iterable.
# iterable: The sequence you want to iterate over.

# Example 38: Using reduce() with a function
# Create a single result by applying a function to each item in a sequence.
from functools import reduce

def add(x, y):
    return x + y

numbers = [1, 2, 3, 4, 5]
result = reduce(add, numbers)
print(result)

# Output
# 15
# In this example, we created a single result by applying the add() function to each item in the numbers list using the reduce() function.

# Example 39: Using reduce() with lambda function
# Create a single result by applying a lambda function to each item in a sequence.
from functools import reduce

numbers = [1, 2, 3, 4, 5]
result = reduce(lambda x, y: x + y, numbers)
print(result)

# Output
# 15
# In this example, we created a single result by applying a lambda function to each item in the numbers list using the reduce() function.

# Using itertools
# The itertools module provides a collection of functions for working with iterators.

# Example 40: Using itertools.count()
# Create an infinite iterator that counts from a specified number.
import itertools

for number in itertools.count(5):
    print(number)
    if number == 10:
        break

# Output
# 5
# 6
# 7
# 8
# 9
# 10
# In this example, we created an infinite iterator that counts from 5 using the count() function from the itertools module.

# Example 41: Using itertools.cycle()
# Create an infinite iterator that cycles through a sequence of items.
import itertools

colors = ["red", "green", "blue"]
for color in itertools.cycle(colors):
    print(color)
    if color == "blue":
        break

# Output
# red
# green
# blue
# red
# green
# blue
# In this example, we created an infinite iterator that cycles through the colors list using the cycle() function from the itertools module.

# Example 42: Using itertools.repeat()
# Create an infinite iterator that repeats a specified value.
import itertools

for number in itertools.repeat(5):
    print(number)
    if number == 10:
        break

# Output
# 5
# 5
# 5
# 5
# 5
# 5
# 5
# 5
# 5
# 5
# In this example, we created an infinite iterator that repeats the number 5 using the repeat() function from the itertools module.


# Using Generators
# A generator is a special type of iterator that generates values on the fly.
# A generator is a function that returns an iterator.
# A generator uses the yield keyword to return the next value in the sequence.
# A generator can be used to iterate over a sequence of items one at a time.
#syntax: def generator():
    # yield value
    
# Example 43: Using a generator
# Create a generator that generates a sequence of numbers.
def generator():
    yield 1
    yield 2
    yield 3

g = generator()
print(next(g))
print(next(g))
print(next(g))

# Output
# 1
# 2
# 3
# In this example, we created a generator that generates a sequence of numbers using the yield keyword.

# Example 44: Using a generator with a loop
# Create a generator that generates a sequence of numbers.
def generator():
    for number in range(1, 4):
        yield number

g = generator()
for number in g:
    print(number)

# Output
# 1
# 2
# 3
# In this example, we created a generator that generates a sequence of numbers using the yield keyword and iterated over the generator using a loop.

# Example 45: Using a generator expression
# Create a generator that generates a sequence of numbers.
g = (number for number in range(1, 4))
for number in g:
    print(number)

# Output
# 1
# 2
# 3
# In this example, we created a generator that generates a sequence of numbers using a generator expression.

# Example 46: Using a generator with a function
# Create a generator that generates a sequence of numbers.
def generator(n):
    for number in range(1, n + 1):
        yield number

g = generator(3)
for number in g:
    print(number)

# Output
# 1
# 2
# 3
# In this example, we created a generator that generates a sequence of numbers using the yield keyword in a function.










