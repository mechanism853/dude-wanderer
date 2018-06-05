#!/usr/bin/env python3
import curses

def main(stdscr):
    # Clear screen
    stdscr.clear()
    y = 0
    x = 0
    c = '%'
    while True:
        MAX_Y, MAX_X = stdscr.getmaxyx()
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

curses.wrapper(main)

