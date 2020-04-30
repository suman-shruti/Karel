from karel.stanfordkarel import *

"""
File: TripleKarel.py
--------------------
When you finish writing this file, TripleKarel should be
able to paint the exterior of three buildings in a given
world, as described in the Assignment 1 handout. You
should make sure that your program works for all of the 
Triple sample worlds supplied in the starter folder.
"""


def main():
    move_to_wall_West()
    turn_left()
    move_to_wall_south()
    turn_left()
    move_to_wall_east()
    turn_right()
    put_beeper()
    move_to_wall_north()
    turn_left()
    move_to_wall_east()
    turn_left()
    move_to_wall_south()
    put_beeper()
    turn_right()
    move_to_wall_east()
    turn_left()
    move_to_wall_north()
    turn_left()
    move_to_wall_final()

def move_to_wall_West():
    while left_is_blocked():
        put_beeper()
        move()
    else:
        no_beepers_in_bag()

def move_to_wall_south():
    move()
    while left_is_blocked():
        put_beeper()
        move()
    else:
        no_beepers_in_bag()

def move_to_wall_east():
    move()
    while left_is_blocked():
        put_beeper()
        move()
    else:
        no_beepers_in_bag()

def move_to_wall_north():
    move()
    while left_is_blocked():
        put_beeper()
        move()
    else:
        no_beepers_in_bag()

def move_to_wall_final():
    if front_is_clear():
        move()
        move_to_wall_West()
        while front_is_blocked():
            no_beepers_in_bag()



def turn_right():
    for i in range(3):
        turn_left()


# There is no need to edit code beyond this point

if __name__ == "__main__":
    run_karel_program()
