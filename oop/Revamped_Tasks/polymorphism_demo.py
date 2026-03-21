import math
class Shape:
    def areaself:
        raise NotImplementedError"Derived Class needs to overide this method"
    
class RectangleShape:
    def __init__self, length , width:
        self.length = length
        self.width = width

    def areaself:
        return self.length * self.width
    
class CircleShape:
    def __init__self, radius:
        self.radius = radius

    def areaself:
        return math.pi * self.radius * self.radius
    
