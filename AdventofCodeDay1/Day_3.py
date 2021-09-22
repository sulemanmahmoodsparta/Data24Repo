
def check_if_space_has_hash(current_location):
    if line[current_location] == "#":
        return True
    else:
        return False


with open("slope.txt", "r") as slope:
    map = slope.readlines()
    current_location = 0

    for line in map:
        current_location += 3
        hash_check = check_if_space_has_hash(current_location)
        


# need to repeat the instance of the line.
# need to check if point has . or #
# need to add to a counter if #
