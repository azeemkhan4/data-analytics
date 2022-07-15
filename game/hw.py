from turtle import width
import pgzrun


HEIGHT= 600
WIDTH=600
item=Rect((200,100),(25,25))
ivy=3
item2=Rect((300,200),(25,25))
i2vy=2
item3=Rect((400,300),(25,25))
i3vy=3
platform1=Rect((200,50),(50,250))
platform2=Rect((400,50),(50,250))

def item_motion_control(obj,plt,speed):
    obj.x += speed 
    if obj.x> WIDTH:
        obj.x=WIDTH
        speed=-speed
    if obj.x <0:
        obj.x=0
        speed= -speed
    if obj.colliderect(plt):
        speed = -speed
    return speed

def platform_control():
    if keyboard.down:
        platform1.y -=3
        platform2.y +=3
    elif keyboard.up:
        platform1.y +=3
        platform2.y -=3
    if platform1.y<0 :
        platform1.y=HEIGHT
    if platform1.y>HEIGHT:
        platform1.y=0
    if platform2.y<0 :
        platform2.y=HEIGHT
    if platform2.y>HEIGHT:
        platform2.y=0
    

    
def draw():
    screen.fill("white")
    screen.draw.filled_rect(item,'green')
    screen.draw.filled_rect(item2,'blue')
    screen.draw.filled_rect(item3,'red')

    screen.draw.filled_rect(platform1,'brown')
    screen.draw.filled_rect(platform2,'pink')

def update():
    global ivy
    global i2vy 
    global i3vy
    ivy=item_motion_control(item,platform1,ivy)
    i2vy=item_motion_control(item2,platform1,i2vy)
    i3vy=item_motion_control(item3,platform1,i3vy)
    ivy=item_motion_control(item,platform2,ivy)
    i2vy=item_motion_control(item2,platform2,i2vy)
    i3vy=item_motion_control(item3,platform2,i3vy)
    platform_control()
    print(item.x, item.y, ivy)
    
    
pgzrun.go()