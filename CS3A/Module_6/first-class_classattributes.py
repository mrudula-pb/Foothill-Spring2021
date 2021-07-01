
class PetDog:

    number_of_legs = 4
    number_of_dogs = 0
    max_name_length = 10

    def __init__(self, name: str):
        print(f"{name} is born!")
        if len(name) > PetDog.max_name_length:
            self._name = "Puff"
        else:
            self._name = name
        self._location = "the doghouse"
        PetDog.number_of_dogs += 1

    def bark(self):
        """ Make fido talk """
        print(f"{self._name} says woof!")

    @property
    def name(self):
        return self._name

    # @name.setter
    # def name(self, name):
    #     self._name = name

    @property
    def location(self):
        return self._location

    @location.setter
    def location(self, location: str):
        if location == "the kitchen" or location == "the doghouse":
            self._location = location
        else:
            raise ValueError


print(f'There are {PetDog.number_of_dogs} dogs')
my_dog = PetDog("Fido the king of all dogs")
# my_dog = PetDog('Fido')
print(f'There are {PetDog.number_of_dogs} dogs') # Class variables value is common to all Object of the class

# We are accessing location, name getter and setter methods using location, name. See below
my_dog.location = "the kitchen"

your_dog = PetDog("Spot")
print(f'There are {your_dog.number_of_dogs} dogs') # Class variables value is common to all Object of the class

# Class variables are accessed via Object name and Class name
print(f"{my_dog.name} is in {my_dog.location} and has {my_dog.number_of_legs} legs")

print(f"{your_dog.name} is in {your_dog.location} and has {your_dog.number_of_legs} legs")

print(f"dogs have {PetDog.number_of_legs} legs")

print(f"all dogs are named {PetDog.name}") # all dogs are named <property object at 0x7fb87f47ef98>

