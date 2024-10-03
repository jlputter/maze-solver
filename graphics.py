from tkinter import Tk, BOTH, Canvas

class Window():
    def __init__(self, width, height):

        self.__root_widget = Tk()
        self.__root_widget.title("Maze solver")

        self.__canvas = Canvas(self.__root_widget, height = height, width=width)
        self.__canvas.pack()

        self.__running = False

        self.__root_widget.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self.__root_widget.update_idletasks()
        self.__root_widget.update()

    def draw_line(self, line, fill_color):
        line.draw(self.__canvas, fill_color)
    
    def wait_for_close(self):
        self.__running = True
        while self.__running:
            self.redraw()
        print("Window closed")

    def close(self):
        self.__running = False


class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
class Line():
    def __init__(self, point_one, point_two):
        self.__point_one = point_one
        self.__point_two = point_two

    def draw(self, canvas, fill_color):
        canvas.create_line(self.__point_one.x, self.__point_one.y,  self.__point_two.x, self.__point_two.y, fill=fill_color, width = 2)

