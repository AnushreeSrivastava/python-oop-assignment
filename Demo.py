import requests

# from abc import ABC, abstractmethod
# class Shape(ABC):
#
#     @abstractmethod
#     def area(self): pass
#
#     @abstractmethod
#     def perimeter(self): pass
#
# class Square(Shape):
#     def __init__(self, side):
#         self.__side = side
#     def area(self):
#         return self.__side * self.__side
#     def perimeter(self):
#         return 4 * self.__side
#
# shape = Shape()
# square = Square(5)
# print(square.area())


def func(a):
    # print(a)
    r = requests.get("https://google.com")
    print(r.status_code)
    func(5)

