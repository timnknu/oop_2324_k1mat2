class Figure:
    def __init__(self):
        self._position = [0, 0]
        self._visible = False

    def set_position(self, x, y):
        self._position = [x, y]
    def get_position(self):
        return self._position
    def is_visible(self):
        return self._visible
    def show(self):
        if not self._visible:
            pass # TODO: намалювати фігуру
    def hide(self):
        if self._visible:
            pass # TODO: прибрати фігуру

