# abstractmethod is a decorator

from abc import ABC, abstractmethod


# Base Class
class FarmAnimal(ABC):
    def __init__(self, name):
        self._name = name

    # This is abstractmethod which has no body.
    # We don’t want anyone to create a FarmAnimal object. We want to use it as base
    # class to create a different animal. TypeError occurs when calling my_farm = FarmAnimal()
    @abstractmethod
    def make_a_noise(self):
        pass


# Child Class
class Cow(FarmAnimal):
    # defining the abstract method in child class
    def make_a_noise(self):
        print(f'{self._name} says Moooo')


# Child Class
class Horse(FarmAnimal):
    # defining the abstract method in child class
    def make_a_noise(self):
        print(f'{self._name} says Neigh')


class Farm():
    def __init__(self):
        self._animals = []

    def add_animal(self, animal: FarmAnimal):
        if isinstance(animal, FarmAnimal):
            self._animals.append(animal)
        else:
            raise TypeError

    def make_lots_of_noise(self):
        for animal in self._animals:
            animal.make_a_noise()

# my_farm = FarmAnimal("CAT") # cannot create object of abstract class, TypeError occurs


my_cow = Cow("Bessie")
# my_cow.make_a_noise()
my_horse = Horse("Mr. Ed")
# my_horse.make_a_noise()


my_farm = Farm()

my_farm.add_animal(my_cow)

my_farm.add_animal(my_horse)
my_farm.make_lots_of_noise()


