from abc import ABC, abstractmethod
from PIL import Image as PILImage

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.__age = age

    def bark(self):
        return f"{self.name} says Woof!"

my_dog = Dog("Buddy", 3)

class Circle:
    pi=3.14159

    def __init__(self, radius):
        self._radius=radius

    def area(self):
        return Circle.pi*self._radius**2

circle = Circle(5)
print(circle.area())

class Image(ABC):
    def __init__(self, data):
        self._data = data

    @property
    @abstractmethod
    def width(self):
        pass

    @property
    @abstractmethod
    def height(self):
        pass

    @abstractmethod
    def get_pixel(self, x, y):
        pass

    @abstractmethod
    def set_pixel(self, x, y, colour):
        pass


class GreyScaleImage(Image):

    def __init__(self, data):
        super().__init__(data)

    def get_pixel(self, x, y):
        return self._data[y][x]

    def set_pixel(self, x, y, colour):
        self._data[y][x] = colour

    @property
    def width(self):
        return len(self._data)

    @property
    def height(self):
        return len(self._data)


grayscale = GreyScaleImage([])
print(grayscale.width)

image = PILImage.open("../../images/stork.png")

resized_image = image.resize((100, 100))

rotated_image = image.rotate(45)

rotated_image.save("../../images/updated_image.png")

print("toto")