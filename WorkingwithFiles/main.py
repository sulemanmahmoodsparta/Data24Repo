# file = open("order.txt") # Would have to do entire file path if its not in the same directory.
# # open ^ in this case opens a file as a 'stream'.
#
# file_content = file.readlines()
#
# for line in file_content:
#     print(line.replace("\n", ""))
#
# file.close() # need to close the file as it stays in memories.

# We can not have an open and close file function when we just do this

# with open("order.txt", "r") as file:
#
#     file_content = file.readlines()
#
#     for line in file_content:
#         print(line.replace("\n", ""))

with open("order.txt", "w") as file:

    order_items = ["Fries", "Onion rings", "Drink"]

    for item in order_items:
        file.write(item + "\n")