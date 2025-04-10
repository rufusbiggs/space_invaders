import curses
from curses import wrapper
import time
from game import update_ship_position, update_laser_position, generate_alien_row
from renderer import draw_game_screen, draw_home_screen
from game_parameters import game_height

def main(stdscr):
    curses.curs_set(0)
    stdscr.nodelay(True)
    stdscr.timeout(0)

    game_started = False
    ship_pos = game_height / 2
    laser_active = False

    # aliens alive at start 1 means alive 0 means destroyed
    aliens = generate_alien_row()
    alien_pos = 4

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
        if laser_active:
            draw_game_screen(stdscr, ship_pos, laser_active, aliens, alien_pos, laser_pos)
            laser_pos, laser_active = update_laser_position(laser_pos, laser_direction)
        else:
            draw_game_screen(stdscr, ship_pos, laser_active, aliens, alien_pos, laser_pos=None)

        key = stdscr.getch()
        ship_pos = update_ship_position(ship_pos, key)

        # fire laser (space bar)
        if key == 32:
            laser_direction = "ship"
            laser_pos = [ship_pos, game_height - 3]
            laser_active = True

        # Esc to exit
        if key == 27:
            break

        time.sleep(0.05)
 
wrapper(main)