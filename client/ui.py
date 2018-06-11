import curses
import _curses

class UI:

    def __init__(self):
        self.win = None
        self.Y = 0
        self.X = 0

    ##
    # Attempts to a replace character in the window at given coordinates
    #
    # @param y
    # @param x
    # @param c
    # @return A boolean reporting whether the replacement was successful
    ##
    def safe_char_at(self, y, x, c) -> bool:
        if y >= 0 and y <= self.Y:
            if x >= 0 and x <= self.X:
                try:
                    self.win.addch(y, x, c)
                except _curses.error as e:
                    return False
                return True
            else:
                return False
        else:
            return False

    def safe_string_at(self, y, x, s):
        for i in range(len(s)):
            if not self.safe_char_at(y, x+i, s[i]):
                break
        
    def print_horizontal_line(self, y, x1, x2, c):
        for x in range(x1, x2+1):
            if not self.safe_char_at(y, x, c):
                break
        
    def print_vertical_line(self, y1, y2, x, c):
        for y in range(y1, y2+1):
            if not self.safe_char_at(y, x, c):
                break

    def update_YX(self):
        self.Y, self.X = self.win.getmaxyx()
        self.Y -= 1
        self.X -= 1

    def print_frames(self):

        # border lines        
        self.print_horizontal_line(        0, 0, self.X, '═')
        self.print_horizontal_line( self.Y-4, 0, self.X, '═')
        self.print_horizontal_line(   self.Y, 0, self.X, '═')

        self.print_vertical_line(        0, self.Y,           0, '║')
        self.print_vertical_line(        0, self.Y,      self.X, '║')
        self.print_vertical_line( self.Y-4, self.Y,   self.X//3, '║')
        self.print_vertical_line( self.Y-4, self.Y, 2*self.X//3, '║')

        # corner pieces
        self.safe_char_at(        0,           0, '╔')
        self.safe_char_at(        0,      self.X, '╗')
        self.safe_char_at(   self.Y,           0, '╚')
        self.safe_char_at(   self.Y,      self.X, '╝')
        self.safe_char_at( self.Y-4,           0, '╠')
        self.safe_char_at( self.Y-4,      self.X, '╣')
        self.safe_char_at( self.Y-4,   self.X//3, '╦')
        self.safe_char_at( self.Y-4, 2*self.X//3, '╦')
        self.safe_char_at(   self.Y,   self.X//3, '╩')
        self.safe_char_at(   self.Y, 2*self.X//3, '╩')
        
        # labels
        self.safe_string_at(        0,               2, "DUDE WANDERER")
        self.safe_string_at( self.Y-4,               2,        "STATUS")
        self.safe_string_at( self.Y-4,   (self.X//3)+2,         "TOOLS")
        self.safe_string_at( self.Y-4, (2*self.X//3)+2,        "DETECT")

    def main(self,stdscr):
        # Initialize
        curses.curs_set(0)

        self.win = stdscr
        self.win.clear()
        self.update_YX()
        self.print_frames()

        # Vestigial
        y = 1
        x = 1
        c = '%'

        while True:
            self.safe_char_at(y, x, c)
            stdscr.refresh()
            key = stdscr.getkey()
            if key == 'KEY_UP':
                y = (y - 1) % self.Y
            elif key == 'KEY_DOWN':
                y = (y + 1) % self.Y
            elif key == 'KEY_LEFT':
                x = (x - 1) % self.X
            elif key == 'KEY_RIGHT':
                x = (x + 1) % self.X
            elif key == 'KEY_RESIZE':
                self.update_YX()                
                self.win.clear()
                self.print_frames()
            elif key == '^[':
                break
            elif len(key) == 1:
                c = key

    def start(self):
        # put inside a thread?
        curses.wrapper(self.main)

my_ui = UI()
my_ui.start()

