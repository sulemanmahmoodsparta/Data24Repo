
age = 17

# if age >= 18:
#     print("You are old enough to watch this film.")
#
# if age < 18:
#     print("You are not old enough to watch this film")

# ----------- OR can be written as:

if age >= 18:
    print("You are old enough to watch this film")
elif 18 > age >= 15:
    print("You need to be with an adult to watch this film")
# elif age > 100:
#     print("You are too old for this film")
#  Careful when ordering the if statements as it will take the statement it hits first.
else:
    print("You are too young to watch this film")

# ----------------- Control Flow ------------------

# An if statement is a control flow. It can control the flow how the code is read.
