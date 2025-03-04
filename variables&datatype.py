# variables are used to store data values
# x = str(3)    # x will be '3'
# y = int(3)    # y will be 3
# z = float(3)  # z will be 3.0
# x = 5
# y = "John"
# print(type(x))
# print(type(y))


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
# 2myvar = "John"
# my-var = "John"
# my var = "John"

# x, y, z = "Orange", "Banana", "Cherry"
# print(x)
# print(y)
# print(z)

# x = y = z = "Orange"
# print(x)
# print(y)
# print(z)
#
#
# # Unpack a list:
#
# fruits = ["apple", "banana", "cherry"]
# x, y, z = fruits
# print(x)
# print(y)
# print(z)
#
#
# x = "Python"
# y = "is"
# z = "awesome"
# print(x+y+z)
#
# # x = 5
# # y = "John"
# # print(x + y) # output multiple variables in the print() function is to separate them with commas,
#
# #######################################
# x = 5
# y = "John"
# print(x, y)
# ##########################################
# x=12
# def myfun():
#     print("python is " , x)
# myfun()
# ##################################################
# x = "awesome"
#
# def myfunc():
#   x = "fantastic"
#   print("Python is " + x)
#
# myfunc()
#
# print("Python is " + x)
############################################################
# we have defined the global variable inside the function using the global keyword
x
# def myfunc():
#     global x
#     x="kannan"
# myfunc()
#
# print("python is ", x)

#############################################################
# this will overwrite the existing variable value because the global variable is defined inside the function
# x= "qwerty"
# def myfunc():
#     global x
#     x="kannan"
# myfunc()
#
# print("python is ", x)
##################################################

# Datatype

# x = 1    # int
# y = 2.8  # float
# z = 1j   # complex
#
# print(type(x))
# print(type(y))
# print(type(z))
# #convert from int to float:
# a = float(x)
#
# #convert from float to int:
# b = int(y)
#
# #convert from int to complex:
# c = complex(x)
#
# print(a)
# print(b)
# print(c)
#
# print(type(a))
# print(type(b))
# print(type(c))
##################################################3
# a = '''Lorem ipsum dolor sit amet,
# consectetur adipiscing elit,
# sed do eiusmod tempor incididunt
# ut labore et dolore magna aliqua.'''
# print(a)

####################################################
#
# for i in "banana":
#     print(i)
# b = "Hello, World!"
# print(b[2:8])
#######################
# a = " Hello, World! "
# print(len(a))
# b=a.strip()
# print(len(b))

# thislist = ["apple", "banana", "cherry"]
# thislist[1] = "blackcurrant"
# print(thislist)
# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
# thislist[1:5:3] = ["blackcurrant", "watermelon"]
# print(thislist)

# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
# thislist[2:1] = ["watermelon"]
# print(thislist)
#
# thislist = ["apple", "banana", "cherry"]
# thislist.insert(2, "watermelon")
# print(thislist)
#
# thislist = ["apple", "banana", "cherry"]
# thislist.insert(1, "orange")
# print(thislist)

# thislist = ["apple", "banana", "cherry"]
# thistuple = ("kiwi", "orange")
# thislist.extend(thistuple)
# print(thislist)

# thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
# thislist.remove("banana")
# print

# thislist = ["apple", "banana", "cherry"]
# for i in range(len(thislist)):
#   print(thislist[i])

# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# newlist=[x for x in fruits if "cherry" in x ]
# print(newlist)
#
# thislist = ["banana", "Orange", "Kiwi", "cherry"]
# thislist.sort(key = str.lower)
# print(thislist)

# def myfunc(n):
#     return abs(n - 50)
#
#
# thislist = [100, 50, 65, 82, 23]
# thislist.sort(key=myfunc)
# print(thislist)

# we can copy the list by multiple methods
# thislist = ["apple", "banana", "cherry"]
# mylist = thislist.copy()
# mylist = list(thislist)
# mylist = thislist[:]
# mylist=thislist
# print(mylist)


#join lists
# list1=["kannan","kanna","kakn"]
# list2=["qwe","qaz",]
# m=list2+list1
# m.sort()
# print(m)

# thistuple = ("apple",)
# print(type(thistuple))
#
# #NOT a tuple
# thistuple = ("apple")
# print(type(thistuple))

# fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
#
# (green, yellow, *red) = fruits
#
# print(green)
# print(yellow)
# print(red)
#
# fruits = ("apple", "mango", "papaya", "pineapple", "cherry")
#
# (green, *tropic, red) = fruits
#
# print(green)
# print(tropic)
# print(red)
#
# thisset = {"apple", "banana", "cherry"}
#
# print("banana" not in thisset)
#
# x = {"a", "b", "c"}
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

# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# thisdict.update({"year": 2020})