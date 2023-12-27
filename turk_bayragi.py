import turtle
screen = turtle.Screen()
screen.title("Python ile Türk Bayrağı")
screen.setup(720,420)
screen.bgcolor("red")

kalem = turtle.Turtle()
kalem.color("white")
kalem.penup()
kalem.goto(-120,-100)
kalem.pendown()
kalem.begin_fill()
kalem.circle(120)
kalem.end_fill()

kalem.color("red")
kalem.penup()
kalem.goto(-90,-80)
kalem.pendown()
kalem.begin_fill()
kalem.circle(100)
kalem.end_fill()


kalem.color("white")
kalem.penup()
kalem.goto(-30,20)
kalem.pendown()
kalem.left(10)
kalem.begin_fill()
for i in range(5):
    kalem.forward(120)
    kalem.right(144)
kalem.end_fill()














turtle.done()