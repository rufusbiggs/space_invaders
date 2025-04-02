import curses

def update_ship_position(ship_pos, key):
    if key == curses.KEY_LEFT and ship_pos > 2:
        ship_pos -= 1
    elif key == curses.KEY_RIGHT and ship_pos < 40:
        ship_pos += 1

    return ship_pos

def update_laser_position(laser_pos, laser_direction):
    laser_active = True
    if laser_direction == "ship" and laser_pos[1] > 1:
        laser_pos[1] -= 1
    elif laser_direction == "alien" and laser_pos[1] < 12:
        laser_pos[1] += 1
    elif laser_pos[1] == 1 or laser_pos[1] == 12:
        laser_active = False
    
    return laser_pos, laser_active
