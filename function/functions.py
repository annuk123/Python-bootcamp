#Functions in Python are blocks of reusable code that perform a specific task. They help to organize code, make it more readable, and avoid redundancy. Here's a step-by-step guide on how to define and use functions in Python.

### Defining a Function

#A function is defined using the `def` keyword, followed by the function name, parentheses, and a colon. The code block within every function starts with an indentation (usually four spaces).

#### Basic Syntax

#python
# def function_name(parameters):
     # Code block
#     return value


# - `function_name`: The name of the function, following the naming conventions.
# - `parameters`: Optional. A comma-separated list of parameters the function accepts.
# -`return`: Optional. Specifies the value to be returned by the function.

#### Example

#python
def greet(name):
    return f"Hello, {name}!"


### Calling a Function

#You call a function by using its name followed by parentheses and passing any required arguments.

#### Example

#python
message = greet("Alice")
print(message)

# Output:
# Hello, Alice!

### Parameters and Arguments

# Functions can take parameters, which are variables inside the function that receive values when the function is called. These values are called arguments.

#### Example with Parameters

#python
def add(a, b):
    return a + b

result = add(3, 5)
print(result)

# Output:
# 8

### Default Parameters

#You can define default values for parameters. If an argument is not provided, the default value is used.

#### Example with Default Parameters

#python
def greet(name="World"):
    return f"Hello, {name}!"

print(greet())         # Uses the default value
print(greet("Alice"))  # Uses the provided argument

# Output:
# Hello, World!
# Hello, Alice!

### Keyword Arguments

# You can specify arguments by parameter names, allowing you to pass them in any
# When calling functions, you can use keyword arguments to specify arguments by their parameter names. This allows you to pass arguments in any order.

#### Example with Keyword Arguments

#python
def describe_pet(animal_type, pet_name):
    return f"I have a {animal_type} named {pet_name}."

print(describe_pet(animal_type="dog", pet_name="Buddy"))
print(describe_pet(pet_name="Whiskers", animal_type="cat"))

# Output:
# I have a dog named Buddy.
# I have a cat named Whiskers.

### Variable-Length Arguments

# Python allows you to handle functions with an arbitrary number of arguments using `*args` and `**kwargs`.

# - `*args`: Allows you to pass a variable number of non-keyword arguments.
# - `**kwargs`: Allows you to pass a variable number of keyword arguments.

#### Example with `*args`

#python
def add(*numbers):
    return sum(numbers)

print(add(1, 2, 3))      # 6
print(add(4, 5, 6, 7))   # 22

#### Example with `**kwargs`

#python
def greet(**person):
    return f"Hello, {person['first_name']} {person['last_name']}!"

print(greet(first_name="John", last_name="Doe"))


# Output:
# Hello, John Doe!

### Lambda Functions

# Lambda functions are small, anonymous functions defined using the `lambda` keyword. They can have any number of arguments but only one expression.

#### Example of Lambda Function

#python
add = lambda a, b: a + b
print(add(3, 5))

# Output:
# 8

### Function Scope and Lifetime

# - Local Scope: Variables defined inside a function are not accessible from outside the function.
# - Global Scope: Variables defined outside any function are accessible from any function.

#### Example

# python
global_var = "I am global"

def my_function():
    local_var = "I am local"
    print(global_var)
    print(local_var)

my_function()
print(global_var)
# print(local_var)  # This will cause an error

# Output:
# I am global
# I am local
# I am global


### Nested Functions and Closures

#You can define functions inside other functions. A nested function can access variables of the enclosing function.

#### Example of Nested Functions

#python
def outer_function(msg):
    def inner_function():
        print(msg)
    return inner_function

my_func = outer_function("Hello")
my_func()


# Output:
# Hello


### Summary

# - Defining functions: Use `def` keyword.
# - Calling functions: Use the function name followed by parentheses.
# - Parameters and arguments: Define parameters in the function and pass arguments when calling it.
# - Default parameters: Provide default values for parameters.
# - Keyword arguments: Specify arguments by parameter names.
# - Variable-length arguments: Use `*args` and `**kwargs` for a variable number of arguments.
# - Lambda functions: Small anonymous functions using `lambda`.
# - Scope: Understand local and global variables.
# - Nested functions: Functions defined inside other functions.