from graphics import Line, Point

class Cell():
    def __init__(self, window=None):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1 = None
        self._x2 = None
        self._y1 = None
        self._y2 = None
        self.visited = False
        self._win = window
    
    def draw_move(self, to_cell, undo=False):

        center_x_first = (self._x1 + self._x2) / 2
        
        center_y_first = (self._y1 + self._y2) / 2

        center_x_second = (to_cell._x1 + to_cell._x2) / 2
        center_y_second = (to_cell._y1 + to_cell._y2) / 2

        print(center_x_first, center_x_second)

        connecting_line = Line(Point(center_x_first, center_y_first), Point(center_x_second, center_y_second))

        color = "red"

        if undo:
            color = "gray"

        self._win.draw_line(connecting_line, color)

    def draw(self, x1, y1, x2, y2):
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2
        if self.has_left_wall:
            wall = Line(Point(x1, y1), Point(x1,y2))
            self._win.draw_line(wall, "blue")
        else:
            wall = Line(Point(x1, y1), Point(x1,y2))
            self._win.draw_line(wall, "white")
        if self.has_right_wall:
            wall = Line(Point(x2, y1), Point(x2,y2))
            self._win.draw_line(wall, "blue")
        else:
            wall = Line(Point(x2, y1), Point(x2,y2))
            self._win.draw_line(wall, "white")
        if self.has_top_wall:
            wall = Line(Point(x1, y1), Point(x2,y1))
            self._win.draw_line(wall, "blue")
        else:
            wall = Line(Point(x1, y1), Point(x2,y1))
            self._win.draw_line(wall, "white")
        if self.has_bottom_wall:
            wall = Line(Point(x1, y2), Point(x2,y2))
            self._win.draw_line(wall, "blue")
        else:
            wall = Line(Point(x1, y2), Point(x2,y2))
            self._win.draw_line(wall, "white")
        
    


    

