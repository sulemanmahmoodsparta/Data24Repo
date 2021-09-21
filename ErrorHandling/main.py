
# This code below catches an error and allows the code to continue running
try:
    list1 = [1, 2, 3]

    print(list1[4])

    with open("document.txt") as file:

            file.readlines()

except FileNotFoundError as errmsg:

    print("You have deleted the document, you fool!", errmsg)
    raise

except IndexError as errmsg:

    print("There are not enough elements fool!\n", errmsg)

finally:
    print("Execution has stopped")
