
import turtle

from turtle import *

window = Screen()
window.bgcolor("black")

tess = Turtle()
tess.pensize(5)
tess.color("white")

def gameBoard() :
 tess.speed(0)
 tess.forward(333 / 2)
 tess.backward(333)
 tess.forward(111)
 tess.right(90)
 tess.forward(222)
 tess.backward(111)
 tess.left(90)
 tess.forward(222)
 tess.backward(333)
 tess.forward(222)
 tess.right(90)
 tess.forward(111)
 tess.backward(333)
 tess.penup()
 tess.right(90)
 tess.forward(111)
 tess.left(90)
 tess.pendown()
 tess.forward(111)
 
def cross() :
    tess.speed(2)
    tess.penup()
    tess.forward(diagonal / 10)
    tess.pendown()
    tess.forward((8*diagonal)/10)
    tess.backward(((8*diagonal)/10) / 2)
    tess.right(90)
    tess.forward(((8*diagonal)/10) // 2)
    tess.backward((8*diagonal)/10)
    tess.speed(0)
    
def square() :
    tess.speed(2)
    tess.penup()
    tess.forward(111 / 10)
    tess.pendown()
    for _ in range(4):
        tess.forward(888/10)
        tess.right(90)
        
    tess.speed(0)
        
def reset() :
    tess.penup()
    tess.goto(55.50, -222.0)
    tess.setheading(90)
    tess.pendown()
     
def player1() :
    
    
    if (m == 1) :
       tess.penup()
       tess.forward(222)
       tess.left(90)
       tess.forward(111)
       tess.right(45)
       cross()
    
    if (m == 2) :
       tess.penup()
       tess.forward(222)
       tess.left(45)
       cross()
       
    if (m == 3) :
       tess.forward(222)
       tess.right(45)
       cross()

    if (m == 4) :
       tess.forward(111)
       tess.left(90)
       tess.forward(111)
       tess.right(45)
       cross()
   
    if (m == 5) :
       tess.forward(111)
       tess.left(45)
       cross()
    
    if (m == 6) :
       tess.forward(111)
       tess.right(45)
       cross()
    
    if (m == 7) :
       tess.penup()
       tess.left(90)
       tess.forward(111)
       tess.right(45)
       tess.pendown()
       cross()
    
    if (m == 8) :
       tess.left(45)
       cross()
    
    if (m == 9) :
       tess.right(45)
       cross()        
   
def player2() :
    
    
    
    if (x == 1) :
       tess.forward(222)
       tess.left(90)
       tess.forward(111+(999/10))
       tess.right(90)
       tess.penup()
       square()
    if (x == 2) :
       tess.forward(222)
       tess.left(90)
       tess.forward(999/10)
       tess.right(90)
       square()
    
    if (x == 3) :
       tess.forward(222)
       tess.left(90)
       tess.backward(111/10)
       tess.right(90)
       square()

    if (x == 4) :
       tess.forward(111)
       tess.left(90)
       tess.forward(111)
       tess.forward(999/10)
       tess.right(90)
       square()
        
    if (x == 5) :
       tess.forward(111)
       tess.left(90)
       tess.forward(999/10)
       tess.right(90)
       square()
        
    if (x == 6) :
       tess.forward(111)
       tess.left(90)
       tess.backward(111/10)
       tess.right(90)
       square()
        
    if (x == 7) :
       tess.penup()
       tess.left(90)
       tess.forward(111)
       tess.forward(999/10)
       tess.right(90)
       square()
     
    if (x == 8) :
       tess.penup()
       tess.left(90)
       tess.forward(999/10)
       tess.right(90)
       square()
        
    if (x == 9) :
       tess.penup()
       tess.left(90)
       tess.backward(111/10)
       tess.right(90)
       square()
       
diagonal = int((2*(111**2))**(1/2))

# Built the tic-tac-toe board. And defined all required functions.
# start pos of tess will always be (55.50, -222.0)  

gameBoard()

reset()

n = input("Which tile does Player 1 want to place a cross in? = ")
m = int(n)
player1()

reset()

n = input("Player 2's turn, where to square, Player 2? = ")
x = int(n)
if (x != m) :
   player2()
   
else :
   print("Invalid Input, restart the game")
   exit()
   

oldm = m
oldx = x

for _ in range(7) :
   
   reset()
   
   n = input("Which tile does Player 1 want to place a cross in? = ")
   m = int(n)
   if (m != oldx and m != oldm) :
      player1()
   else :
      print("Invalid Input, restart the game")
      exit()
      
   oldm = m
   
   reset()
   
   n = input("Player 2's turn, where to square, Player 2? = ")
   x = int(n)
   if (x != oldm and x != oldx) :
      player2()
   else :
      print("Invalid Input, restart the game")
      exit()
      
   oldx = x

    







window.exitonclick()



