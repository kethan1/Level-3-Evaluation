# Classes and Object-Oriented Programming

# Defining Class
print("\nSample OOP\n")
class SampleClass:

    # Class Var
    sample_class_var1 = "Hi"

    # Initialization Method
    def __init__(self, sample_var1, sample_var2):
        # Instance Var
        self.sample_var1 = sample_var1
        self.sample_var2 = sample_var2

    # Function
    def print_value(self):
        print(self.sample_var1, SampleClass.sample_class_var1, self.sample_var2)

# Create instance
x = SampleClass("H ", " Bye")
# Call class function
x.print_value()


# Encapulasion
print("\nEncapsulation\n")

"""
Used to hide variable from outside class (bundle together instance and variable). Mainly to 
prevent overriding a variable and protect sensitive data. 
"""

class Encapsulation1:
    def __init__(self, n1):
        self.__n1 = n1

    def __p1(self):
        return "Hi"

    def return_n1(self):
        return str(self.__n1)+self.__p1()

x = Encapsulation1(1)
try:
    print(x.__n1)
except:
    print("Got Error When Trying to Access Private Variable")

try:
    print(x.__p1())
except:
    print("Got Error When Trying to Access Private Method")

print(x.return_n1())

# Abstraction
print("\nAbstraction\n")

import abc

class USB_Stick(abc.ABC):
    @abc.abstractmethod
    def return_which_OSs():
        pass

class TestClass(USB_Stick):
    def return_which_OSs(self):
        print("Windows, Linux, MacOS")

test_usb = TestClass()
test_usb.return_which_OSs()


# Inheritance
print("\nInheritance\n")

"""
Inheritance is where there is one main class, and multiple sub classes. 

Overloading and overriding
"""

class Transportation:
    def __init__(self, vehicle_name, wheels):
        self.vehicle_name = vehicle_name
        self.wheels = wheels

    def get_wheels(self):
        return self.wheels

    def vehicle_name(self):
        return self.vehicle_name

    def do(self):
        print("transport")

class Car(Transportation):
    def __init__(self, vehicle_name, wheels, milage):
        self.milage = milage
        super().__init__(vehicle_name, wheels)

    def do(self):
        print("drive")

class Bicyle(Transportation):
    def __init__(self, vehicle_name, wheels, type):
        self.type = type
        super().__init__(vehicle_name, wheels)

    def do(self):
        print("bike")

x1 = [Car("Nissan Altima", 4, "30 miles/gallon"), Bicyle("Random Bicycle", 2, "Mountain Bike")]
for i in x1:
    print(i.get_wheels())
    print(i.do())

# Polymorphism
print("\nPolymorphism\n")

"""
Polymorphism is where multiple apis/classes have the same interface. It makes code cleaner. 
"""

class polymorphism_class1():
    def __init__(self, fruit):
        self.fruit = fruit

    def get_value(self):
        return self.fruit

class polymorphism_class2():
    def __init__(self, vegetable):
        self.vegetable = vegetable
    
    # Arguments
    def get_value(self):
        return self.vegetable

x1 = [polymorphism_class1("orange"), polymorphism_class1("bannana"), polymorphism_class2("lettuce")]
for i in x1:
    print(i.get_value())

# Overloading

"""
Overloading is where you have two functions with the same name, but they are differciated by the
parameters. Technicalities in namespace. The last function will override any function defined
before that with that name. 

Gist: Same Name, Different Function, Different Parameters
"""
