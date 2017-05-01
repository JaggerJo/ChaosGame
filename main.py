from PIL import Image
from random import randint

class Point(object):
    def __init__(self, x=0, y=0):
        self.x = int(x)
        self.y = int(y)

class ChaosGame(object):
    def __init__(self, width, height, fixed_points, start_point):
        self.img_width = width
        self.img_height = height
        self.fixed_points = fixed_points
        self.current_point = start_point
        
        self.img = Image.new("RGB", (self.img_width, self.img_height), "black")
        
        for i in range(0, 1000000):
            self.nextPoint()
        
        for point in self.fixed_points:
            self.img.putpixel((point.x, point.y), (255, 0, 0))

        self.img.save("out.png")
        print("done")
        
    def nextPoint(self):
        rand = randint(0, len(self.fixed_points)-1)
        x = int((self.current_point.x + self.fixed_points[rand].x)/2)
        y = int((self.current_point.y + self.fixed_points[rand].y)/2)

        self.current_point = Point(x, y)
        self.img.putpixel((x, y), (142, 68, 173))
        #print("new point @ x: {0} y: {1}".format(x, y))

if __name__ == "__main__":
    fixed_points = [
        Point(10, 10),
        Point(990, 60),
        Point(450, 990)
    ]
    game = ChaosGame(1000, 1000, fixed_points, Point(200, 200))