# x = 0
#
# while x < 10:
#     print(f"it's working --> {x}")
#     if x == 4:
#         break
#     x += 1

# print("What is your age?")
# age = input()
#
# while age.isnumeric() == False:
#     print("Please reenter your age as a number")
#
# else:
#     print(f"Your age is {age}")

user_prompt = True

while user_prompt:
    age = input ("What is your age? ")
    if age.isdigit() and int(age) < 120:
        user_prompt = False
        print(f"Your age is {age}!")
    else:
        print("Please provide your answer in digits")