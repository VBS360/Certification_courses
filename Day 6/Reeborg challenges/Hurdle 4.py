def turn_right():
    turn_left()
    turn_left()
    turn_left()

def hurdle_jump():
    turn_left()
    move()
    while wall_on_right():
        move()
    turn_right()
    move()
    turn_right()
    while front_is_clear():
        move()
    turn_left()

def move_past_hurdle():
    move()

while front_is_clear():
    move()
    
while not at_goal():
    if wall_in_front():
        hurdle_jump()
    else:
        move_past_hurdle()

################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
