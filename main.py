import pgzrun
import random

WIDTH = 1300
HEIGHT = 1000
TITLE = "Flappy ball game"

R = random.randint(0,255)
G = random.randint(0,255)
B = random.randint(0,255)

CLR =(R,G,B)

GRAVITY = 2000.0

class Ball () :
    def __init__(self,initial_x,initial_y):
        self.x = initial_x
        self.y = initial_y
        self.vx = 200
        self.vy = 0
        self.radius = 40

    def draw_circle(self):
        pos=(self.x,self.y)
        screen.draw.filled_circle(pos,self.radius,CLR)

# Objects for ball class:

ball = Ball(50,50)

def draw():
    screen.clear()
    screen.fill("white")
    ball.draw_circle()

def update(dt):
    # v = u +(a*t) 
    # v-final velocity
    # a-accelaration
    # u-initial velocity
    # t-time taken
    uy=ball.vy
    ball.vy = ball.vy + (GRAVITY*dt)
    
    #displacement
    #s = (u+v)/2*t
    ball.y +=(uy + ball.vy)*0.5*dt

    if ball.y > HEIGHT:
        ball.y = HEIGHT - ball.radius
        ball.vy =- ball.vy * 0.9

    ball.x +=ball.vx*dt

    if ball.x > WIDTH - ball.radius or ball.x < ball.radius:
        ball.vx = -ball.vx

def on_key_down(key):
    if key == keys.UP:
        ball.vy = -500




pgzrun.go()
        