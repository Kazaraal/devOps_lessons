# This is lesson 2 assignment

# # A:
# x = int(input("Enter the first number: "))
# y = int(input("Enter the second number: "))

# if x > y:
#     print("BIG")
# else:
#     print("small")


# B:
# for number in range(1, 6):
#     print(number)

# C:
# season = {1: "summer", 2: "winter", 3: "fall", 4: "spring"}
# number_by_user = int(input("Enter a number between 1-4: "))
# if number_by_user in season:
#     print(season[number_by_user])
# else:
#     print("Invalid number")

# D:
# count = 1
# while count < 11:
#     print(count)
#     count += 1

# 1. 10 times
# 2. 10

# E:
# age = int(input("Enter your age: "))
# first_letter = input("Enter the first letter of your last name: ")
# current_shekels_dollar_exchange_rate = float(input("Enter the current shekels-dollar exchange rate: "))
# fly_abroad = input("True/False: Do you want to fly abroad? ")
# apartment_number = int(input("Enter your apartment number: "))

# print(f"Age: {age} \nFirst letter of your last name: {first_letter} \nCurrent shekels-dollar currency: {current_shekels_dollar_exchange_rate} \nYou flew abroad: {fly_abroad} \nAnd your apartment number is: {apartment_number}")

# print(age + current_shekels_dollar_exchange_rate)

# F:
# phone_number = input("Enter your phone number: ")
# print("Phone number: " + phone_number)

# G:
# def printHello():
#     print("hello")

# def calculate():
#     print(5+3.2)

# printHello()
# calculate()

# H:
# 1.
# def get_name():
#     name = input("Enter your name: ")
#     print(f"Your name is: {name}")

# get_name()

# 2.
# def get_number():
#     number = int(input("Enter a number: "))
#     divided_by_two = number / 2
#     print(f"The number divided by 2 is: {divided_by_two}")

# get_number()

# I:
# 1.
# def adds_numbers():
#     first_number = int(input("Enter the first number: "))
#     second_number = int(input("Enter the second number: "))
#     print(f"The sum of the two numbers is: {first_number + second_number}")

# adds_numbers()

# 2.
# def get_strings():
#     first_string = input("Enter the first string: ")
#     second_string = input("Enter the second string: ")
#     print(f"The strings are: {first_string} {second_string}")

# get_strings()

# J:
# list_of_numbers = [1, 2, 3]
# for number in list_of_numbers:
#     print(number)

# K:
# list_of_numbers = [1, 2, 3]
# total = 0
# for number in list_of_numbers:
#     total += number
# print(total)

# L:
# students = {"first_name": "Yossi", "last_name": "Shitrit", "age": 30}
# for key in students:
#     print(key)

# M:
# for star in range(1, 6):
#     print("*" * star)

# N:
# i = 0
# j = 4
# for row in range(5):
#     for column in range(5):
#         if row == i and column == j:
#             print("*", end="")
#             i += 1
#             j -= 1
#         elif row == column:
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print()


# O:
# 1.
# def get_number():
#     number = input("Enter a number with two digits: ")
#     return number

# def adds_numbers(number):
#     first_number = int(number[0])
#     second_number = int(number[1])
#     print(f"The sum of the two numbers is: {first_number + second_number}")
# adds_numbers(get_number())

# P:
# Convert tuple to string
# tup = ('h', 'e', 'l', 'l', 'o')
# str =  ''.join(tup)
# print(str)

# Q:
# lst = [41, 22, 13, 64, 35]

# def smallest_number(lst):
#     if len(lst) == 0:
#         return None
#     smallest = lst[0]
#     for number in lst:
#         if number < smallest:
#             smallest = number
#     return smallest

# sm_num = smallest_number(lst)
# print(sm_num)