# Space Invaders - Part 1
# Set up the screen
# He's typing this on Python 2.7

import turtle
import os


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

#Create the enemy
enemy = turtle.Turtle()
enemy.color("red")
enemy.shape("circle")
enemy.penup()
enemy.speed(0)
enemy.setposition(-200,250)

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

#Create keyboard bindings
turtle.listen() #tells turtle to listen
turtle.onkey(move_left, "Left") #"Left" is the literal left arrow key.
turtle.onkey(move_right, "Right")  # "Right" is the literal left arrow key.
turtle.onkey(fire_bullet, "space")

#delay = raw_input("Press enter to play")

#Main game loop
while True: #you could think of this as "forever"
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
