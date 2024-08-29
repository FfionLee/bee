import pgzrun
import random

WIDTH=400
HEIGHT=400

score=0

bee=Actor('bee')
bee.pos=200,200

flower=Actor('flower')
flower.pos=90,40

g_o=False

def draw():
    screen.blit('backgroundgrass',(0,0))
    bee.draw()
    flower.draw()
    screen.draw.text("Score: "+str(score),center=(40,20))

    if g_o==True:
        screen.fill('purple')
        screen.draw.text('Your final score is'+str(score),center=(200,200))

def update():
    global score
    if keyboard.left:
        bee.x=bee.x-2
    if keyboard.right:
        bee.x=bee.x+2
    if keyboard.up:
        bee.y=bee.y-2
    if keyboard.down:
        bee.y=bee.y+2
    
    if bee.colliderect(flower):
        flower.pos=random.randint(10,390),random.randint(10,390)
        score=score+1

def gameover():
    global g_o
    g_o=True

    print('jjjjjjjjjjjjjjjjjj')

clock.schedule(gameover,5.0)
pgzrun.go()
