# -- Also known as an array. Lists are a collection of items.

shopping_list = ["bread", "bananas", "mushrooms", "onions"]

# print(type(shopping_list))
# print(shopping_list)

# --- To get an item in the list.

# print(shopping_list[2])

# -- Change an item in the list.

# shopping_list[1] = "plantain"
# print(shopping_list)

# --- Add more things to the list.

# shopping_list.append("pasta")
# print(shopping_list)

# --- Remove an item.

# shopping_list.remove("bread")
# print(shopping_list)

# shopping_list.pop()
# print(shopping_list)

mixture = [1, 2, 3, "one", "two", "three"]
print(mixture)

print(mixture[1:3])
print(mixture[-2::1])
print(mixture[::2])

# --------------------------- Tuple --------------------------------

essentials = ("bread", "tomatoes", "coffee")
print(essentials.count("bread"))
print(len(essentials))
# Tuple can't be changed unlike lists. Only difference is use round brackets instead of square brackets.
