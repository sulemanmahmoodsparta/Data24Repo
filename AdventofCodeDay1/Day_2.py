# Day 2 ---------- Part 1:

# counter = 0
# list_of_passwords = []


# this finds the min requirement for a letter.

# def find_lower(x):
#     return x[:x.index("-")]


# this finds the max requirement for a letter.

# def find_higher(x):
#     return x[x.index("-") + 1:x.index(" ")]


# this finds the letter that is required.

# def find_letter(x):
#     x = x[x.index(" ") + 1:]
#     return x[: x.index(":")]


# with open("passwords.txt", "r") as passwords:
#     data = passwords.readlines()
#
#     for line in data:
#         line = line.rstrip('\n')
#         min_letter = int(find_lower(line))
#         max_letter = int(find_higher(line))
#         letter = find_letter(line)
#         if line.count(letter) - 1 in range(min_letter, max_letter + 1):
#             counter += 1
#             # print("True")
#     print(counter)

# Day 2 ------------------------- Part 2:

def first_number(line):
    return line[:line.index("-")]


def second_number(line):
    return line[line.index("-") + 1:line.index(" ")]


def find_letter(line):
    return line[line.index(" ") + 1: line.index(":")]


def find_password_with_space(line):
    return line[line.index(":") + 1:]


# This function will check if the required character is at one of the locations
def check_if_letter_is_in_location(location, letter, password):
    if password[location] == letter:
        return True
    else:
        return False


with open("passwords.txt", "r") as passwords:
    data = passwords.readlines()
    valid_pass_counter = 0

    for lines in data:
        lines = lines.rstrip("\n")
        first_num = int(first_number(lines))
        second_num = int(second_number(lines))
        let = find_letter(lines)
        password = find_password_with_space(lines)
        number1_match= check_if_letter_is_in_location(first_num, let, password)
        number2_match = check_if_letter_is_in_location(second_num, let, password)

        # if (number1_match == True and number2_match == False) or (number1_match == False and number2_match == True):
        #     valid_pass_counter += 1

        if number1_match != number2_match:
            valid_pass_counter += 1

    print(valid_pass_counter)
