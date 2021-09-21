print("\nQ1a\n")
# Q1a: Replicate the following functions as lambda functions


def square(n):
    return n*n


def percentage(n):
    return n/100


def multiplier(n, m):
    return n*m



def addition(a, b, c):
    return a + b + c


# A1a:

squaring = lambda n: n * n                  # Replicates function square.
print(squaring(5))

percent = lambda n: n / 100                 # Replicates function percentage.
print(percent(10))

multi = lambda n, m: n * m                  # Replicates function multiplier.
print(multi(10, 5))

add = lambda a, b, c: a + b + c             # Replicates function addition.
print(add(5, 20, 25))



print("\nQ1b\n")
# Q1b: Write an explanation of how this factorial lambda function works
factorial = lambda a: a*factorial(a-1) if (a>1) else 1

# A1b:

# Factorial works by taking the variable a and multiplying it by the factorial of a-1 if a is greater than 1.
# If a < 1 then it simply returns 1.


print("\nQ1c\n")
# Q1c: Using the Map function alongside a lambda function, take the list_of_numbers
# and generate a list of all of the numbers squared
list_of_numbers = [23, 345, 45, 76, 87, 4, 2, 0]

# A1c:


# -------------------------------------------------------------------------------------- #
