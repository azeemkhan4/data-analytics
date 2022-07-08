import pgzrun
from pygame import Rect
WIDTH=500
HEIGHT=500
box1= Rect((100,250),(50,50))
box2= Rect((100,200),(50,50))
box1_vx = 2
box2_vy =3
def draw():
    screen.fill('black')
    screen.draw.text("rukega" , (10,10),color="white")
    screen.draw.filled_rect(box1,"yellow")
    screen.draw.filled_rect(box2,"red")

def update():
    global box1_vx , box2_vy
    box1.x += box1_vx
    box2.y += box2_vy
    if box1.x>WIDTH:
        box1.x=0
    if box1.x <0:
        box1.x =WIDTH
    if box2.y <0:
        box2.y =HEIGHT
    
    if box2.y>HEIGHT:
        box2.y=0
    if box1.colliderect(box2):
        box1_vx= -box1_vx
    if box2.colliderect(box1):
        box2_vy= -box2_vy
    
    
pgzrun.go()