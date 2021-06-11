class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


    def move(self):
        print("move")
    def draw (self):
        print("draw")


point1 = Point()
point1.x = 12
point1.y = 21
point1.move()
point1.draw()

point2 = Point()
point2.x = 2
print(point2.x)
point2.draw()