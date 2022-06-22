#!/usr/bin/python3
"""
defines a Square class
implements value and type checks for its attributes
Attributes:
    area
    my_print
"""



class Square:
    """
    Square implementation
    """
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        if type(size) != int:
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size

    def area(self):
        """
        calculates the square area
        """
        return (self.size ** 2)

    def my_print(self):
        """
        prints a square  with the corresponding size
        """
        if (self.__size == 0):
            print('')
        else:
            for i in range(self.position[1]):
                print('')

            for i in range(self.size):
                print(' ' * self.position[0] + '#' * self.size)
    
    @property
    def position(self):
        """
        getter of __position
        Returns: The position of the square in 2D space
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        setter of __position
        Args:
            value (tuple): position of the square in 2D space
        Returns:
            None
        """
        if type(value) is not tuple or len(value) != 2 or \
           type(value[0]) is not int or value[0] < 0 or \
           type(value[1]) is not int or value[1] < 0:
               raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value
