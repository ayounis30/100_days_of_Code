def turn_right():
    turn_left()
    turn_left()
    turn_left()

def follow_right_edge():
    while not at_goal():
        if right_is_clear():
            turn_right()
            move()
        elif front_is_clear():
            move()
        else:
            turn_left()

# Test the function
follow_right_edge()
