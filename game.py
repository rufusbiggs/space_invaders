import curses
import random
from game_parameters import game_height, game_width

def update_ship_position(ship_pos, key):
    if key == curses.KEY_LEFT and ship_pos > 2:
        ship_pos -= 1
    elif key == curses.KEY_RIGHT and ship_pos < game_width - 2:
        ship_pos += 1

    return ship_pos

def update_laser_position(laser_pos, laser_direction):
    laser_active = True

    if laser_direction == "ship":
        laser_pos[1] -= 1
    elif laser_direction == "alien":
        laser_pos[1] += 1
    
    if laser_pos[1] < 1 or laser_pos[1] > game_height:
        laser_active = False
    
    return laser_pos, laser_active

def move_aliens_down(alien_pos, alien_alive):
    if alien_alive:
        # move all aliens down a space?
        alien_pos -= 1

def generate_alien_row():
    array_length = game_width - 11
    row_aliens = [random.choice([0, 1]) for _ in range(array_length)]

    return row_aliens