import curses

def update_ship_position(ship_pos, key):
    if key == curses.KEY_LEFT and ship_pos > 2:
        ship_pos -= 1
    elif key == curses.KEY_RIGHT and ship_pos < 40:
        ship_pos += 1

    return ship_pos
