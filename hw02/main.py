import turtle

def main():
    turtle.hideturtle()
    turtle.pensize(3)
    turtle.penup()
    turtle.goto(-350,300)
    turtle.pendown()
    turtle.begin_fill()
    turtle.color("red")
    for i in range(2):
        turtle.forward(600)
        turtle.right(90)
        turtle.forward(400)
        turtle.right(90)
    turtle.end_fill()
    turtle.penup()
    #红旗
    
    turtle.goto(-285,225)
    turtle.pendown()
    turtle.begin_fill()
    turtle.color("yellow")
    for i in range(5):
        turtle.forward(100)
        turtle.right(144)
    turtle.end_fill()
    turtle.penup()
    #中间大五角星

    turtle.goto(-150,275)
    turtle.pendown()
    turtle.begin_fill()
    turtle.color("yellow")
    turtle.right(36)
    for i in range(5):
        turtle.forward(30)
        turtle.right(144)
    turtle.end_fill()
    turtle.penup()
    turtle.home()
    #第一个小五角星

    turtle.goto(-100,240)
    turtle.pendown()
    turtle.begin_fill()
    turtle.color("yellow")
    turtle.right(54)
    for i in range(5):
        turtle.forward(30)
        turtle.right(144)
    turtle.end_fill()
    turtle.penup()
    turtle.home()
    #第二个小五角星
    
    turtle.goto(-115,180)
    turtle.pendown()
    turtle.begin_fill()
    turtle.color("yellow")
    for i in range(5):
        turtle.forward(30)
        turtle.right(144)
    turtle.end_fill()
    turtle.penup()
    turtle.home()
    #第三个小五角星

    turtle.goto(-160,155)
    turtle.pendown()
    turtle.begin_fill()
    turtle.color("yellow")
    turtle.right(36)
    for i in range(5):
        turtle.forward(30)
        turtle.right(144)
    turtle.end_fill()
    #第四个小五角星
    
main()
