#import runpy
#runpy.run_module('turtledemo')['main']()

import turtle

turtle.goto(0, -100)
#turtle.delay(0)
turtle.speed(0) # 'fastest'
for a in range(0, 270, 20):
    turtle.down()
    turtle.circle(a)
    turtle.up()

#turtle.mainloop()
turtle.exitonclick()