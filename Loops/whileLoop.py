# The `while` loop in Python is used to repeatedly execute a block of code as long as a specified condition is true. It is ideal for scenarios where you do not know beforehand how many times you need to iterate.

### Basic Syntax

# ```python
# while condition:
#     # Code to execute while the condition is true


# condition: An expression that evaluates to `True` or `False`. The loop continues as long as this condition is `True`.
# - The indented block of code below the `while` statement is executed repeatedly as long as the condition is `True`.

### Examples

#### Simple `while` Loop

#python
count = 0
while count < 5:
    print(count)
    count += 1

# Output:
# ```
# 0
# 1
# 2
# 3
# 4


# In this example, the loop prints the value of `count` and then increments it by 1. The loop continues until `count` is no longer less than 5.

#### Infinite Loop
#A while loop can become an infinite loop if the condition never becomes False. Be cautious with such loops as they can cause your program to hang.

#python
while True:
    print("This will print forever")


# You can stop an infinite loop by using a break statement or an interrupt from your environment (like pressing Ctrl+C in a command-line interface).

#### Using `break` in a `while` Loop

#The break statement can be used to exit the loop before the condition is False.

#python
count = 0
while count < 10:
    print(count)
    if count == 5:
        break
    count += 1

# Output:
# 0
# 1
# 2
# 3
# 4
# 5


#In this example, the loop stops when `count` equals 5 due to the `break` statement.

#### Using `continue` in a `while` Loop

#The `continue` statement skips the current iteration and proceeds to the next iteration of the loop.

#python
count = 0
while count < 5:
    count += 1
    if count == 3:
        continue
    print(count)

# Output:
# 1
# 2
# 4
# 5


# Here, when `count` is 3, the `continue` statement skips the rest of the loop body and proceeds with the next iteration.


#### Using `else` with a `while` Loop

# The `else` clause in a `while` loop runs when the loop condition becomes `False`.

# python
count = 0
while count < 5:
    print(count)
    count += 1
else:
    print("Loop finished")


# Output:
# 0
# 1
# 2
# 3
# 4
# Loop finished


# The `else` block executes after the loop completes normally.

### Practical Example: Guessing Game

# Here's a simple guessing game using a `while` loop:

# python
import random

number_to_guess = random.randint(1, 10)
guess = None

while guess != number_to_guess:
    guess = int(input("Guess a number between 1 and 10: "))
    if guess < number_to_guess:
        print("Too low!")
    elif guess > number_to_guess:
        print("Too high!")

print("Congratulations! You guessed it!")

# In this example, the loop continues to prompt the user to guess the number until the correct number is guessed.

### Summary

# - **`while` loop**: Repeats a block of code as long as a condition is true.
# - **Infinite loop**: Can occur if the condition never becomes false; use `break` to exit.
# - **`break` statement**: Exits the loop immediately.
# - **`continue` statement**: Skips the current iteration and continues with the next iteration.
# - **`else` clause**: Executes when the loop condition becomes false.



