import curses
from game_parameters import game_height, game_width

def draw_home_screen(stdscr):
    stdscr.clear()
    stdscr.addstr(4, 5, "Avoid the incoming lasers and kill the invaders!")
    stdscr.addstr(6, 5, "Use the left and right arrow keys to move and space to shoot.")
    stdscr.addstr(8, 5, "Hit Enter to Start Game...")
    stdscr.refresh()

def draw_game_screen(stdscr, ship_pos, ship_laser_active, enemy_laser_active, aliens, alien_height, ship_laser_pos, enemy_laser_pos, enemy_hit, ship_hit):
    
    stdscr.clear()
    # create background
    for i in range(0, game_height):
        stdscr.addstr(i, 1, "|")
        stdscr.addstr(i, game_width - 1, "|")

    # add ship
    if not ship_hit:
        stdscr.addstr(game_height - 2, ship_pos, "A")

    # add aliens
    for i, alien in enumerate(aliens):
        if alien == 1:
            stdscr.addstr(alien_height, i + 5, "M")

    # display laser
    if ship_laser_active:
        stdscr.addstr(ship_laser_pos[1], ship_laser_pos[0], "|")
    stdscr.refresh()

    if enemy_laser_active and not ship_hit:
        stdscr.addstr(enemy_laser_pos[1], enemy_laser_pos[0], "*")
    stdscr.refresh()

    if enemy_hit:
        stdscr.addstr(ship_hit[1], ship_hit[0] + 5, "X")
    stdscr.refresh()

def draw_game_won(stdscr):
    stdscr.clear()
    stdscr.addstr(4, 5, "VICTORY!!!")
    stdscr.addstr(8, 5, "Hit Enter to Start new Game...")
    stdscr.refresh()

def draw_game_over(stdscr):
    stdscr.clear()
    stdscr.addstr(4, 5, "Game Over!!!")
    stdscr.addstr(8, 5, "Hit Enter to Start new Game...")
    stdscr.refresh()
    

def animate_ship_explosion(ship_pos, height, stdscr):
    explosion_frames = [
        "  X  ",
        " X X ",
        "XXXXX",
        " X X ",
        "  X  "
    ]
    frame_delay = 100
    explosion_time = 2000
    time_elapsed = 0

    while time_elapsed < explosion_time:
        for frame in explosion_frames:
            stdscr.addstr(height, ship_pos, frame)
            stdscr.refresh()
            curses.napms(frame_delay)  # Adjust the delay as needed
            stdscr.addstr(height, ship_pos, "     ")  # Clear the explosion
            time_elapsed += frame_delay
            if time_elapsed >= explosion_time:
                break