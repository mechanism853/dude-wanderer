import curses
import _curses

class UI:
    
    @classmethod
    def safe_char_at(cls, win, y, x, c):
        if y >= 0 and x >= 0:
            Y,X = win.getmaxyx()
            if y < Y and x < X:
                try:
                    win.addch(y, x, c)
                    #win.mv(1, 1)
                except _curses.error as e:
                    return False
                return True
            else:
                return False
        else:
            return False

    @classmethod
    def safe_string_at(cls, win, y, x, s):
        for i in range(len(s)):
            cls.safe_char_at(win, y, x+i, s[i])
        
    @classmethod
    def print_horizontal_line(cls, win, y, x1, x2, c):
        for x in range(x1, x2+1):
            if not cls.safe_char_at(win, y, x, c):
                break
        
    @classmethod
    def print_vertical_line(cls, win, y1, y2, x, c):
        for y in range(y1, y2+1):
            if not cls.safe_char_at(win, y, x, c):
                break

    @classmethod
    def print_frames(cls, win):
        Y,X = win.getmaxyx()
        Y -= 1
        X -= 1

        cls.print_horizontal_line(win, 0, 0, X, '═')
        cls.print_horizontal_line(win, Y-4, 0, X, '═')
        cls.print_horizontal_line(win, Y, 0, X, '═')

        cls.print_vertical_line(win, 0, Y, 0, '║')
        cls.print_vertical_line(win, 0, Y, X, '║')
        cls.print_vertical_line(win, Y-4, Y, X//3, '║')
        cls.print_vertical_line(win, Y-4, Y, 2*X//3, '║')

        cls.safe_char_at(win, 0, 0, '╔')
        cls.safe_char_at(win, 0, X, '╗')
        cls.safe_char_at(win, Y, 0, '╚')
        cls.safe_char_at(win, Y, X, '╝')
        cls.safe_char_at(win, Y-4, 0, '╠')
        cls.safe_char_at(win, Y-4, X, '╣')
        cls.safe_char_at(win, Y-4, X//3, '╦')
        cls.safe_char_at(win, Y-4, 2*X//3, '╦')
        cls.safe_char_at(win, Y, X//3, '╩')
        cls.safe_char_at(win, Y, 2*X//3, '╩')

        cls.safe_string_at(win, Y-4, 2, "STATUS")
        cls.safe_string_at(win, Y-4, (X//3)+2, "TOOLS")
        cls.safe_string_at(win, Y-4, (2*X//3)+2, "DETECT")

    @classmethod
    def main(cls,stdscr):
        # Clear screen
        stdscr.clear()
        y = 0
        x = 0
        c = 'X'
         
        # Initialize          
        curses.curs_set(0)
        stdscr.clear()
        cls.print_frames(stdscr)

        while True:
       
 
            MAX_Y, MAX_X = stdscr.getmaxyx()

            try:
                stdscr.addch(y, x, c)
            except _curses.error as e:
                pass
            stdscr.refresh()
            key = stdscr.getkey()
            if key == 'KEY_UP':
                y = (y - 1) % MAX_Y
            elif key == 'KEY_DOWN':
                y = (y + 1) % MAX_Y
            elif key == 'KEY_LEFT':
                x = (x - 1) % MAX_X
            elif key == 'KEY_RIGHT':
                x = (x + 1) % MAX_X
            elif key == 'KEY_RESIZE':
                stdscr.clear()
                cls.print_frames(stdscr)
            elif key == '^[':
                break
            elif len(key) == 1:
                c = key

    @classmethod
    def start(cls):
        # put in a thread?
        curses.wrapper(cls.main)

UI.start()

