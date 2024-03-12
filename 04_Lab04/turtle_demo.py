import turtle

turtle.goto(0, -100)

#turtle.pencolor('#376edc')
turtle.pencolor('forest green')
for a in range(0, 270, 20):
    turtle.down()
    turtle.setheading(a)
    turtle.forward(50)
    turtle.up()

#turtle.mainloop()
turtle.exitonclick()