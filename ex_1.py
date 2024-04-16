class Circle:
    """
    This class represents a circle and provides methods to calculate its area and total area of all circles created.
    """

    all_circles = []
    pi = 3.1415

    def __init__(self, radius=1):
        """
        Initialize a circle with the given radius.
        """
        self.radius = radius
        Circle.all_circles.append(self)

    def area(self):
        """
        Calculate the area of the circle.
        """
        return Circle.pi * self.radius**2

    @staticmethod
    def total_area():
        """
        Calculate the total area of all circles created.
        """
        total_area = 0
        for circle in Circle.all_circles:
            total_area += circle.area()
        return total_area
    
    def __str__(self) -> str:
        """
        Return the string representation of the circle.
        """
        return f'{self.radius}'
    
    def __repr__(self) -> str:
        """
        Return the string representation of the circle for debugging.
        """
        return self.__str__()
