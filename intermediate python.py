# """Python Conditions and If statements
# Python supports the usual logical conditions from mathematics:
#
# Equals: a == b
# Not Equals: a != b
# Less than: a < b
# Less than or equal to: a <= b
# Greater than: a > b
# Greater than or equal to: a >= b"""
# a = 200
# b = 33
# if b > a:
#   print("b is greater than a")
# elif a == b:
#   print("a and b are equal")
# else:
#   print("a is greater than b")
#
# a = 200
# b = 33
# c = 500
# if a > b and c > a:
#   print("Both conditions are True")
#
# # WHILE LOOP
# while True:
#     user_input = input("Enter a number (type 'exit' to stop): ")
#     if user_input.lower() == "exit":
#         break
#     print(f"You entered: {user_input}")
#
# # class
# #
# # class Person:
# #   def __init__(self, name, age):
# #     self.name = name
# #     self.age = age
# #
# #   def introduce(self):
# #     return f"My name is {self.name}, and I am {self.age} years old."
# #
# #
# # person1 = Person("Alice", 25)
# # print(person1.introduce())


# TXT File: Open, Read, Write

# with open("kannan.txt", "w") as file:
#   file.write("Hello, this is a sample text file.\n")
#   file.write("Python makes file handling easy.")

# with open("kannan.txt", "r") as file:
#     content = file.read()
#     print(content)
#
# with open("kannan.txt","a") as file:
#   file.write("\nAppending new data to the file.")

# JSON File: Open, Read, Write
# Python provides the json module for handling JSON files

# import json
#
# data = {
#     "name": "Alice",
#     "age": 25,
#     "skills": ["Python", "Machine Learning"]
# }
#
# with open("data.json", "w") as file:
#     json.dump(data, file, indent=4)
#
# with open("data.json", "r") as file:
#     loaded_data = json.load(file)
#     print(loaded_data)
#
# loaded_data["age"] = 26  # Updating age
#
# with open("data.json", "w") as file:
#     json.dump(loaded_data, file, indent=4)
#
# with open("data.json", "r") as file:
#     loaded_data = json.load(file)
#     print(loaded_data)

# Parquet File: Open, Read, Write
# Parquet is a columnar storage format optimized for big data. Python’s pandas library can handle Parquet files.
# import pandas as pd
#
# data = {"Name": ["Alice", "Bob"], "Age": [25, 30]}
# df = pd.DataFrame(data)
#
# df.to_parquet("data.parquet", engine="pyarrow")
#
# df = pd.read_parquet("data.parquet", engine="pyarrow")
# print(df)


# Try Except
# The try block lets you test a block of code for errors.
#
# The except block lets you handle the error.
#
# The else block lets you execute code when there is no error.
#
# The finally block lets you execute code, regardless of the result of the try- and except blocks.
# try:
#
#     print(x)
# except:
#     print("An exception occurred")

# try:
#   print(x)
# except NameError:
#   print("Variable x is not defined")
# except:
#   print("Something else went wrong")


# try:
#   print("Hello")
# except:
#   print("Something went wrong")
# else:
#   print("Nothing went wrong")


# try:
#   print(x)
# except:
#   print("Something went wrong")
# finally:
#   print("The 'try except' is finished")

# x = -1
#
# if x < 0:
#   raise Exception("Sorry, no numbers below zero")
#
# x = "hello"
#
# if not type(x) is int:
#   raise TypeError("Only integers are allowed")

# Built-in Math Functions
x = min(5, 10, 25)
y = max(5, 10, 25)

print(x)
print(y)

x = abs(-7.25)

print(x)

x = pow(4, 3)

print(x)

import math

import math

x = math.sqrt(64)

print(x)

import math

x = math.ceil(1.4)
y = math.floor(1.4)

print(x)  # returns 2
print(y)  # returns 1

x = math.pi

print(x)
