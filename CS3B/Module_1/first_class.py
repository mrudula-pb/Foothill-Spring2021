class PetDog:
    def __init__(self, name: str):
        print(f'{name} is born')
        self._name = name
        self._location = 'the doghouse'

    def bark(self):
        """ Make Fido talk"""
        print(f"{self._name} says woof!")

    # def get_name(self):
    #     return self._name
    @property
    def name(self):
        return self._name

    # property decorator helps to change the location instead of creating set_location() function
    # def get_location(self):
    #     return self._location
    @property
    def location(self):
        return self._location

    # def set_location(self, location: str):
    #     if location == "the kitchen" or location == "the doghouse":
    #         self._location = location
    #     else:
    #         raise ValueError
    @location.setter
    def location(self, location: str):
        if location == "the kitchen" or location == "the doghouse":
            self._location = location
        else:
            raise ValueError

my_dog = PetDog('Fido')
your_dog = PetDog('Spot')
my_dog.bark()
your_dog.bark()

# my_dog.set_location("the kitchen")
my_dog.location = 'the kitchen'
my_dog._name = "Buster"

# print(f"{my_dog.get_name()} is in {my_dog.get_location()}")
print(f"{my_dog.name} is in {my_dog.location}") # here the location(), name() function is called and gets the location, name values