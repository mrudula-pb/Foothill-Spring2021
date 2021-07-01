
class PetDog:

    number_of_legs = 4
    number_of_dogs = 0
    max_name_length = 10

    def __init__(self, name: str, location="the kitchen"):
        print(f"{name} is born!")
        if len(name) > PetDog.max_name_length:
            self._name = "Puff"
        else:
            self._name = name
        # we don't want to get exception in constructor. Hence we catch the Exception and set the value
        try:
            self.location = location # self.location force a call to setter
        except ValueError:
            self._location = "the kitchen"
        PetDog.number_of_dogs += 1

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


# my_dog = PetDog('Fido')
my_dog = PetDog('Fido', "the bedroom")

print(f"{my_dog.name} is in {my_dog.location}")