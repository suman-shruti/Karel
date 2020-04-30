from karel.stanfordkarel import *

"""
File: CheckerboardKarel.py
----------------------------
When you finish writing it, CheckerboardKarel should draw
a checkerboard using beepers, as described in Assignment 1. 
You should make sure that your program works for all of the 
sample worlds supplied in the starter folder.
"""


def main():
    checker_board()
    turn_left()
    put_beeper()
    move()
    move()
    put_beeper()
    move()
    move()
    put_beeper()
    move()
    move()
    put_beeper()
    move()
    turn_left()
    turn_left()
    turn_left()
    move()
    turn_left()
    turn_left()
    turn_left()
    put_beeper()
    move()
    move()
    put_beeper()
    move()
    move()
    put_beeper()
    move()
    move()
    put_beeper()
    move()


def checker_board():
    for i in range(3):
        put_beeper()
        turn_left()
        move()
        move()
        put_beeper()
        move()
        move()
        put_beeper()
        move()
        move()
        put_beeper()
        move()
        turn_left()
        turn_left()
        turn_left()
        move()
        turn_left()
        turn_left()
        turn_left()
        put_beeper()
        move()
        move()
        put_beeper()
        move()
        move()
        put_beeper()
        move()
        move()
        put_beeper()
        move()
        turn_left()
        move()








# There is no need to edit code beyond this point

if __name__ == "__main__":
    run_karel_program()
