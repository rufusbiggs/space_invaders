import curses
from game_parameters import game_height, game_width

def draw_home_screen(stdscr):
    stdscr.clear()
    stdscr.addstr(4, 5, "Avoid the incoming lasers and kill the invaders!")
    stdscr.addstr(6, 5, "Use the left and right arrow keys to move and space to shoot.")
    stdscr.addstr(8, 5, "Hit Enter to Start Game...")
    stdscr.refresh()

def draw_game_screen(stdscr, ship_pos, laser_active, aliens, alien_pos, laser_pos):
    stdscr.clear()
    # create background
    for i in range(0, game_height):
        stdscr.addstr(i, 1, "|")
        stdscr.addstr(i, game_width - 1, "|")

    # add ship
    stdscr.addstr(game_height - 2, ship_pos, "A")

    # add aliens
    for i in aliens:
        if aliens[i] == 1:
            stdscr.addstr(alien_pos, i + 5, "M")

    # display laser
    if laser_active:
        stdscr.addstr(laser_pos[1], laser_pos[0], "|")
    stdscr.refresh()


    

