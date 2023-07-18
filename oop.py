# class and object
class Dog:
    def __init__(self, name, age):
        self._name = name # _name is a protected attribute
        self.__age = age # __age is a private attribute
    
    def bark(self):
        print(f"{self._name} is barking. age is {self.__age}")

dog1 = Dog("Max", 3)
# print(dog1._name) # protected attribute can be accessed
# print(dog1.__age) # private attribute cannot be accessed
# dog1.bark() # Max is barking. age is 3



# Inheritance
class Company:
    def __init__(self, name, address):
        self.name = name
        self.address = address
    
    def get_company_name(self):
        return self.name
    
class SyntechSolution(Company):

    def __init__(self, name, address, employee_count):
        super().__init__(name, address)
        self.employee_count = employee_count

    def get_company_name(self):
        return self.name + ' is a software company' + ' and address is ' + self.address + ' and employee count is ' + str(self.employee_count)

syntechObj = SyntechSolution('Syntech Solution', 'Kathmandu', 100)
#print(syntechObj.get_company_name()) # Syntech Solution

### parent class declaration in child class as chile class parameter. while creating child class object, we need to pass parent class object as parameter



# Polymorphism
class Animal:
    def make_sound(self):
        print('Animal is making sound')

class Dog(Animal):
    def make_sound(self):
        print('Dog is barking')

class Cat(Animal):
    def make_sound(self):
        print('Cat is meowing')

def animal_sound(animal):
    animal.make_sound()

animal_sound(Animal()) # Animal is making sound
animal_sound(Dog()) # Dog is barking
