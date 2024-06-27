# Lambda functions in Python, also known as anonymous functions, are small, unnamed functions defined using the `lambda` keyword. They are typically used for short, simple operations where defining a full function would be overkill. Lambda functions can take any number of arguments but have only one expression.

### Syntax
#python
# lambda arguments: expression

# - **`arguments`**: The parameters the lambda function takes.
# - **`expression`**: A single expression that is evaluated and returned.

### Examples

#### Basic Example

#python
add = lambda a, b: a + b
print(add(3, 5))

# Output:
# 8

#### Using Lambda with `map()`

# The `map()` function applies a given function to all items in an input list (or any other iterable).

#python
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x ** 2, numbers))
print(squared)

# Output:
# [1, 4, 9, 16, 25]

#### Using Lambda with `filter()`

# The `filter()` function constructs an iterator from elements of an iterable for which a function returns true.

#python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)

# Output:
# [2, 4, 6, 8, 10]

#### Using Lambda with `reduce()`

# The `reduce()` function from the `functools` module applies a rolling computation to sequential pairs of values in an iterable.

#python
from functools import reduce

numbers = [1, 2, 3, 4, 5]
product = reduce(lambda x, y: x * y, numbers)
print(product)

# Output:
# 120

# Sorting with Lambda

# Lambda functions are often used as the key function in sorting.

#python
students = [("Alice", 25), ("Bob", 20), ("Charlie", 23)]
# Sort by age
students_sorted = sorted(students, key=lambda student: student[1])
print(students_sorted)

# Output:
# [('Bob', 20), ('Charlie', 23), ('Alice', 25)]

#### Nested Lambda Functions

#Lambda functions can be nested to create more complex operations.

#python
nested_lambda = lambda x: (lambda y: x + y)
add_five = nested_lambda(5)
print(add_five(3))

# Output:
# 8

### Comparison with Regular Functions

# While lambda functions are concise, they have limitations compared to regular functions defined with `def`:

# - Lambda functions are limited to a single expression. They cannot contain multiple statements or annotations.
# - Lambda functions are generally less readable for complex operations.
# - Lambda functions do not have a name, which can make debugging harder.

#### Regular Function Example

#python
def add(a, b):
    return a + b

print(add(3, 5))

# Output:
# 8


### When to Use Lambda Functions

# - **Short, simple functions**: When you need a quick function for a small task.
# - **Inline operations**: When used as arguments to functions like `map()`, `filter()`, or `sorted()`.
# - **Avoiding boilerplate code**: When you don't want to define a full function using `def`.

### Summary

# - **Lambda functions**: Anonymous, small functions defined with the `lambda` keyword.
# - **Syntax**: `lambda arguments: expression`.
# - **Common uses**: With `map()`, `filter()`, `reduce()`, and as sorting keys.
# - **Limitations**: Single expression, no statements, and typically less readable for complex tasks.
