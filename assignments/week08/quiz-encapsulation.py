"""
Write a Python class Rectangle with:

Private attributes for length and width
Methods to calculate area (getArea()) and perimeter getPerimeter())
A method to check if it's a square (isSquare())

"""
class Rectangle:
    def __init__(self,length,width):
        self.__length = length
        self.__width = width

    def getArea(self):
        area = self.__length * self.__width
        return f"Area = {area}"

    def getPerimeter(self):
        perimeter = (self.__length + self.__width) *2
        return f"Perimeter = {perimeter}"

    def isSquare(self):
        if self.__length == self.__width:
            return True
        else:
            return False

myRectangle = Rectangle(10,2)
print(myRectangle.getArea())
myRectangle.getPerimeter()
print(myRectangle.isSquare())