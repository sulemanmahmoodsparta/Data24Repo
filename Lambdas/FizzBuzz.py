# Fizzbuzz = False
# def divisble_5_3(x):
#     x % 5 == 0 and x % 3 == 0
#     return Fizzbuzz = True
#
# for i in range(1, 101):
#     if i % 3 == 0 and i % 5 == 0:
#         print("FizzBuzz")
#     elif i % 3 == 0:
#         print("Fizz")
#     elif i % 5 == 0:
#         print("Buzz")
#     else:
#         print(i)


# ---------- Dannys Code ------------
class Fizzbuzz:

    def __init__(self, start_of_range, end_of_range):
        self.range = range(start_of_range, end_of_range)
        self.fizzbuzz_list = []
        self.fizzbuzz_iterator()

    def divisible_by(self, num1, num2):
        if num1 % num2 == 0:
            return True
        else:
            return False
    def fizzbuzz_iterator(self):

        for num in self.range:
            if self.divisible_by(num, 15):
                self.fizzbuzz_list.append("fizzbuzz")
            elif self.divisible_by(num, 5):
                self.fizzbuzz_list.append("buzz")
            elif self.divisible_by(num, 3):
                self.fizzbuzz_list.append("fizz")
            else:
                self.fizzbuzz_list.append(num)