# Day 2 ---------- Part 1:

counter = 0
list_of_passwords = []


# this finds the min requirement for a letter.

def find_lower(x):
    return x[:x.index("-")]


# this finds the max requirement for a letter.

def find_higher(x):
    return x[x.index("-") + 1:x.index(" ")]


# this finds the letter that is required.

def find_letter(x):
    x = x[x.index(" ") + 1:]
    return x[: x.index(":")]


with open("passwords.txt", "r") as passwords:
    data = passwords.readlines()

    for line in data:
        line = line.rstrip('\n')
        min_letter = int(find_lower(line))
        max_letter = int(find_higher(line))
        letter = find_letter(line)
        if line.count(letter) - 1 in range(min_letter, max_letter + 1):
            counter += 1
            # print("True")
    print(counter)

# Day 2 ------------------------- Part 2:



