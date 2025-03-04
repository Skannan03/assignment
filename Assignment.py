# Data types in Python
# Text Type:	str
# Numeric Types:	int, float, complex
# Sequence Types:	list, tuple, range
# Mapping Type:	dict
# Set Types:	set, frozenset
# Boolean Type:	bool
# Binary Types:	bytes, bytearray, memoryview
# None Type:	NoneType

# a = "kannan"  # str
# b = 20  # int
# c = 20.5  # float
# d = 2j + 45  # complex
# e = ["qwe", "qaz", "esz", "ijn"]  # list
# j = ("ij", "iujn", "rdc")  # tuple
# k = range(5)  # range
# l = {"name": "kannan", "age": 23}  # dict
# m = {"kannan", "hello", "how r u"}  # set
# p = True  # bool
#
# # Built-In Data Structures:
# # list
# list = ["apple", "banana", "cherry", "2", "13", "True"]
# print(type(list))
# # Access Items
# print(list[1])
# print(list[-1])
# print(list[2:5])
#
# # Change values
# list = ["apple", "banana", "cherry", "2", "13", "True"]
# list[2] = "kannan"
# print(list)
# list[1:3] = ["kannan"]
# print(list)
# list[4:5] = ["awwwsome", 1, 3]
# print(list)
# list.insert(2, "qwerty")
# print(list)
# # list.insert(6,"qwertty",12345) #can only insert 1 argument
# # print(list)
#
# # Add List Items
#
# list = ["apple", "banana", "cherry", "2", "13", "True"]
# list.append("maggie")
# print(list)
#
# list2 = [1234, 1234, 654, 6543]
# list.extend(list2)
# print(list)
#
# # remove list
#
# list.remove("maggie")  # remove uses values
# print(list)
#
# list.pop(4)  # pop uses index
# print(list)
#
# del list[1:4]  # can delete with index
# print(list)
#
# print(list2)
# del list2  # delete the whole list
# # print(list2)
#
# list.clear()  # clears the content in the list
# print(list)
#
# # looping through list
#
# l = ["Kannan", "kEe", "qaz", 12345]
# print(l)
#
# for i in l:
#     print(i)
#
# for i in l:
#     if isinstance(i,str):
#
#         print( i.lower())
# print(l)
#
# list3 = ["apple", "banana", "pineapple"]
# i = 0
# while i < len(list3):
#   print(list3[i])
#   i = i + 1
#
# #list comprehension
# [print(x) for x in l]


#tuple
# Tuple items are ordered, unchangeable, and allow duplicate values.
# tuple = ("qwert","okm",132435,1324)
# tuplee =("plkm","3ed","eda")
# qw= tuple+tuplee
# print(qw)
# # if you want to change the tuple or remove the elements we have to convert into list
#
#
# # set
# # Set items are unordered, unchangeable, and do not allow duplicate values.
# set = {"kannan", "hello", "guys"}
# for x in set:
#   print(x)
# set.add(1234)
# print(set)
#
# set2={123,654,456}
# set.update(set2)
# print(set)
#
# set.remove("kannan")
# print(set)
#
# set.pop()
# print(set)
#
# set.clear()
# del set

x = {"a", "b", "c"}
# y = (1, 2, 3)
#
# z = x.union(y)
# print(z)
#
# set1 = {"a", "b" , "c"}
# set2 = {1, 2, 3}
#
# set1.update(set2)
# print(set1)
#
# set1 = {"apple", "banana", "cherry"}
# set2 = {"google", "microsoft", "apple"}
#
# set3 = set1.difference(set2)
#
# print(set3)
#
# set1 = {"apple", "banana", "cherry"}
# set2 = {"google", "microsoft", "apple"}
#
# set1.difference_update(set2)
#
# print(set1)
#
# set1 = {"apple", "banana", "cherry"}
# set2 = {"google", "microsoft", "apple"}
#
# set3 = set1.symmetric_difference(set2)

# print(set3)

# Dictionary items are ordered, changeable, and do not allow duplicates.
# Dictionary items are presented in key:value pairs, and can be referred to by using the key name.

# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# print(type(thisdict))
#
# x = thisdict.keys()
# x = thisdict.values()
#
# print(x)

# thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964, "color": "red"}
# print(thisdict)

# thisdict.pop("model")
# print(thisdict)

# thisdict.popitem()
# print(thisdict)

# modules
# A file containing a set of functions you want to include in your application.
# we can import a module

# Random Module
#
# import random
#
# print(random.randint(1, 10))  # Random integer between 1 and 10
# print(random.choice(['kanna', 'sonuu', 'aishu']))  # Random choice from a list
# print(random.sample(range(100), 5))
#
# # String Module
# import string
#
# print(string.ascii_letters)
# print(string.digits)
# print(string.punctuation)

# class
# class employee:
#     def __init__(self,name,age,job):
#         self.name=name
#         self.age=age
#         self.job=job
#     def emp(self):
#         print(f"name is {self.name} age is {self.age} job is {self.job}")

# obj=employee("kannan",21,"developer")
# obj.emp()
# ###################################################################################
# name="kannan4"
# age=21
# job="dev"
# class employee4:

#     job="dev"
#     def emp4(self):
#         print(f"name is {name} age is {age} job is {job}")
# obj4=employee4()
# obj4.emp4()

# ############################################################################################
# ###################################################################################
# class employee1:
#     def emp2(self,name,age,job):
#         print(f"name is {name} age is {age} job is {job}")
# obj2=employee1()
# obj2.emp2("kannan1",21,"dev")
# ####################################################################################
# class employee3:
#     name="kannan3"
#     age=21
#     job="dev"
#     def emp3(self):
#         print(f"name is {self.name} age is {self.age} job is {self.job}")
# obj3=employee3()
# obj3.emp3()
# #########################################################################################
# class employee2:
#     name="kannan2"
#     age=21
#     job="dev"
#     def emp2(self):
#         print(f"name is {employee2.name} age is {employee2.age} job is {employee2.job}")
# obj2=employee2()
# obj2.emp2()

################################################################################
# class kannnan:
#     def __init__(self):
#         print("hi nigg")
#     def add(self,a):
#         print("print",a)
#     def maima(self,x):
#         return x+1
#     def __init__(self,name):
#         self.name=name
#         print(name)
# bj=kannnan("kannan")
# bj.add(9)
# bj.maima(9)


# class kannan:
#     pass
# obj=kannan()
# #assign attributes to the instance of the class
# obj.name="kannan"
# obj.age=22

# print(obj.name,obj.age)


# class kannan:
#     def __init__(self,name:str,age:int,sal):
#         self.name=name
#         self.age =age
#         self.sal=sal
#     #assert to compare with actual result
#         assert age>=20,'age should be greater than 20'
#     def id(self):
#         return self.age + 10000

#     def rnge(self):
#         if self.age>=21 and self.age<=30 :
#             print("expected salary = 3000000")
#         elif self.age>=31 and self.age<=40 :
#             print("expected salary = 6000000")
#         elif self.age>=41 and self.age<=50 :
#             print("expected salary = 7000000")

# obj=kannan("kannan",35,3030303)
# print(obj.id())
# obj.rnge()
# print(kannan.__dict__)


# class shiva:
#     @staticmethod
#     def isint(num):
#         if isinstance(num,float):
#             return False
#         elif isinstance(num,int):
#             return True
#         else:
#             return False

# obj=shiva()
# print(obj.isint(123))
# from datetime import date
# class kannan:
#     name="kannan"
#     age=18
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def display(self):
#         print(self.name + " " +str(self.age))
#     @classmethod
#     def date(cls,name,age):
#         dt=date.today().year
#         print(dt)
#         return kannan(name,age)
# obj=kannan()
# obj.display()
# # class method
# a=kannan.date("kannanaa",34)
# a.display()
#
# class employee:
#     employeename = "kannan"
#
#     def __init__(self, account_holder, balance):
#         self.account_holder = account_holder
#         self.balance = balance
#
#     @classmethod
#     def change_emp_name(cls, new_name):
#         cls.employeename = new_name
#
#     @staticmethod
#     def is_valid_amount(amount):
#         return amount > 0
#
#     def deposit(self, amount):
#         if employee.is_valid_amount(amount):
#             self.balance += amount
#             print(f"Deposited {amount}. New balance: {self.balance}")
#         else:
#             print("Invalid deposit amount!")
#
#
# account = employee("ladoo", 500)
#
# print("employee name:", employee.employeename)
# account.deposit(100)
# account.deposit(-50)
#
# employee.change_emp_name("gulabjamun")
# print("Updated emp name:", employee.employeename)


# type casting

# from datetime import datetime
#
# today = datetime.now()
# date_str = today.strftime("%Y-%m-%d")
# print(date_str)
#
# num_str = "123"
# num_int = int(num_str)
#
#
# num_str = "123"
# num_int = int(num_str)
#
# num = 100
# num_float = float(num)

# 6) Identify Scenarios where Built-in Structures May Not Work
# Dictionaries do not support duplicate keys
# Sets do not support indexing
# Lists are slow for large data searches (use set or dict for fast lookups)
# Tuples are immutable and cannot be modified


# # remove duplicate from list
# list = [1, 2, 2, 3, 4, 4, 5]
# unique_list = list(set(list))
# print(unique_list)
#
# my_dict = {"a": 1, "b": 2, "c": 2}
# unique_values = list(set(my_dict.values()))
# print(unique_values)



# Variable Names
# A variable can have a short name (like x and y) or a more descriptive name (age, carname, total_volume). Rules for Python variables:
# A variable name must start with a letter or the underscore character
# A variable name cannot start with a number
# A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
# Variable names are case-sensitive (age, Age and AGE are three different variables)
# A variable name cannot be any of the Python keywords.

# Legal variable names:
# myvar = "John"
# my_var = "John"
# _my_var = "John"
# myVar = "John"
# MYVAR = "John"
# myvar2 = "John"

# Illegal variable names:
#
# 2myvar = "John" # SyntaxError
# my-var = "John" # SyntaxError
# my var = "John" # SyntaxError


# a = "kannan wat are u doing"
# b=a.split()
# b[2]=""
# print(b)
#
# text = "Python is great"
# print(text.replace("great", "awesome"))

# a="racecar is fast"
# b=" fast is fasting "

# print('{} {}'.format(a,b))

# a = "hi my name is kanan what is your name"

# # b=a.split(" ")
# # print(b)
# # for i in b :
# #  if len(i)%2==0:
# #   print(i)

# # a[::]

# decorators
# Function that modifies another function without changing its structure.
# def my_decorator(func):
#     def wrapper():
#         print("Something before function execution")
#         func()
#         print("Something after function execution")
#     return wrapper
#
# @my_decorator
# def say_hello():
#     print("Hello!")
#
# say_hello()
#
# # closure
# # Function that remembers variables from its enclosing scope
# def outer_function(x):
#     def inner_function(y):
#         return x + y
#     return inner_function
#
# add_five = outer_function(5)
# print(add_five(10))
