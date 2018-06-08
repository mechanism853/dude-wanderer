import curses

class Display:
    
    @staticmethod
    def safe_char_at(win, y, x, c):
        if y > 0 and x > 0:
            Y,X = win.getmaxyx()
            if y <= Y and x <= X:
                win.mvaddch(y, x, c)
                return True
            else:
                return False
        else:
            return False
        
    @staticmethod
    def print_horizontal_line(win, y, x1, x2, c):
        for x in range(x1, x2+1):
            if not safe_char_at(win, y, x, c):
                break
        
    @staticmethod
    def print_vertical_line()

    @staticmethod
    def print_border_lines(start_y, start_x, )

    @staticmethod
    def main(self.stdscr):
        # Clear screen
        stdscr.clear()
        y = 0
        x = 0
        c = '%'
        while True:
        
            MAX_Y, MAX_X = stdscr.getmaxyx()
            #print horizontal borders
            for i in range():
               stdscr.mvaddch(y, x, c)
               stdscr.mvaddch(

            stdscr.addstr(y, x, c)
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
            elif key == '^[':
                break
            elif len(key) == 1:
                c = key

    def start(self):
        curses.wrapper(self.main)

