import curses
from game_parameters import game_height, game_width

def draw_home_screen(stdscr):
    stdscr.clear()
    stdscr.addstr(4, 5, "Avoid the incoming lasers and kill the invaders!")
    stdscr.addstr(6, 5, "Use the left and right arrow keys to move and space to shoot.")
    stdscr.addstr(8, 5, "Hit Enter to Start Game...")
    stdscr.refresh()

def draw_game_screen(stdscr, ship_pos, ship_laser_active, enemy_laser_active, aliens, alien_height, ship_laser_pos, enemy_laser_pos, ship_hit):
    
    stdscr.clear()
    # create background
    for i in range(0, game_height):
        stdscr.addstr(i, 1, "|")
        stdscr.addstr(i, game_width - 1, "|")

    # add ship
    stdscr.addstr(game_height - 2, ship_pos, "A")

    # add aliens
    for i, alien in enumerate(aliens):
        if alien == 1:
            stdscr.addstr(alien_height, i + 5, "M")

    # display laser
    if ship_laser_active:
        stdscr.addstr(ship_laser_pos[1], ship_laser_pos[0], "|")
    stdscr.refresh()

    if enemy_laser_active:
        stdscr.addstr(enemy_laser_pos[1], enemy_laser_pos[0], "*")
    stdscr.refresh()

    if ship_hit:
        stdscr.addstr(ship_hit[1], ship_hit[0] + 5, "X")
    stdscr.refresh()

def draw_game_won(stdscr):
    stdscr.clear()
    stdscr.addstr(4, 5, "VICTORY!!!")
    stdscr.addstr(8, 5, "Hit Enter to Start new Game...")
    stdscr.refresh()
    

