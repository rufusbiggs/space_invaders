import curses

def draw_home_screen(stdscr):
    stdscr.clear()
    stdscr.addstr(5, 5, "Hit Enter to Start Game!")

def draw_game_screen(stdscr, ship_pos):
    stdscr.clear()
    stdscr.addstr(ship_pos, 80, "A")

