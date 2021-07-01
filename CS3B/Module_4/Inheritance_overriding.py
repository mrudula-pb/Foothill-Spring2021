

class Cat:
    def __init__(self, name):
        self.name = name

    def make_a_noise(self, number):
        print(f"{self.name} says meow")
        for _ in range(number):
            print('meow!')

    def x(self, new_parameter):
        pass

class Siamese(Cat):
    # overriding a method
    def make_a_noise(self, number):
        print(f"{self.name} says mooooooooooooo")
        for _ in range(number):
            print('moooooooooo!')

    def x(self, new_parameter):
        pass

my_cat = Cat("Fido")
my_cat.make_a_noise(4)


my_newcat = Siamese("Fido")
my_newcat.make_a_noise(5)




































































































































































