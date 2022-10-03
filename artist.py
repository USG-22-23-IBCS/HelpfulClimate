import turtle

class Artist:

    def __init__(self, t):
        self.t = t
    
    def triangle(self, size = 100):
        for i in range(3):
            self.t.right(120)
            self.t.forward(size)

    def circle(self, size = 1):
         for i in range(360):
            self.t.right(1)
            self.t.forward(1)
                  
    def square(self, size = 10):
         for i in range(4):
            self.t.right(90)
            self.t.forward(size)

    def zigzag(self, size = 100):
         for i in range(4):
            self.t.right(234)
            self.t.forward(size)
            self.t.left(234)
            self.t.forward(size)

    def polygon(self):
        s = int(input("How many sides for the polygon?"))
        l = int(input("How many pixels per side?"))
        for i in range (s):
            self.t.right(360/s)
            self.t.forward(l)

    def star(self, size = 100):
         for i in range(5):
            self.t.right(144)
            self.t.forward(size)
            #self.t.left(234)
            #self.t.forward(size)


    def move(self, x, y):
        self.t.penup()
        self.t.goto(x, y)
        self.t.pendown()

def main():

    canvas = turtle.Screen()
    canvas.bgcolor("lavender")
    canvas.title("Turtle Example")
    t = turtle.Turtle()
    t.shape("turtle")
    t.speed(5)
    art = Artist(t)
#Draw triangle
    art.triangle()
    art.move(150,200) 
#Draw circle
    #art.circle(200)
    art.move(-150, 200)
#Draw# 2 squares
    art.square()
    art.move(-60, 250)
    art.square(100)
#Draw zigzag
    art.move(0,100)
    art.star(50)
#Draw polygon
    art.move(70, -100)
    art.polygon()
#Draw zigzag
    art.move(10, -100)
    art.zigzag()

    
    

    
    
    
    


if __name__ == "__main__":
    main()
