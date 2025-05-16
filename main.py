import curses
from curses import wrapper
import random
import time
from game import update_ship_position, update_laser_position, generate_alien_row, check_laser_hit, check_game_won, generate_enemy_laser, check_ship_hit
from renderer import draw_game_screen, draw_home_screen, draw_game_won, draw_game_over, animate_ship_explosion
from game_parameters import game_height, game_width

def main(stdscr):
    curses.curs_set(0)
    stdscr.nodelay(True)
    stdscr.timeout(0)

    game_started = False
    ship_pos = game_width / 2
    ship_laser_active = False
    enemy_laser_active = False
    victory = False
    alien_height = 4
    alien_hit = False
    ship_hit = False

    while not game_started:
        # aliens alive at start 1 means alive 0 means destroyed
        aliens = generate_alien_row()

        if victory:
            draw_game_won(stdscr)
        else:
            draw_home_screen(stdscr)
        key = stdscr.getch()
        # Enter to start game
        if key == 10:
            game_started = True

        # Esc to exit
        if key == 27:
            break

        while game_started:
            
            if ship_laser_active:
                if check_laser_hit(aliens, alien_height, ship_laser_pos):
                    alien_hit = True
                    hit_x = max(0, ship_laser_pos[0] - 5)
                    aliens[hit_x] = 0
                    ship_laser_active = False
                else:
                    ship_laser_pos, ship_laser_active = update_laser_position(ship_laser_pos, "ship")

            if enemy_laser_active:
                if check_ship_hit(ship_pos, enemy_laser_pos):
                    ship_hit = True
                    enemy_laser_active = False

                    animate_ship_explosion(ship_pos - 2, game_height - 2, stdscr)

                    draw_game_over(stdscr)
                    game_started = False
                    ship_hit = False
                else:
                    enemy_laser_pos, enemy_laser_active = update_laser_position(enemy_laser_pos, "alien")
            
            draw_game_screen(stdscr, 
                             ship_pos, 
                             ship_laser_active, 
                             enemy_laser_active, 
                             aliens, 
                             alien_height, 
                             ship_laser_pos if ship_laser_active else None,
                             enemy_laser_pos if enemy_laser_active else None,
                             [hit_x, alien_height] if alien_hit else None,
                             ship_hit)
            alien_hit = False


            key = stdscr.getch()
            ship_pos = update_ship_position(ship_pos, key)

            # fire laser (space bar)
            if key == 32 and not ship_laser_active:
                laser_direction = "ship"
                ship_laser_pos = [ship_pos, game_height - 3]
                ship_laser_active = True

            # Esc to exit
            if key == 27:
                victory = False
                game_started = False

            if check_game_won(aliens):
                victory = True
                game_started = False

            # randomly generate enemy laser
            if random.randint(0, 100) > 95 and not enemy_laser_active:
                enemy_laser_active = True
                enemy_laser_pos = generate_enemy_laser()
                

            time.sleep(0.05)

    

        
wrapper(main)