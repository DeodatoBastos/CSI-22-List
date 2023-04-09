from math import pi


# Polymorphims
class Shape:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name


class Square(Shape):
    def __init__(self, name, side):
        super().__init__(name)
        self.side = side

    def get_side(self):
        return self.side

    def set_side(self, side):
        self.side = side

    def get_area(self):
        return self.get_side() * self.get_side()


class Circle(Shape):
    def __init__(self, name, radius):
        super().__init__(name)
        self.radius = radius

    def get_radius(self):
        return self.radius

    def set_radius(self, radius):
        self.radius = radius

    def get_area(self):
        return pi * self.get_radius() * self.get_radius()


# Duck typing
class Bird:
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        pass

    def info(self):
        print(f"My name is {self.name}.")


class Pigeon(Bird):
    def __init__(self, name):
        super().__init__(name)

    def make_sound(self):
        print("Pruuuu!")

    def info(self):
        print("I'm a pigeon!", end=" ")
        super().info()


class Seagull(Bird):
    def __init__(self, name):
        super().__init__(name)

    def make_sound(self):
        print("Meeew!")

    def info(self):
        print("I'm a seagull!", end=" ")
        super().info()


if __name__ == "__main__":
    p = Pigeon("Greg")
    s = Seagull("Drake")

    for bird in (p, s):
        bird.info()
        bird.make_sound()
