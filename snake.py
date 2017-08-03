import turtle
import random
#We'll need this later in the lab

turtle.tracer(1,0) #This helps the turtle move more smoothly
turtle.fillcolor("blue")
SIZE_X=500
SIZE_Y=500
turtle.setup(SIZE_X+50,SIZE_Y+50) #
#Curious? It's the turtle window
#size.
turtle_border = turtle.clone()
turtle_border.penup()
turtle_border.goto(-250,-250)
turtle_border.pendown()
turtle_border.goto(-250,250)
turtle_border.goto(250,250)
turtle_border.goto(250,-250)
turtle_border.goto(-250,-250)

turtle.penup()
SQUARE_SIZE = 20
START_LENGTH = 1
#Initialize lists
pos_list = []
stamp_list = []
food_pos = []
food_stamps = []
#Set up positions (x,y) of boxes that make up the snake
snake = turtle.clone()
snake.shape("circle")
score=turtle.clone()
x=0


    
    
    
#Hide the turtle object (it's an arrow - we don't need to see it)
for snake_1 in range(START_LENGTH):
    x_pos=snake.pos()[0]
    y_pos=snake.pos()[1]
    x_pos = x_pos + SQUARE_SIZE
    my_pos=(x_pos,y_pos)
    snake.goto(x_pos,y_pos)
    pos_list.append(my_pos)
    snake_current_place=snake.stamp()
    stamp_list.append(snake_current_place)

turtle.register_shape("trash.gif")
food = turtle.clone()
food.shape("trash.gif")
turtle.hideturtle()
UP_ARROW="Up"
LEFT_ARROW="Left"
DOWN_ARROW = "Down"
RIGHT_ARROW = "Right"
TIME_STEP = 100
SPACE_BAR = "space"
UP=0
LEFT = 1
DOWN = 2
RIGHT  =3
direction = UP
UP_EDGE = SIZE_Y / 2
DOWN_EDGE = -(SIZE_Y / 2)
RIGHT_EDGE = SIZE_X / 2
LEFT_EDGE = -(SIZE_X / 2)

def up():
    global direction
    direction = UP
    print("You pressed the up key")
    
def down():
    global direction
    direction = DOWN
    print("You presses the down key")
    
def left():
    global direction
    direction = LEFT
    print("You presssed the left key")
    
def right():
    global direction
    direction = RIGHT
    print("You pressed the right key")
    
turtle.onkeypress(up,UP_ARROW)
turtle.onkeypress(down,DOWN_ARROW)
turtle.onkeypress(left,LEFT_ARROW)
turtle.onkeypress(right,RIGHT_ARROW)
turtle.listen()

def make_food():
    min_x=-int(SIZE_X/2/SQUARE_SIZE)## -12
    max_x=int(SIZE_X/2/SQUARE_SIZE) ## 12
    min_y=-int(SIZE_Y/2/SQUARE_SIZE)## -12
    max_y= int(SIZE_Y/2/SQUARE_SIZE) ##-1 12
    food_x = random.randint(min_x,max_x)*SQUARE_SIZE ##-240
    food_y = random.randint(min_y,max_y)*SQUARE_SIZE ## -240
    food.goto(food_x,food_y)
    food_pos.append((food_x,food_y))
    stamp = food.stamp()
    food_stamps.append(stamp)
    

def move_snake():
    global direction
    my_pos = snake.pos()
    x_pos= my_pos[0]
    y_pos= my_pos[1]
    if direction == RIGHT:
        snake.goto(x_pos + SQUARE_SIZE, y_pos)
        print("You moved right!")
    elif direction == LEFT:
        snake.goto(x_pos - SQUARE_SIZE, y_pos)
        print("You moved left")
    elif direction == UP:
        snake.goto(x_pos, y_pos + SQUARE_SIZE)
    elif direction == DOWN:
        snake.goto(x_pos, y_pos - SQUARE_SIZE)
        
    new_pos = snake.pos()
    new_x_pos = new_pos[0]
    new_y_pos = new_pos[1]
    
    if new_x_pos >= RIGHT_EDGE:
        print ("You hit the right edge! Game over!")
        quit()
    if new_x_pos <= LEFT_EDGE:
        print ("You hit the left edge! Game over!")
        quit()
    if new_y_pos >= UP_EDGE:
        print ("You hit the up edge! Game over!")
        quit()
    if new_y_pos <= DOWN_EDGE:
        print ("You hit the down edge! Game over!")
        quit()
    if new_pos in pos_list[:-1]:
        print("You die! Game over")
        quit()
       
    my_pos=snake.pos()
    pos_list.append(my_pos)
    #pos_list.pop(0)
    new_stamp = snake.stamp()
    stamp_list.append(new_stamp)
    global food_stamps , food_pos,x
    if snake.pos() in food_pos:
        food_ind = food_pos.index (snake.pos())
        food.clearstamp (food_stamps[food_ind])
        food_pos.pop(food_ind)
        food_stamps.pop(food_ind)
        print("You have eaten the food!")
        make_food()
        stamp_list.append(new_stamp)
        pos_list.append(snake.pos())
        x=x+1
        score.clear()
        score.write ("score: " + str(x))
        
    else:
        old_stamp=stamp_list.pop(0)
        snake.clearstamp(old_stamp)
        pos_list.pop(0)
        
            
        

    turtle.ontimer(move_snake,TIME_STEP)

make_food()
move_snake()
