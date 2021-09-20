# You define an iterator and cycle through it.

list_data = [1, 2, 3, 4, 5]
#
for num in list_data:
    print(num * 2)
    print("_____" + str(num) + "_______")

embedded_lists = [[1, 2, 3], [4, 5, 6]]
for data in embedded_lists:
    print(data)
    for num in data:
        print(num)

dict_data = {1: {"name": "Izah", "age": "29"}, 2: {"name": "Joi", "age": "15"}}

for key in dict_data:
    print(key)

for dictionary in dict_data.values():
    for value in dictionary.values():
        print(value)

for key in dict_data:
    print(dict_data[key])

for dictionary in dict_data.values():
    print(dictionary["name"])

list_data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for num in list_data:
    if num == 3:
        print("I've found three")
    elif num > 3:
        print("I have gone too far")
    else:
        print("Too soon")

for num in list_data:
    if num % 3 == 0:
        print(num)

