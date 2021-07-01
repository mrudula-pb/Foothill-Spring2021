
class Dog:
    number_of_dogs = 0

    def __init__(self, name: str):
        self._name = name # _name is instance attribute
        Dog.number_of_dogs += 1 # no_of_dogs get incremented for every dog created. EX: dog_one

    # creating class method to access class attributes
    @classmethod
    # It has access to class attribute. It will not know instance attributes i.e will not know name of particular dog
    def how_many_dogs(cls): #instead of instance object "self", a class object is passed "cls" to the method
        return cls.number_of_dogs # (or) return Dog.no_of_dogs

    @staticmethod
    def how_many_legs(number_of_dogs: int): # it doesn't have self parameter
        return number_of_dogs * 4

    @property
    def name(self):
        return self._name

    def talk(self):
        print(f"{self._name} says woof")


print(f"We have {Dog.number_of_dogs} dogs")

dog_one = Dog('Fido') # dog_one is reference to the Object, has name which is tied to _name which is instance attribute
print(dog_one.name) # The property object enables us to access name() method with just as "name" and return the
# private/protected variable value "_name'
dog_one.talk() # We need not pass argument to talk(). dog_one is passed via self in talk() method

print(f'We have {Dog.number_of_dogs} dogs') # need not instantiate to use class method. We can call it by classname
dog_two = Dog("FiFi")
print(f'We have {Dog.number_of_dogs} dogs') #no:of-dogs are called on classname
print(f'We have {dog_two.number_of_dogs} dogs')
print(f"We have {dog_one.number_of_dogs} dogs") # here dog_one will be able to tell the total no:of dogs

dog_legs = Dog.how_many_legs(Dog.how_many_dogs()) # static method doesn’t have access to objects of class or the class
# itself but it was accessed by Dog class

print(f"There are {dog_legs} dog legs")