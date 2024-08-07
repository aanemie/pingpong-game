from pygame import *
from random import randint
from time import time as kub
lost = 0
score = 0
rel_time = False
num_fire = 0


class GameSprite(sprite.Sprite):
    def __init__(self, image1, resolution1, resolution2, speed1, x1, y1):
        sprite.Sprite.__init__(self)
        self.image = transform.scale(image.load(image1), (resolution1, resolution2))
        self.speed = speed1
        self.rect = self.image.get_rect()
        self.rect.x = x1
        self.rect.y = y1

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self, direction):
        if direction == "left":

            keys_pressed = key.get_pressed()
            if keys_pressed[K_w] and self.rect.y > 20:
                self.rect.y -= self.speed 

            if keys_pressed[K_s] and self.rect.y < 780:
                self.rect.y += self.speed 


        if direction == "right":

            keys_pressed = key.get_pressed()
            if keys_pressed[K_UP] and self.rect.y > 20:
                self.rect.y -= self.speed 

            if keys_pressed[K_DOWN] and self.rect.y < 780:
                self.rect.y += self.speed  

window = display.set_mode((1280, 920))
display.set_caption("Ping-pong")
background = transform.scale(image.load("Board.png"), (1280, 920))

# mixer.init()
# mixer.music.load("galaxy.mp3")
# mixer.music.play()

font.init()
font1 = font.Font(None, 36)
lose = font1.render("тебя взяли в плен иноприщеленцы. гг", True, (255, 0, 0))

firstplayer = Player("player1.png", 17, 120, 13, 45, 400)
secondplayer = Player("player2.png", 17, 120, 13, 1235, 400)

ballsprite = GameSprite("Ball.png", 30, 30, 20, 625, 445)

finish = False
clock = time.Clock()
FPS = 100
flag = True
while flag == True:

    for e in event.get():

        if e.type == QUIT:
            flag = False
    
    if finish != True:
        window.blit(background, (0, 0))
        firstplayer.reset()
        firstplayer.update("left")
        secondplayer.reset()
        secondplayer.update("right")
        ballsprite.reset()

    


    clock.tick(FPS)
    display.update()
    time.delay(20)