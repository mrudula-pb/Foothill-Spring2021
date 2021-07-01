
class PetDog:
    def __init__(self, name: str):
        print(f"{name} is born!")
        self._name = name
        self._location = "the doghouse"

    def bark(self):
        """ Make fido talk """
        print(f"{self._name} sayd woof!")

    def get_name(self):
        return self._name

    def get_location(self):
        return self._location

    def set_name(self, name):
        self._name = name

    def set_location(self, location: str):
        if location == "the kitchen" or location == "the doghouse":
            self._location = location
        else:
            raise ValueError


my_dog = PetDog('Fido')
your_dog = PetDog('Spot')
my_dog.bark()
your_dog.bark()

# pycharm warns that you are accessing protected/private Object attributes via Object name
# print(f"{my_dog._name} is in {my_dog._location}")

# It's not true implementation of OOP ENCAPSULATION And abstraction
# We should use accessor get and mutator set methods instead
print(f"{my_dog.get_name()} is in {my_dog.get_location()}")

# Python allow you to change get_location() directly using my_dog._location = "the bedroom"
my_dog._location = "the bedroom"
print(f"{my_dog.get_name()} is in {my_dog.get_location()}")
print("--------------")

# We can use set methods to set location
my_dog.set_location("the bedroom")
print(f"{my_dog.get_name()} is in {my_dog.get_location()}")


