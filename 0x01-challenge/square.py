#!/usr/bin/python3

class Square():
    """Class Square"""
    
    width = 0
    height = 0

    
    def __init__(self, *args, **kwargs):
        """init function"""
        self.width = self.height = 0
        for key, value in kwargs.items():
            setattr(self, key, value)

    def area_of_my_square(self):
        """ Area of the square """
        return self.width * self.width

    def PermiterOfMySquare(self):
        """ Permiter of the square """
        return (self.width * 2) + (self.width * 2)

    def __str__(self):
        """string representaion of the obj"""
        return "{}/{}".format(self.width, self.width)

if __name__ == "__main__":

    s = Square(width=12)
    print(s)
    print(s.area_of_my_square())
    print(s.PermiterOfMySquare())
