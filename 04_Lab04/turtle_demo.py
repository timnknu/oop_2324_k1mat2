import turtle

turtle.goto(0, -100)

for a in range(0, 270, 20):
    turtle.down()
    turtle.setheading(a)
    turtle.forward(50)
    turtle.up()

#turtle.mainloop()
turtle.exitonclick()