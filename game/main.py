from pygame import *
from random import randint
from time import time as kub
lost = 0
score = 0
rel_time = False
num_fire = 0
score1text = 0
score2text = 0

mixer.init()
mixer.music.set_volume(0.5)
mixer.music.load("game/assets/background.mp3")
mixer.music.play()

ball2platform = mixer.Sound("game/assets/platform.mp3")

ball2window = mixer.Sound("game/assets/window.mp3")

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


class Ball(GameSprite):
    def __init__(self, image1, resolution1, resolution2, speedx, speedy, x1, y1):
        sprite.Sprite.__init__(self)
        self.image = transform.scale(image.load(image1), (resolution1, resolution2))
        self.rect = self.image.get_rect()
        self.rect.x = x1
        self.rect.y = y1
        self.speedx = speedx
        self.speedy = speedy

    def motion(self, enemy):
        global score1text
        global score2text
        # self.rect.x += self.speedx
        # self.rect.y += self.speedy

        if sprite.collide_rect(enemy, self):
            self.speedx *= -1
            ball2platform.play()

            if self.rect.x < 104:
                score1text += 1

            if self.rect.x > 1154:
                score2text += 1


window = display.set_mode((1280, 920))

display.set_caption("Ping-pong")
background = transform.scale(image.load("game/assets/background.png"), (1280, 920))



font.init()
font1 = font.Font(None, 36)

lose = font1.render("первый игрок проиграл!", True, (255, 0, 0))
lose2 = font1.render("второй игрок проиграл!", True, (255, 0, 0))

# score1 = font1.render("Счёт: " + str(score1text), True, (255, 255, 255))
# score2 = font1.render("Счёт: " + str(score2text), True, (255, 255, 255))


firstplayer = Player("game/assets/player1.png", 17, 120, 20, 45, 400)
secondplayer = Player("game/assets/player2.png", 17, 120, 20, 1235, 400)

ballsprite = Ball("game/assets/ball.png", 30, 30, 15, 10, 625, 445)


score_back_left = GameSprite("game/assets/ScoreBar.png", 341, 47, 0, 0, 0)
score_back_right = GameSprite("game/assets/ScoreBar2.png", 341, 47, 0, 939, 0)


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
        score_back_left.reset()
        score_back_right.reset()
        ballsprite.rect.x += ballsprite.speedx
        ballsprite.rect.y += ballsprite.speedy

        ballsprite.motion(firstplayer)
        ballsprite.motion(secondplayer)

        if ballsprite.rect.y > 920-40 or ballsprite.rect.y < 1:
            ballsprite.speedy *= -1
            ball2window.play()
        score1 = font1.render("Счёт: " + str(score1text), True, (255, 255, 255))
        score2 = font1.render("Счёт: " + str(score2text), True, (255, 255, 255))
        window.blit(score1, (10, 10))
        window.blit(score2, (1180, 10))

        if ballsprite.rect.x < 10:
            finish == True
            window.blit(lose, (50, 50))

        if ballsprite.rect.x > 1260:
            finish == True
            window.blit(lose2, (930, 50))

    clock.tick(FPS)
    display.update()
    time.delay(20)