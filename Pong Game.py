import turtle

#window configs and setup
win = turtle.Screen()
win.title =("Pong by PurpleShark2705")
win.bgcolor("black")
win.setup(width = 1000, height = 800)
win.tracer(0)

#score
score_1 = 0
score_2 = 0

#first paddle
paddle_1 = turtle.Turtle()
paddle_1.speed(4)
paddle_1.shape("square")
paddle_1.color("blue")
paddle_1.shapesize(stretch_wid=8, stretch_len=1)
paddle_1.penup()
paddle_1.goto(-450,0)

#second paddle
paddle_2 = turtle.Turtle()
paddle_2.speed(4)
paddle_2.shape("square")
paddle_2.color("red")
paddle_2.shapesize(stretch_wid=8, stretch_len=1)
paddle_2.penup()
paddle_2.goto(450,0)

#ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.shapesize(stretch_len=1.5, stretch_wid=1.5)
ball.penup()
ball.goto(0,0)
ball.dx = 2.5
ball.dy = 1

#pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,360)
pen.write("Player 1: 0  Player 2: 0", align="center", font=("Courier", 24, "bold"))

#Functions
def paddle_1_up():
    y = paddle_1.ycor()
    y += 20
    paddle_1.sety(y)

def paddle_1_down():
    y = paddle_1.ycor()
    y -= 20
    paddle_1.sety(y)

def paddle_2_up():
    y = paddle_2.ycor()
    y += 20
    paddle_2.sety(y)

def paddle_2_down():
    y = paddle_2.ycor()
    y -= 20
    paddle_2.sety(y)

#Keybinds (listens for keyboard input)
win.listen()
win.onkeypress(paddle_1_up, "w") 
win.onkeypress(paddle_1_down, "s")
win.listen()
win.onkeypress(paddle_2_up, "Up")
win.onkeypress(paddle_2_down, "Down")

#game loop (the game code)
while True:
    win.update()

    #move ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #ball hits border
    if ball.ycor() > 385:
        ball.sety(385)
        ball.dy *= -1

    if ball.ycor() < -385:
        ball.sety(-385)
        ball.dy *= -1

    if ball.xcor() > 485:
        ball.goto(0,0)
        ball.dx *= -1
        score_1 += 1
        pen.clear()
        pen.write("Player 1: {}  Player 2: {}".format(score_1, score_2), align="center", font=("Courier", 24, "bold"))
     
    if ball.xcor() < -485:
        ball.goto(0,0)
        ball.dx *= -1
        score_2 += 1
        pen.clear()
        pen.write("Player 1: {}  Player 2: {}".format(score_1, score_2), align="center", font=("Courier", 24, "bold"))
      
    #ball hits paddle
    if ball.xcor() > 430 and ball.xcor() < 440 and (ball.ycor() < paddle_2.ycor() + 50 and ball.ycor() > paddle_2.ycor() - 50):
        ball.setx(430)
        ball.dx *= -1 

    if ball.xcor() < -430 and ball.xcor() < 440 and (ball.ycor() < paddle_1.ycor() + 50 and ball.ycor() > paddle_1.ycor() - 50):
        ball.setx(-430)
        ball.dx *= -1 
