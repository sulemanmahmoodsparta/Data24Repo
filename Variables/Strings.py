# string_var1 = 'Hello 123'
# string_var2 = "Hello 345"
#
# print(string_var1 + ' ' + string_var2)


# string_fail = "I said 'WOW!'"
# print(string_fail)


# escape_example_1 = 'I said \'WOW!\'... and to escape a backslash \\'
# print(escape_example_1)
#
# quote_in_quote = 'I said "WOW!"'
# print(quote_in_quote)
#

# ------------------------slicing strings------------------

# Hw = 'Hello! World'
# print(len(Hw))
# print(Hw[7:12])
# print(Hw[7:])
# print(Hw[:5])
# print(Hw[-1:])
#
# print(Hw[1::2])
# # square brackets works by [character number:to secound character:steps]


# white_space = "                    Lot's of white space         "
# print(len(white_space))
# print(len(white_space.strip()))

# white_space = white_space.strip()
# print(len(white_space))
#
# a = 1
# a = a + 1
# print(a)

# example_text = "Here's some text with lots of text"
# print(example_text.count("text"))
# count is case sensitive
# print(example_text.lower())
# print(example_text.upper())
# print(example_text.capitalize())
# print(example_text.replace("text",""))
# print(example_text.replace((" ", "")))

# a = "Here"
# b= "more"
# c = "much more"
# print(a + b + c)
#
# x = 2
# y = 5.4
# z = "there's a now number 25.4 unless we put a space in!"
# print(str(x) + str(y) + z)


# ------------------- Casting-----------------------

# int_string = "6"
#
# print(float(int_string))
# print(type(float(int_string)))


# ----------------------- F-String-------------------

name = "Lassie"
years = 7
height_cm = 60.2

print(f"{name} is {years} years old and {height_cm}cm tall.")

name = "Snoopy"
years = 52

print(f"{name.upper()} IS {years * 7} YEARS OLD IN DOG YEARS")
