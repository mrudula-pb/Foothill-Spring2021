class PetDog:
    number_of_attributes = 4 # class attributes

    def __init__(self, name: str):  # self refers to Fido i.e the Object we are talking about
        # here name is local to constructor/PetDog object
        print(f"{name} is born!")
        # here self._name is available to other methods of self
        self._name = name # self.-name exits outside of constructor for Object Fido
        self._location = "the doghouse"

    def bark(self):  # here self is for ANY object of PetDog class
        print(f"{self._name} says woof!")

    # get methods
    @property
    def name(self):
        return self._name
    # def get_name(self):
    #     return self._name

    @property
    def location(self):
        return self._location
    # def get_location(self):
    #     return self._location

    # set methods
    @name.setter
    def name(self, name):
        self._name = name
    # def set_name(self, name):
    #     self._name = name

    @location.setter
    def location(self, location: str):
        if location == "the kitchen" or location == "the dighouse":
            self._location = location
        else:
            raise ValueError
    # def set_location(self, location: str):
    #     if location == "the kitchen" or location == "the dighouse":
    #         self._location = location
    #     else:
    #         raise ValueError


my_dog = PetDog("Fido")
print(type(my_dog))
my_dog.bark()
your_dog = PetDog("Betty")
your_dog.bark()

# here is a warning that says you are accessing protected/private values via Object. Python warns but allows
print(f"{my_dog._name} is in {my_dog._location}")


# we created a layer of abstraction by get() methods and not directly accessing the protected/private attributes
# This meets the Object-Oriented Design principles
print(f"{my_dog.name} is in {my_dog.location}")

# Changing _location directly is not safe. Hence we you set() methods as below
my_dog._location = "the bedroom"
print(f"{my_dog._name} is in {my_dog._location}")

my_dog.location = "the kitchen"  # Correct way of setting attribute, HERE IT'S CALLING THE @location.setter
# print(f"{my_dog.get_name()} is in {my_dog.get_location()}")

# The property decorator is allowing the location and name function to be called without parentheses. It's really
# calling the internal private/protected _location _name attributes
print(f"{my_dog.name} is in {my_dog.location} and has {my_dog.number_of_attributes} legs")

# class attribute accessed using Object name
print(f"{your_dog.name} is in {your_dog.location} and has {your_dog.number_of_attributes} legs")

# We can access class attribute using class name and object name
print(f"{PetDog.number_of_attributes}")
