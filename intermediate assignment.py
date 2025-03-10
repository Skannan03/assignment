# # Usage of if statement for various built-in structures
# # Using if with list
# lst = [1, 2, 3]
# if lst:  # Checks if list is non-empty
#     print("List is not empty")
#
# # Using if with dictionary
# dct = {}
# if not dct:  # Checks if dictionary is empty
#     print("Dictionary is empty")
#
# # Using if with string
# string = "Python"
# if "P" in string:
#     print("String contains 'P'")
#
#
# # 2) Usage of if-else statement for various built-in structures
# # If-else with a tuple
# tpl = ()
# if tpl:
#     print("Tuple is not empty")
# else:
#     print("Tuple is empty")
#
# # If-else with set
# s = {1, 2, 3}
# if 2 in s:
#     print("Set contains 2")
# else:
#     print("Set does not contain 2")
#
# # 3) While loop and its importance in implementation
#
# # While loops are useful when the number of iterations is unknown and depends on a condition.
#
# # Printing numbers using while loop
# i = 1
# while i <= 5:
#     print(i, end=" ")
#     i += 1
#
#
# # 4) Accept a file as user input, count words, unique words, and letters
# filename = input("Enter file name: ")
# with open(filename, 'r') as f:
#     text = f.read()
#
# words = text.split()
# unique_words = set(words)
# letters = len(text.replace(" ", "").replace("\n", ""))
#
# print(f"Total words: {len(words)}")
# print(f"Unique words: {len(unique_words)}")
# print(f"Total letters: {letters}")


# Count Occurrences of a Word in a File
# word_to_find = input("Enter the word to count: ")
# with open("kannan.txt", 'r') as f:
#     text = f.read()
#
# count = text.split().count(word_to_find)
# print(f"The word '{word_to_find}' appears {count} times.")

# 6) Operator Overloading and Its Importance
# Operator overloading allows us to redefine how operators like +, -, etc., work for custom objects.
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):  # Overloading +
        return Vector(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f"({self.x}, {self.y})"

v1 = Vector(2, 3)
v2 = Vector(4, 5)
print(v1 + v2)  # Output: (6, 8)

# Key Takeaway: Helps in making custom classes behave like built-in types.

# 7) Functions as First-Class Objects
# Functions in Python can be assigned to variables, passed as arguments, and returned from other functions.
def greet(name):
    return f"Hello, {name}"

g = greet  # Assigning function to a variable
print(g("kan"))  # Hello, kan

def execute_func(func, name):
    return func(name)

print(execute_func(greet, "kannan"))  # Hello, kannan

# 8) Object References, Their Advantages, and Why They Are Needed
# In Python, variables store references to objects, not actual data.

class Person:
    def __init__(self, name):
        self.name = name

p1 = Person("kannan")
p2 = p1  # p2 now references the same object as p1

print(p2.name)  # Alice
p1.name = "sanj"
print(p2.name)  # Bob (both reference the same object)
# Advantages: Saves memory, enables object sharing.

# 9) Find Min & Max Count in a DataFrame

import pandas as pd

df = pd.DataFrame({'A': [10, 20, 30, 40], 'B': [5, 15, 25, 35]})
print(f"Min count: {df.count().min()}")
print(f"Max count: {df.count().max()}")

# 10) Find Max and Min Value for a Specific Column
print(f"Max in column A: {df['A'].max()}")
print(f"Min in column A: {df['A'].min()}")

# 11) Find Duplicate Rows and Their Count from Multiple Tables python Copy code

df2 = pd.DataFrame({'A': [10, 10, 20, 30], 'B': [5, 5, 15, 25]})
duplicates = df2[df2.duplicated()]
print("Duplicate rows:\n", duplicates)
print("Duplicate count:", duplicates.shape[0])

# Find List of Columns w.r.t Data Type
print(df.dtypes)


# 13) Find Unique Values from a Table Attribute

print(df['A'].unique())

# 14) Find List of Rows w.r.t Data Type

for dtype in df.dtypes.unique():
    print(f"Rows with data type {dtype}:\n", df.select_dtypes(include=[dtype]))

# 15) Find Missing Values from the Table

df_missing = pd.DataFrame({'A': [1, 2, None], 'B': [None, 5, 6]})
print(df_missing.isnull().sum())  # Count of missing values per column


