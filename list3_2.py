from math import pi


class Area:
    def get_area(self):
        raise NotImplementedError()


class Volume:
    def get_volume(self):
        raise NotImplementedError()


class Shape:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name


class Square(Area, Shape):
    def __init__(self, name, side):
        super().__init__(name)
        self.side = side

    def get_side(self):
        return self.side

    def set_side(self, side):
        self.side = side

    def get_area(self):
        return self.get_side() ** 2


class Circle(Area, Shape):
    def __init__(self, name, radius):
        super().__init__(name)
        self.radius = radius

    def get_radius(self):
        return self.radius

    def set_radius(self, radius):
        self.radius = radius

    def get_area(self):
        return pi * (self.get_radius() ** 2)


class Cube(Volume, Square):
    def __init__(self, name, side):
        super().__init__(name, side)

    def get_area(self):
        return 6 * (self.get_side() ** 2)

    def get_volume(self):
        return self.get_side() ** 3


class Sphere(Volume, Circle):
    def __init__(self, name, radius):
        super().__init__(name, radius)

    def get_area(self):
        return 4 * pi * (self.radius ** 2)

    def get_volume(self):
        return (4 / 3) * pi * (self.radius ** 3)


class Cylinder(Volume, Circle):
    def __init__(self, name, radius, height):
        super().__init__(name, radius)
        self.height = height

    def get_height(self):
        return self.height

    def set_height(self, height):
        self.height = height

    def get_area(self):
        return 2 * pi * self.radius * self.height

    def get_volume(self):
        return pi * self.height * (self.radius ** 2)


if __name__ == "__main__":
    s = Square("my_square", 2)
    c = Circle("my_circle", 1)
    cube = Cube("my_cube", 2)
    sphere = Sphere("my_sphere", 3)
    cylinder = Cylinder("my_cylinder", 2, 2)

    print(s.get_area())
    print(c.get_area())
    print(cube.get_area(), cube.get_volume())
    print(sphere.get_area(), sphere.get_volume())
    print(cylinder.get_area(), cylinder.get_volume())

    print(s.__class__.__mro__)
    print(c.__class__.__mro__)
    print(cube.__class__.__mro__)
    print(sphere.__class__.__mro__)
    print(cylinder.__class__.__mro__)
