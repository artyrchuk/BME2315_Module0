import numpy as np
# This is your first coding assignment for Computational BME.
# As discussed in class, feel free to use AI tools to help you complete this assignment, but remember to cite them.
# I encourage you to try the problems yourself first and only use AI tools when you are stuck to benefit your learning. 

# %% ###########################################################
# Problem 1: Practice writing pseudocode

# Write pseudocode that will input a integer N and output the sum of the first N numbers in the fibonacci sequence.
# Fibonacci sequence starts: 0, 1, 1, 2, 3, 5, 8, 13, 21, ...
# Example: If N = 5, the output should be 0 + 1 + 1 + 2 + 3 = 7

""" # you can use three double-quotes to write multi-line comments
XXX Write your pseudocode here XXX
N = 6

a = 0 # set a to the first fibonacci number
b = 1 # set b to the second fibonacci number
count = 0
total = 0

while count < N:
    total = total + b

    next_value = a + b
    a = b
    b = next_value

    count = count + 1

print(total)
"""

# %% ###########################################################
# Problem 2: Comment your code
# Comments are very helpful for others (especially when pair-coding!) and yourself to understand your code! Add comments to the following code, which will run but produces the wrong output. Once you comment the code, you should be able to identify the error and fix it (the correct total that should be printed is 12).
N = 6

a = 0 # set a to the first fibonacci number
b = 1 # set b to the second fibonacci number
count = 0 #index/iteration counter
total = 0 #total sum of fibonacci numbers

while count < N:
    total = total + b #add next number to total sum

    next_value = a + b #calculate the next fibonacci number
    a = b#set the old next number to the new current number
    b = next_value#set the calculated new number to b

    count = count + 1#increment the counter

print(total)

# %% ###########################################################
# Problem 3: Using common Python libraries
# What is the standard deviation of the first 10 numbers in the fibonacci sequence? Use the numpy library to calculate the standard deviation.
fibonacci_numbers = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
std_dev = np.std(fibonacci_numbers)
print("The standard deviation of the first 10 Fibonacci numbers is:", std_dev)

# %% ###########################################################
# Problem 4: Don't repeat yourself by writing functions
# Write a function that takes an integer N as input and returns the sum of the first N numbers in the fibonacci sequence.
# Then use this function to calculate the sums for N = 5, 10, 15, 20, 25, and 30 and print them as a list.

def sum_fib(N):
    """# The function inputs an integer called "N" and finds the sum of the first N numbers in the fibonacci sequence. It returns the sum.
    :param N: number of fibonacci numbers to sum
    :type N: integer
    :return: sum of the first N fibonacci numbers
    :rtype: integer
    """
    a = 0 # set a to the first fibonacci number
    b = 1 # set b to the second fibonacci number
    count = 0 #index/iteration counter
    total = 0 #total sum of fibonacci numbers

    while count < N:
        total = total + b #add next number to total sum

        next_value = a + b #calculate the next fibonacci number
        a = b#set the old next number to the new current number
        b = next_value#set the calculated new number to b

        count = count + 1#increment the counter

    return total

print(sum_fib(5))
print(sum_fib(10))
print(sum_fib(15))
print(sum_fib(20))
print(sum_fib(25))
print(sum_fib(30))

# %% ###########################################################
# Problem 5: Read your error messages
# Run the following code block to see what the error messages are. Then, for each error:
# 1. Identify what type of error it is (SyntaxError, NameError, TypeError, etc.)
# 2. Add a comment to the line that is throwing the error explaining what the error is
# 3. Fix the error so that the code runs correctly

# You will only see one error at a time when you run the code. After fixing one error, run the code again to see the next error. Your final code should work correctly and will have comments where the original errors were.


def find_fib_above_limit(limit):
    """# The function inputs an integer called "limit" and finds the first number that goes above "limit" in the fibonacci sequence. It returns the index of that number.
    :param limit: limit of fibonacci sequence
    :type limit: integer
    :return: index of the first number above limit
    :rtype: integer
    """
    a = 0 #these used to be str TypeError
    b = 1 #these used to be str TypeError
    index = 0 #index/iteration counter was missing Name Error

    while a <= limit:
        next_value = a + b
        a = b
        b = next_value
        index += 1

    return index


result = find_fib_above_limit(50) #type error can't compare using <= between str and int
print("The index of the first number above your limit is: ", result)
# %% ###########################################################
# Problem 6: Test your code
# The following function will run but will output the wrong answer sometimes. Add test cases to verify that the function works correctly for a variety of inputs. If you find any inputs that produce incorrect outputs, fix the function. The function, when working properly, should return the sum of all odd Fibonacci numbers less than or equal to the input "limit".


def sum_even_fib(limit):
    a, b = 0, 1
    total = 0
    while b <= limit:
        if b % 2 != 0:  # This line checks if the Fibonacci number is odd
            total += b
        a, b = b, a + b
    return total

print(sum_even_fib(13))  # Expected output: 23 (1 + 1 + 3 + 5 + 13)
# Add your test cases here
"""
for the original code I firstly put the limit to 13 and I expected the output to be 23 (1+1+3+5+13) but the output was different
since it is checking for whether b is even and the if it is it adds b to the sum which is not what we want, instead we want to
check if it odd
"""
# %%
