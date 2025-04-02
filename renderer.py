import curses

def draw_home_screen(stdscr):
    stdscr.clear()
    stdscr.addstr(4, 5, "Avoid the incoming lasers and kill the invaders!")
    stdscr.addstr(6, 5, "Use the left and right arrow keys to move and space to shoot.")
    stdscr.addstr(8, 5, "Hit Enter to Start Game...")
    stdscr.refresh()

def draw_game_screen(stdscr, ship_pos):
    stdscr.clear()
    stdscr.addstr(10, ship_pos, "A")
    stdscr.refresh()

