from pygame import *
from time import sleep, time as timer
from random import randint

w = 700
h = 500

window = display.set_mode((w, h))
display.set_caption("ping pong")
window.fill((100,200,150))







class GameSprite(sprite.Sprite):
    def __init__(self, image_filename, x, y, w, h, speed):
        super().__init__()
        self.image = transform.scale(image.load(image_filename), (w, h))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed
        self.direction = 'left'
        self.image_filename = image_filename

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_l(self):
        keys_pressed = key.get_pressed()

        # left and right
        if keys_pressed[K_UP] and (self.rect.y - self.speed) > 0:
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN] and (self.rect.y + self.speed) < (h - 150):            
            self.rect.y += self.speed
    def update_r(self):
        keys_pressed = key.get_pressed()

        # left and right
        if keys_pressed[K_w] and (self.rect.y - self.speed) > 0:
            self.rect.y -= self.speed
        if keys_pressed[K_s] and (self.rect.y + self.speed) < (h - 150):
            self.rect.y += self.speed

p1 = Player('paddle.png', 30, 200, 50, 150, 4)
p2 = Player('paddle.png', 620, 200, 50, 150, 4)
ball = GameSprite('ball (4).png', 200, 200, 50, 50, 4)



fps = 120
clock = time.Clock()
game = True 
while game :
    for e in event.get():
        if e.type == QUIT:
            game = False









    p2.update_l()
    p1.update_r()

    window.fill((100,200,150))
    p1.reset()
    p2.reset()
    ball.reset()


    display.update()
    clock.tick(fps)