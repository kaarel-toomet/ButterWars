#!/usr/bin/python3
import pygame as pg
import random as r
pg.init()
pic = pg.image.load("mrbutter1.png")
pics = pg.image.load("mrbutter1stab.png")
picf = pg.image.load("mrbutter1flip.png")
picsf = pg.image.load("mrbutter1stabflip.png")
gstkm = pg.image.load("greenstickman.png")
gstkmp = pg.image.load("greenstickmanpunch.png")
screen = pg.display.set_mode((0,0), pg.RESIZABLE)
screenw = screen.get_width()
screenh = screen.get_height()
pg.display.set_caption("egg")
do = True
dist = 4
mup = False
mdown = False
mleft = False
mright = False
gofast = False
timer = pg.time.Clock()
gstick = 0
gsmax = 120
points = 0
hp = 5
font = pg.font.SysFont("Times", 24)
dfont = pg.font.SysFont("Times", 32)
pfont = pg.font.SysFont("Times", 50)
pause = False
gameover = False
player = pg.sprite.Group()
gstickmen = pg.sprite.Group()
atk = False
fc = 0
attick = 0
attimer = False
gsugly = 0
ac = 0
class Player(pg.sprite.Sprite):
    def __init__(self,x,y):
        pg.sprite.Sprite.__init__(self)
        self.image = pic
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def update(self, mup, mdown, mleft, mright):
        global fc, atk
        if fc == 0 and atk == False:
            self.image = pic
        if fc == 1 and atk == False:
            self.image = picf
        if fc == 0 and atk == True:
            self.image = pics
        if fc == 1 and atk == True:
            self.image = picsf
        if self.rect.y <= 0:
            up = False
        else:
            up = True
        if self.rect.y >= screenh-100:
            down = False
        else:
            down = True
        if self.rect.x <= 0:
            left = False
        else:
            left = True
        if self.rect.x >= screenw-124:
            right = False
        else:
            right = True
        if mup and up:
            self.rect.y -= dist 
        if mdown and down:
            self.rect.y += dist
        if mleft and left:
            self.rect.x -= dist
        if mright and right:
            self.rect.x += dist
class Gstick(pg.sprite.Sprite):
    def __init__(self, x, y, img):
        pg.sprite.Sprite.__init__(self)
        self.image = img
        self.rect = self.image.get_rect()
        self.x = float(x)
        self.y = float(y)
        self.rect.x = int(self.x)
        self.rect.y = int(self.y)
        self.hp = 5
        self.ptick = r.randint(0, 60)
        self.punch = False
        self.pl = 0
    def update(self):
        self.x += 0
        if self.pl <= 0:
            self.ptick += 1
            self.image = gstkm
        else:
            self.pl -= 1
        if self.ptick >= 60:
            self.punch = True
            self.image = gstkmp
            self.ptick = 0
            self.pl += 5

def reset():
    global points, hp, atick, gtick, atimer, gtimer, otick,\
           omax, slowtick, sbtick, sbmax, imtick, gameover, speed,\
           speedf
    gameover = False
    screen.fill((0, 0, 0))
    points = 0
    hp = 5
    gstickmen.empty()
    gstickmen.add(Gstick(r.uniform(10,screenw-96),screenh-96, gstkm))
mb = Player(screenw/2,screenh-128)
player.add(mb)
while do:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            do = False
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_LEFT:
                mleft = True
                fc = 0
            elif event.key == pg.K_RIGHT:
                mright = True
                fc = 1
            elif event.key == pg.K_p:
                pause = True
            elif event.key == pg.K_r:
                reset()
            elif event.key == pg.K_SPACE and ac == 0:
                atk = True
                attimer = True
                attick = 5
                ac += 60
        elif event.type == pg.MOUSEBUTTONDOWN:
            gofast = True
        elif event.type == pg.MOUSEBUTTONUP:
            gofast = False
        elif event.type == pg.KEYUP:
            if event.key == pg.K_UP:
                mup = False
            elif event.key == pg.K_DOWN:
                mdown = False
            elif event.key == pg.K_LEFT:
                mleft = False
            elif event.key == pg.K_RIGHT:
                mright = False
    while pause:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pause = False
                do = False
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_p:
                    pause = False
        pd = "PAUSED"
        ptext = dfont.render(pd, True, (127,127,127))
        ptext_rect = ptext.get_rect()
        ptext_rect.centerx = screen.get_rect().centerx
        ptext_rect.y = 50
        screen.blit(ptext,ptext_rect)
        screen.blit(text,text_rect)
        pg.display.update()
    if hp <= 0:
        uded = "GAME OVER"
        dtext = dfont.render(uded, True, (255,0,0))
        dtext_rect = dtext.get_rect()
        dtext_rect.centerx = screen.get_rect().centerx
        dtext_rect.y = 30
        screen.blit(dtext,dtext_rect)
        screen.blit(text,text_rect)
        pg.display.update()
        gameover = True
    while gameover:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                gameover = False
                do = False
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_r:
                    reset()
        uded = "GAME OVER"
        dtext = dfont.render(uded, True, (255,0,0))
        dtext_rect = dtext.get_rect()
        dtext_rect.centerx = screen.get_rect().centerx
        dtext_rect.y = 30
        screen.blit(dtext,dtext_rect)
        screen.blit(text,text_rect)
        pg.display.update()
    acol = pg.sprite.spritecollide(mb,gstickmen,False)
    if len(acol) > 0 and atk == True:
        points += 1
        gstickmen.remove(acol)

    if r.uniform(0, 1) < 1/300:
        gstickmen.add(Gstick(r.uniform(10,screenw-90),screenh-96,gstkm))
    if ac > 0:
        ac -= 1
    screen.fill((64,128,255))
    status = ("Score: " + str(points) + " Health: " + str(hp))
    text = font.render(status, True, (255,255,255))
    text_rect = text.get_rect()
    text_rect.centerx = screen.get_rect().centerx
    text_rect.y = 10
    screen.blit(text,text_rect)
    player.update(mup,mdown, mleft, mright)
    player.draw(screen)
    gstickmen.update()
    gstickmen.draw(screen)
    if attimer:
        attick -= 1
    if attick == 0:
        attimer = False
        atk = False
    pg.display.update()
    if not gofast:
        timer.tick(60)

pg.quit()
