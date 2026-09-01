import math

class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def magnitude(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def add(self, other):
        return Vector2D(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f"Vector({self.x}, {self.y})"


v1 = Vector2D(3, 4)
v2 = Vector2D(1, 2)

print(v1.magnitude())

v3 = v1.add(v2)
print(v3)