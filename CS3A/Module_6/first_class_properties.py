
class PetDog:
    def __init__(self, name: str):
        print(f"{name} is born!")
        self._name = name
        self._location = "the doghouse"

    def bark(self):
        """ Make fido talk """
        print(f"{self._name} sayd woof!")

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


my_dog = PetDog('Fido')

# WE are accessing location, name getter and setter methods using location, name. See below
my_dog.location = "the kitchen"

my_dog.name = "Buster" # we didn't provide setter method. It means we don't want to change the attribute of name, Error
# AttributeError: can't set attribute is observed which is right

# my_dog._name = "Buster" # This is not the right way to do

print(f"{my_dog.name} is in {my_dog.location}")