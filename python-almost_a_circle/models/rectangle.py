class Rectangle(Base):
    """A class representing a rectangle that inherits from the Base class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize a Rectangle object with the specified
        width, height, x, y, and optional id"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """
        Get the width of the rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Set the width of the rectangle
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """
        Get the height of the rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Set the height of the rectangle
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """
        Get the x
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        Set the x
        """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """
        Get the y
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        Set the y
        """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Return the area of the rectangle"""
        return self.__width * self.__height

    def display(self):
        """Print the rectangle with # characters"""
        print("{}".format("\n" * self.__y), end="")
        for i in range(self.height):
            print("{}{}".format(" " * self.__x, "#" * self.width))
    def update(self, *args):
        """Update the attributes of the rectangle"""
        if len(args) > 0:
            self.id = args[0]
        if len(args) > 1:
            self.width = args[1]
        if len(args) > 2:
            self.height = args[2]
        if len(args) > 3:
            self.x = args[3]
        if len(args) > 4:
            self.y = args[4]
    def __str__(self):
        """Return a string representation of the Rectangle instance"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.__x, self.__y, self.__width, self.__height
        )
