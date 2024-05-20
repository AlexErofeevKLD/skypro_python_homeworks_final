import math
def square(side):
    
    if not isinstance(side, int):
        side = math.ceil(side)
    return side ** 2
side = 6.5
area = square(side)
print("Площадь квадрата со стороной", side, "равна", area)