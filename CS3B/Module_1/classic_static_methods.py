class Dog:

    number_of_dogs = 0

    # The object dog_one is automatically passed and is accessible via self
    def __init__(self, name: str): # self is instance parameter
        self._name = name # private instance object called _name
        Dog.number_of_dogs += 1

    # We can create instance method that wud access class attribute using classmethod
    @classmethod
    def how_many_dogs(cls): # by default class object cls but not instance object self is passed here
        return cls.number_of_dogs

    # The object dog_one is automatically passed and is accessible via self
    @property  # property method used as an accessor for class
    def name(self): # self is instance parameter
        return self._name

    @staticmethod
    def how_many_legs(number_of_dogs: int):
        return number_of_dogs * 4

    def talk(self): # THe object dog_one is automatically passed and is accessible via self
        print(f"{self._name} says woof!")

print(f"There are {Dog.how_many_dogs()} dogs in the universe")

dog_one = Dog('Fido')
print(dog_one.name)
dog_one.talk()

# Using classmethod
print(f"There are {Dog.how_many_dogs()} dogs in the universe")
dog_two = Dog("Fool")
# dog_one knows that there are 2 dogs in the universe
print(f"There are {dog_two.how_many_dogs()} dogs in the universe")
# dog_two knows that there are 2 dogs in the universe
print(f"There are {dog_one.how_many_dogs()} dogs in the universe")

# Using staticmethod
dog_legs = Dog.how_many_legs(Dog.how_many_dogs())
print(f"THere are {dog_legs} dog legs in the universe")
