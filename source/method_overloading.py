""" This module is to demonstrate method overloadind.
"""
from typing import overload

class MethodOverloading():
    """ This class contain multiple implementations
    for add function to understand method overloading.
    """
    def __init__(self):
        pass

    @overload
    def add(self, a: int, b: int) -> int:
        """Implementation for integer arguments.
        """
        print("integere addition")
        return a + b

    @overload
    def add(self, a: float, b: float) -> float:
        """Implementation for float arguments.
        """
        print("float addition")

    @overload
    def add(self, a: str, b: str) -> str:
        """Implementation for string arguments.
        """
        print("str addition")
        return a + b

if __name__ == "__main__":
    method_overloading = MethodOverloading()
    print(method_overloading.add(10, 20))
    print(method_overloading.add(10.5, 20.7))
    print(method_overloading.add('subin ', 'george'))
