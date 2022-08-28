import turtle

# Project has been scrapped

################################
# UTILITY CLASSES
################################

# Makes gfx calc easier
class vec:
    def __init__(self, px, py):
        self.x = px
        self.y = py

    def add(self, v):
        return vec(self.x + v.x, self.y + v.y)

    def sub(self, v):
        return vec(self.x - v.x, self.y - v.y)
    
    def mult(self, scalar):
        return vec(self.x * scalar, self.y * scalar)

class drawing_manager:
    turtle = turtle.Turtle()

    @staticmethod
    def init():
        turtle.up()
        turtle.tracer(0, 0)
        turtle.hideturtle()
        turtle.update()

    # Not really sure how these equations for the box pos works but once it works
    # I don't really have to worry about it since I can hand it coord (0-10, 0-20)
    # and it will map them
    
    @staticmethod
    def draw_piece(pos, piece_state, color):
        
        pos.y = -pos.y
        for i in range(4):
            for j in range(4):
                if piece_state[i][j] == "X":            
                    drawing_manager.draw_box(vec(j, 20-i).add(pos).mult(BOX_SIZE).add(BOARD_POS), color)
        turtle.update()

    def draw_dead_pieces(pieces):
        for i in range(20):
            for j in range(10):
                if pieces[i][j] != "":
                    drawing_manager.draw_box(vec(j, 19-i).mult(BOX_SIZE).add(BOARD_POS), pieces[i][j])
    
    @staticmethod
    def draw_box(pos, color):
        turtle.goto(pos.x, pos.y)
        turtle.color(color)
        turtle.down()
        turtle.begin_fill()
        for i in range(4):
            turtle.forward(BOX_SIZE)
            turtle.left(90)
        turtle.end_fill()
        turtle.up()

    @staticmethod
    def draw_bg():
        #  Prefer this to turtle.screensize() because I don't want the whole screen black
        turtle.goto(BOARD_POS.x, BOARD_POS.y)
        turtle.color("black")
        turtle.down()
        turtle.begin_fill()
        turtle.forward(BOX_SIZE*10)
        turtle.left(90)
        turtle.forward(BOX_SIZE*20)
        turtle.left(90)
        turtle.forward(BOX_SIZE*10)
        turtle.left(90)
        turtle.forward(BOX_SIZE*20)
        turtle.left(90)
        turtle.end_fill()
        turtle.up()

################################
# CONSTANTS
################################
        
BOX_SIZE = 10
BOARD_POS = vec(-150, -100)
# Adding to the piece state rotates the piece clockwise
O_PIECE = ([["....", ".XX.", ".XX.", "...."],
            ["....", ".XX.", ".XX.", "...."],
            ["....", ".XX.", ".XX.", "...."],
            ["....", ".XX.", ".XX.", "...."]], "blue")
T_PIECE = ([["....", ".XXX", "..X.", "...."],
            ["..X.", ".XX.", "..X.", "...."],
            ["..X.", ".XXX", "....", "...."],
            ["..X.", "..XX", "..X.", "...."]], "green")
I_PIECE = ([["..X.", "..X.", "..X.", "..X."],
            ["....", "....", "XXXX", "...."],
            [".X..", ".X..", ".X..", ".X.."],
            ["....", "XXXX", "....", "...."]], "red")
Z_PIECE = ([["....", ".XX.", "..XX", "...."],
            ["..X.", ".XX.", ".X..", "...."],
            ["....", ".XX.", "..XX", "...."],
            ["..X.", ".XX.", ".X..", "...."]], "orange")
S_PIECE = ([["....", "..XX", ".XX.", "...."],
            [".X..", ".XX.", "..X.", "...."],
            ["....", "..XX", ".XX.", "...."],
            [".X..", ".XX.", "..X.", "...."]], "aqua")
J_PIECE = ([["..X.", "..X.", ".XX.", "...."],
            ["....", ".X..", ".XXX", "...."],
            [".XX.", ".X..", ".X..", "...."],
            ["....", "...X", ".XXX", "...."]], "yellow")
L_PIECE = ([[".X..", ".X..", ".XX.", "...."],
            ["....", "..X.", "XXX.", "...."],
            [".XX.", "..X.", "..X.", "...."],
            ["....", "X...", "XXX.", "...."]], "purple")

################################
# PIECE CLASSES
################################

class piece:
    def __init__(self, piece_info):
        self.states = piece_info[0]
        # Some pieces begin at the first row and other at the second
        # so with this if we ensure that the pieces begin at the very top
        self.pos = vec(3, 1 if "X" in self.states[0][0] else 0)
        self.current_state = 0
        self.color = piece_info[1]

    def draw(self):
        drawing_manager.draw_piece(self.pos, self.states[self.current_state], self.color)

class dead_pieces:
    data = []

    @staticmethod
    def init():
        for i in range(20):
            dead_pieces.data.append([])
            for j in range(10):
                dead_pieces.data[i].append("")

    @staticmethod
    def draw():
        drawing_manager.draw_dead_pieces(dead_pieces.data)

drawing_manager.init()
drawing_manager.draw_bg()
