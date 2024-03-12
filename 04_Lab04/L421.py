import turtle


class Figure:
    def __init__(self):
        self._position = [0, 0]
        self._visible = False
        self._color = 'forest green'
    def set_position(self, x, y):
        self._position = [x, y]
    def get_position(self):
        return self._position
    def is_visible(self):
        return self._visible
    def set_color(self, clr):
        self._color = clr
    def draw(self):
        raise Exception("Don't call this method!")
        pass
    def show(self):
        if not self._visible:
            # намалювати фігуру
            turtle.pencolor(self._color)
            self.draw()
            self._visible = True
    def hide(self):
        if self._visible:
            # стерти -- намалювати кольором фону
            bgc = turtle.bgcolor()
            turtle.pencolor(bgc)
            self.draw()
            self._visible = False

class Circle(Figure):
    def draw(self):
        turtle.up()
        turtle.goto(*self._position)
        turtle.down()
        turtle.circle(50)

class Triangle(Figure):
    def draw(self):
        side_len = 50
        turtle.up()
        turtle.goto( * self._position )
        turtle.down()
        turtle.setheading(0)
        turtle.forward(side_len)
        turtle.setheading(120)
        turtle.forward(side_len)
        turtle.setheading(240)
        turtle.forward(side_len)

if __name__ == "__main__":
    #obj = Figure()
    #obj.show() # буде помилка

    #fg = Triangle()
    fg = Circle()
    fg.show()
    fg.hide()

    fg.set_position(50, 80)
    fg.show()

    turtle.exitonclick()
