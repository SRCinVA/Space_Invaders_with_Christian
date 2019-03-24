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

#Move the player left and right
def move_left():
    x = player.xcor()
    x -= playerspeed
    player.setx(x) #sets x coord to the new x.


#Create keyboard bindings
turtle.listen() #tells turtle to listen
turtle.onkey(move_left, "Left") #"Left" is the literal left arrow key.


#delay = raw_input("Press enter to play")

wn.mainloop()