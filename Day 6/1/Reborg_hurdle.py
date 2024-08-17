def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def jump_hurdle ():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

for hurdle in range (6):
    jump_hurdle()
    
#jump_hurdle ()
#jump_hurdle ()
#jump_hurdle ()
#jump_hurdle ()
#jump_hurdle ()
#jump_hurdle ()