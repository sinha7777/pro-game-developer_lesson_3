import pgzrun
import random

WIDTH = 1300
HEIGHT = 1000
TITLE = "bouncing ball"
GRAVITY = 2000.0

class Ball:
    def __init__(self, x, y, radius, color, bounce):
        self.x = x
        self.y = y
        self.vx = random.randint(150, 300)
        self.vy = 0
        self.radius = radius
        self.color = color
        self.bounce = bounce

    def draw_circle(self):
        screen.draw.filled_circle((self.x, self.y), self.radius, self.color)

    def update(self, dt):
        uy = self.vy
        self.vy += GRAVITY * dt
        self.y += (uy + self.vy) * 0.5 * dt
        if self.y > HEIGHT - self.radius:
            self.y = HEIGHT - self.radius
            self.vy = -self.vy * self.bounce
        self.x += self.vx * dt
        if self.x > WIDTH - self.radius or self.x < self.radius:
            self.vx = -self.vx

balls = []
for i in range(5):
    color = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
    radius = 40
    bounce = random.uniform(0.6, 0.95)
    x = random.randint(radius, WIDTH - radius)
    y = random.randint(radius, HEIGHT // 2)
    balls.append(Ball(x, y, radius, color, bounce))

def draw():
    screen.clear()
    screen.fill("white")
    for ball in balls:
        ball.draw_circle()

def update(dt):
    for ball in balls:
        ball.update(dt)

def on_key_down(key):
        if key == keys.UP:
            for ball in balls:
                ball.vy = -500

pgzrun.go()
