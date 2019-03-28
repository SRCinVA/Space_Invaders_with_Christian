# Space Invaders - Part 1
# Set up the screen
# He's typing this on Python 2.7

import turtle
import os
import math
import random

#Set up screen
wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Space Invaders")

#Draw border
border_pen = turtle.Turtle()
border_pen.speed(0) #oddly, "0" is the fastest
border_pen.color("white")
border_pen.penup()

border_pen.setposition(-300,-300) #starting to the left and down
border_pen.pendown()
border_pen.pensize(3)
for side in range(4): #to draw a square, starting at (-300,-300)
    border_pen.fd(600)
    border_pen.lt(90)
border_pen.hideturtle()

#Create the player turtle
player = turtle.Turtle()
player.color("blue")
player.shape("triangle")
player.penup()
player.speed(0)
player.setposition(0,-250)
player.setheading(90)

playerspeed = 15

#Choose number of enemies
number_of_enemies = 5

#Create an empty list of enemies
enemies = []

#add enemies to the list
for i in range(number_of_enemies):
    #Create the enemy
    enemies.append(turtle.Turtle()) #appending 5 turtle

for enemy in enemies: #give attributes to that turtle using a list.
    enemy.color("red")
    enemy.shape("circle")
    enemy.penup()
    enemy.speed(0)
    x = random.randint(-200,200) #to randomize where the enemies first appear
    y = random.randint(100,250) # to randomize where the enemies first appear

    enemy.setposition(x,y) # they'll each start at a different spot.

enemyspeed = 2

#Create the player's bullet
bullet = turtle.Turtle()
bullet.color("yellow")
bullet.shape("triangle")
bullet.penup()
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(0.5,0.5) #half the x height and y height
bullet.hideturtle()

bulletspeed = 20

#Define bullet state
#ready - ready to fire
#fire - bullet is firing
bulletstate = "ready"

#Move the player left and right
def move_left():
    x = player.xcor()
    x -= playerspeed
    if x < -280:
        x = -280
    player.setx(x) #sets x coord to the new x.


def move_right():
    x = player.xcor()
    x += playerspeed
    if x > 280:
        x = 280
    player.setx(x)  # sets x coord to the new x.

def fire_bullet():
    #Declare bulletstate as a global if it is changed
    global bulletstate
    if bulletstate == "ready":
        bulletstate = "fire"
    #above, so it can operate outside of the function and not just disappear
        x = player.xcor()
        y = player.ycor() + 10
        bullet.setposition(x,y)
        bullet.showturtle()

def isCollision(t1,t2): #isX convention usually tells us it's a Boolean.
    distance = math.sqrt(math.pow(t1.xcor()-t2.xcor(),2)+math.pow(t1.ycor()-t2.ycor(),2))
    if distance < 15:
        return True
    else:
        return False

#Create keyboard bindings
turtle.listen() #tells turtle to listen
turtle.onkey(move_left, "Left") #"Left" is the literal left arrow key.
turtle.onkey(move_right, "Right")  # "Right" is the literal left arrow key.
turtle.onkey(fire_bullet, "space")

#delay = raw_input("Press enter to play")

#Main game loop
while True: #you could think of this as "forever"
    
    for enemy in enemies: # for all of the enemies now, not just one.
    
    #Move the enemy
        x = enemy.xcor()
        x += enemyspeed
        enemy.setx(x)

        #Move the enemy back and down
        if enemy.xcor() > 280:
            y = enemy.ycor()
            y -= 40 #when hits boundary, moves down
            enemyspeed *= -1 #to reverse directions
            enemy.sety(y)

        if enemy.xcor() < -280:
            y = enemy.ycor()
            y -= 40  # when hits boundary, moves down
            enemyspeed *= -1 #to reverse directions
            enemy.sety(y)

            #Check for collision of bullet and the enemy
        if isCollision(bullet, enemy):
            #Reset the bullet
            bullet.hideturtle()
            bulletstate = "ready"
            bullet.setposition(0, -400)
            # to randomize where the enemies first appear
            x = random.randint(-200, 200)
            y = random.randint(100, 250)  # to randomize where the enemies first appear
            enemy.setposition(x,y)


        if isCollision(player, enemy):
            player.hideturtle()
            enemy.hideturtle()
            print("Game Over")
            break

#The main loop will go over all of these, 
#and then check the bullet's status.

    #Move the bullet
    if bulletstate == "fire":
        y = bullet.ycor()
        y += bulletspeed
        bullet.sety(y)

    #Check to see if bullet has reached top
    if bullet.ycor() > 275:
        bullet.hideturtle()
        bulletstate = "ready"

wn.mainloop()
    
