"""
Copy the code from the previous lesson, 08a_More_Turtle_programs.ipynb, 
from the section "Change the Turtle Image"

Then change the code so that the turtle has a different image ( look in the 'images'
directory ) and moves to the corners of the screen in a square pattern. 
"""
import turtle as turtle

screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.bgcolor('')





t1 = turtle.Turtle()
t1.penup()
t1.shape("turtle")

t2 = turtle.Turtle()
t2.penup()
t2.shape("arrow")

for i in range(-200, 200):
    t1.goto(i,i)
    t2.goto(i,-i)

t1.forward(40)
t2.forward(35)






