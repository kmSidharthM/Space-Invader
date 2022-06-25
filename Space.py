import pygame
import random
import math
from pygame import mixer

pygame.init()

screen=pygame.display.set_mode((500,500))
pygame.display.set_caption('SPACE INVADER')
icon=pygame.image.load('spaceship.png')
pygame.display.set_icon(icon)

#player details
playerimg=pygame.image.load('player.png')
playerx=218
playery=430
playerchangex=0

#multiple enemy details
enemyimg=[]
enemyx=[]
enemyy=[]
noofEnemy=2
enemyspeed=0.05
for i in range(2):
    enemyimg.append(pygame.image.load('enemy.png'))
    enemyx.append(random.randint(0,436))
    enemyy.append(100)

#bullet details
bulletimg=pygame.image.load('bullet.png')
bulletx=playerx
bullety=430
bulletchange=0.4
bulletstate="ready"


score=0
font=pygame.font.Font('freesansbold.ttf',32)
scorex=10
scorey=10

#adding background music
mixer.music.load('background.wav')
mixer.music.play(-1)

#gameover text
gm='GAME OVER'
gmtext=pygame.font.Font('freesansbold.ttf',64)

running=True
collision=False
background=pygame.image.load('background.png')

#funtion to display player
def player(x,y):
    screen.blit(playerimg,(x,y))

#funtion to display enemy
def enemy(x,y,i):
    screen.blit(enemyimg[i],(x,y))

#funtion to display bullets
def bullet(x,y):
    global bulletstate
    bulletstate="fire"
    screen.blit(bulletimg,(x+25,y))

#funtion to check for collision
def iscollision(enemyx,enemyy,bulletx,bullety):
    distance=math.sqrt(math.pow(enemyx-bulletx,2)+math.pow(enemyy-bullety,2))
    if distance<27:
        return True
    else:
        return False
    
#funtion to display score
def scoreval(x,y):
    scorevalue=font.render("Score:"+str(score),True,(255,255,255))
    screen.blit(scorevalue,(x,y))

#funtion to display game over
def gmfuntion():
    text=font.render(gm,True,(255,255,255))
    screen.blit(text,(150,240))


while running:
    screen.fill((200,200,255))
    screen.blit(background,(0,0))
    for event in pygame.event.get():
        if(event.type==pygame.QUIT):
            running=False
        if(event.type==pygame.KEYDOWN):
            if(event.key==pygame.K_LEFT):
                playerchangex=-0.15
            if(event.key==pygame.K_RIGHT):
                playerchangex=0.15
            if(event.key==pygame.K_SPACE):
                if bulletstate is "ready":
                    mixer.Sound('laser.wav').play()
                    bulletx=playerx 
                    bullet(bulletx,bullety)
        if(event.type==pygame.KEYUP):
            playerchangex=0

    playerx+=playerchangex
    if(playerx>=436):
        playerx=436
    if(playerx<=0):
        playerx=0
    player(playerx,playery)


    for i in range(2):
        if(enemyy[0]>405 and enemyy[1]>405):
            gmfuntion()
            break
        enemyy[i]+=enemyspeed
        enemy(enemyx[i],enemyy[i],i) 
        collision=iscollision(enemyx[i]-16,enemyy[i]-16,bulletx-4,bullety-4)
        if collision:
            mixer.Sound('explosion.wav').play()
            bullety=430
            bulletstate="ready"
            score+=1
            enemyx[i]=random.randint(0,436)
            enemyy[i]=0
            if(score%15==0):
                enemyspeed+=0.05
    
    if(bullety<0):
        bullety=playery
        bulletstate="ready"
    if bulletstate is "fire":
        bullet(bulletx,bullety)
        bullety-=bulletchange
    
    scoreval(scorex,scorey)
    pygame.display.update()

