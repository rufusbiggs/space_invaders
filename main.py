from curses import wrapper
from game import update_ship_position
from renderer import draw_game_screen, draw_home_screen

def main(stdscr):
    game_started = False
    ship_pos = 21

    while not game_started:
        draw_home_screen(stdscr)
        key = stdscr.getch()
        # Enter to start game
        if key == 10:
            game_started = True

        # Esc to exit
        if key == 27:
            break

    while game_started:
        draw_game_screen(stdscr, ship_pos)
        key = stdscr.getch()
        ship_pos = update_ship_position(ship_pos, key)

        # Esc to exit
        if key == 27:
            break

wrapper(main)