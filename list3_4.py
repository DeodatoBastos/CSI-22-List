class Person:

    neighborhood = "Local Vile"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say(self):
        print(f"Hi, I'm {self.name} and I'm {self.age} years old.")

    @classmethod
    def update_neighborhood(cls, neighborhood):
        print(f"Old neighborhood: {Person.neighborhood}")
        Person.neighborhood = neighborhood
        print(f"New neighborhood: {Person.neighborhood}")

    @staticmethod
    def say_a_phrase(phrase):
        print(phrase)


if __name__ == "__main__":
    p = Person("Josh", 20)
    p.say()  # method
    p.say_a_phrase("Today is sunny!")  # staticmethod
    p.update_neighborhood("State Vile")  # classmethod
