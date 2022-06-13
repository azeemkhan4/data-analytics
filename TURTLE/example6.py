from turtle import*
t=Turtle()
t.speed('fastest')
bgcolor('black')
t.color('red')
t.pensize(7)
for i in range(1,401,3):
    t.fd(i)
    t.lt(60)
mainloop()