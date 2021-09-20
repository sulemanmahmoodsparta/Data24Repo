# ----Q1:

# list1 = []
#
# for i in range(1000):
#     if i % 3 == 0 or i % 5 == 0:
#         list1.append(i)
#
# print(sum(list1))

# -------------------------------------------Q2:
#
# n1 = 0
# n2 = 1
# f1 = 0
# f2 = 0
#
# flist = []
#
# while f1 < 4000000:
#     f1 = n1 + n2
#     n2 = n1
#     n1 = f1
#     if f1 % 2 == 0:
#         f2 += f1
#         flist.append(f1)
# print(f2)

# sequence = [1, 2]
# total = 0
#
# for i in range(4000000):
#     if i == sequence[-1] + sequence[-2]:
#         sequence.append(i)
#
# for n in sequence:
#     if n % 2 == 0:
#         total += n
# print(total)

# -------------------------------------------Q3:

# n = 600851475143
# i = 2
# while i * i < n:
#     while n % i == 0:
#         n /= i
#     i += 1
#
# print(n)

# --- Q4: Find the largest palindrome made from the product of two 3-digit numbers.

# x = 100
# y = 100
# list1 =[]
# biggest_number = 0
# for x in range(100, 1000):
#     # print(x)
#     for y in range(100,1000):
#         number = x * y
#         number1 = str(number)
#         if number1[0] == number1[-1] and number1[1] == number1[-2] and number1[2] == number1[-3]:
#             list1.append(number1)
#             if number > biggest_number:
#                 biggest_number = number
#
# print(biggest_number)

# --- Q5: What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

# i = 2
# x = 20
# smlist = []
# while i < 21:
#     if x % i == 0:
#         i += 1
#     else:
#         x += 1
#         i = 2
#
# print(x)

# --- Q6: Find the difference between the sum of the squares of the first one hundred natural numbers
#           and the square of the sum.

# list = []
# list2 = []
#
# for x in range(1, 101):
#     squares = x * x
#     list.append(squares)
#     sum(list)
# for y in range(1, 101):
#     list2.append(y)
#     sum_list2 = sum(list2) * sum(list2)
#
# difference = sum_list2 - sum(list)
#
# print(difference)

# sum_of_squares = sum([i * i for i in range(1, 101)])
# square_of_sum = sum(range(1, 101))
# square_of_sum = square_of_sum * square_of_sum
# print(square_of_sum - sum_of_squares)

# ---Q7: What is the 10 001st prime number?
# We want the 10001 number that isnt divisble by any number
#prime number is a number in which its not divisble by all numbers below it except 1.


last = 0

for i in range(2, 10002):
    for j in range(2, i):
        if(i % j) == 0:
            break
    else:
        last = i
print(last)

