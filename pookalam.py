import turtle
t = turtle.Turtle()
t.hideturtle()
screen = turtle.Screen()
screen.bgcolor("beige")

def circle_center(radius, extent=None, steps=None, color="black"):
    t = turtle.Turtle()
    t.hideturtle()
    t.width(3)
    t.speed(0)
    t.color(color)
    t.begin_fill()
    start_pos = t.pos()
    t.penup()
    t.goto(0, -radius)
    t.pendown()

    if extent is None and steps is None:
        t.circle(radius)
    elif steps is None:
        t.circle(radius, extent)
    elif extent is None:
        t.circle(radius, steps=steps)
    else:
      t.circle(radius, extent, steps)
    t.goto(start_pos)
    t.end_fill()

def square_looping(size, color="white", angle=0):
    t.speed(0)
    t.penup()
    t.goto(0, 0)
    t.setheading(angle)
    t.left(90)
    t.pendown()
    t.color(color)
    t.begin_fill()
    start_pos = t.pos()
    for _ in range(4):
        t.forward(size)
        t.left(90)
    t.goto(start_pos)
    t.end_fill()

def square(size, color="black"):
    t.speed(0)
    t.penup()
    # move to bottom-left corner so square is centered at (0,0)
    t.goto(-size/2, -size/2)
    t.pendown()
    t.color(color)
    t.begin_fill()
    for _ in range(4):
        t.forward(size)
        t.left(90)
    t.end_fill()

def flower(radius=100, color="red", angle=0):
    t.color(color)
    t.setheading(angle)
    t.begin_fill()

    for _ in range(12):   # 8 petals
        t.circle(radius, 60)   # draw an arc (smooth curve)
        t.left(120)            # turn back
        t.circle(radius, 60)   # mirror arc
        t.left(90)             # spacing for next petal (360° / 8)

    t.end_fill()



for angle in range(0,360,12):
    square_looping(200,"gold",angle=angle)
for angle in range(0,360,12):
    square_looping(195,"orange",angle=angle)
for angle in range(0,360,12):
  square_looping(190,"yellow",angle=angle)
flower(250,"green")
circle_center(225,360,12,"orange")
circle_center(220,360,12,"gold")
circle_center(200,color="red")
circle_center(175,360,12,"white")
flower(165,"green")
circle_center(140,color="purple")
for angle in range(0,360,12):
    square_looping(95,"magenta",angle)
for angle in range(0,360,12):
    square_looping(90,"pink",angle)
flower(105,"orange")
flower(95,"gold")
flower(75,"red")
turtle.done()
