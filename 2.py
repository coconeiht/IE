class Animal:
    def __init__(self, name):
        self.__name = name  # Private attribute

    @property
    def Animal_name(self):
        return self.__name


class Reptile(Animal):
    def __init__(self, name):
        super().__init__(name)


class Mammal(Animal):
    def __init__(self, name):
        super().__init__(name)


class Lizard(Reptile):
    def __init__(self, name):
        super().__init__(name)


class Snake(Reptile):
    def __init__(self, name):
        super().__init__(name)


class Gorilla(Mammal):
    def __init__(self, name):
        super().__init__(name)


class Bear(Mammal):
    def __init__(self, name):
        super().__init__(name)