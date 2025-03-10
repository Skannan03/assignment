#  Operator Overloading in Python
# Operator overloading allows us to redefine the behavior of operators (+, -, *, etc.)
# for user-defined objects. This is done using special methods
# (also called magic methods or dunder methods, like __add__, __sub__, __mul__, etc.).
#
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f"({self.x}, {self.y})"

p1 = Point(2, 3)
p2 = Point(4, 5)
p3 = p1 + p2  # Calls __add__ method
print(p3)  # Output: (6, 8)

# Operator	Magic Method
# + (Addition)	__add__(self, other)
# - (Subtraction)	__sub__(self, other)
# * (Multiplication)	__mul__(self, other)
# / (Division)	__truediv__(self, other)
# % (Modulo)	__mod__(self, other)
# == (Equality)	__eq__(self, other)
# != (Not Equal)	__ne__(self, other)
# < (Less Than)	__lt__(self, other)
# <= (Less Than or Equal)	__le__(self, other)
# > (Greater Than)	__gt__(self, other)
# >= (Greater Than or Equal)	__ge__(self, other)


class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def __mul__(self, bonus):
        return self.salary * bonus

e1 = Employee("Alice", 50000)
print(e1 * 2)  # Output: 100000

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def __eq__(self, other):
        return self.marks == other.marks

s1 = Student("Alice", 85)
s2 = Student("Bob", 85)
s3 = Student("Charlie", 90)

print(s1 == s2)  # Output: True (Same marks)
print(s1 == s3)  # Output: False (Different marks)



class Box:
    def __init__(self, volume):
        self.volume = volume

    def __gt__(self, other):
        return self.volume > other.volume

    def __lt__(self, other):
        return self.volume < other.volume
box1 = Box(30)
box2 = Box(20)

print(box1 > box2)  # Output: True
print(box1<box2)
