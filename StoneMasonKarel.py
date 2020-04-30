from karel.stanfordkarel import *

"""
File: StoneMasonKarel.py
------------------------
When you finish writing code in this file, StoneMasonKarel should 
solve the "repair the quad" problem from Assignment 1. You
should make sure that your program works for all of the 
sample worlds supplied in the starter folder.
"""


def main():
    for i in range(4):
        if front_is_clear():
            fill_column()
            if front_is_blocked():
                turn_left()
                for i in range(4):
                    move()
            else:
                no_beepers_in_bag()
        else:
            no_beepers_in_bag()
    if front_is_blocked():
        fill_column()




def fill_column():
    turn_left()
    while front_is_clear():
        if no_beepers_present():
            put_beeper()
        else:
            move()
    if front_is_blocked():
        while no_beepers_present():
            put_beeper()
    turn_left()
    turn_left()
    while front_is_clear():
        move()

# There is no need to edit code beyond this point

if __name__ == "__main__":
    run_karel_program()
