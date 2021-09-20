# A function is something that requires an input and results in a certain outcome.

# To define a function you def it. Greeting in this case is the function and name is the variable.
# Name is also an argument in this case as it is fed into a function.

def greeting(name: str) -> str:
    return "Hello" + name


# greeting("Danny")

# By adding in the = 0 you are setting a default. It will run this when its left blank.
def addition(int1=0, int2=0):
    return int1 + int2


# print(addition(2, 3) + 5)

def multi_args(*multiargs):
    print(type(multiargs))
    for arg in multiargs:
        print(arg)


# multi_args(1, 2, 3, 4, 5, 6, 7, 8, 9)

# standard 1:
def capture_first_name_from_cmd_line():
    return

# Standard 2: Always include a return.

# Standard 3: Keep your functions small when possible.
# I.e. make everything modular. - To test specific problems with the code.

# Standard 4: Use Comments to make things clearer.


# Always feed variables into the function. Don't use global variables into a function. It should be self-contained.

# Functions should always return something.

# DRY - Don't.
#       Repeat.
#       Yourself.
