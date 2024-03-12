import turtle

for a in range(0, 270, 10):
    turtle.home()
    turtle.down()
    turtle.setheading(a)
    turtle.forward(120)
    turtle.up()

#turtle.mainloop()
turtle.exitonclick()