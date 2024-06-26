#In Python, there is no built-in `do-while` loop, but you can mimic its behavior using a `while` loop. However, Python does support `for` loops that can iterate over sequences, effectively providing a `for-each` loop functionality.

### Mimicking `do-while` Loop

#A `do-while` loop ensures that the loop body is executed at least once before the condition is checked. To achieve this in Python, you can use a `while` loop with a `break` condition inside.

#### Example of Mimicking `do-while` Loop

#python
#while True:
    # Loop body
    #print("This will run at least once.")
    
    # Condition to exit the loop
    # if some_condition:
    #     break

#### Practical Example

#python
count = 0
while True:
    count += 1
    print(count)
    if count >= 5:
        break

#Output:
#1
#2
#3
#4
#5

# In this example, the loop body executes, increments the `count`, and then checks the condition to potentially break out of the loop.

### `for-each` Loop in Python

# Python's `for` loop is designed to iterate over the elements of a sequence (such as a list, tuple, dictionary, or set) directly, making it similar to a `for-each` loop found in other languages.

#### Basic Syntax

#python
#for item in sequence:
    # Do something with item

#### Examples

#Iterating Over a List:

#python
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# Output:
# apple
# banana
# cherry

#Iterating Over a Dictionary:


#python
person = {"name": "Alice", "age": 30, "city": "New York"}
for key, value in person.items():
    print(f"{key}: {value}")

# Output:
# name: Alice
# age: 30
# city: New York


# **Iterating Over a Set:**

# python
unique_numbers = {1, 2, 3, 4, 5}
for number in unique_numbers:
    print(number)


# Output (order may vary):
# 1
# 2
# 3
# 4
# 5



# Iterating Over a String:

#python
for char in "Hello":
    print(char)


# Output:
# H
# e
# l
# l
# o


### Summary

# - **`do-while` loop**: Not directly available in Python but can be mimicked using a `while True` loop with a `break` condition.
# - **`for-each` loop**: Python's `for` loop iterates directly over the elements of a sequence, serving the same purpose as a `for-each` loop.


