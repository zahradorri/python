Python 3.11.3 (tags/v3.11.3:f3909b8, Apr  4 2023, 23:49:59) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import turtle 
... import random
... 
... emtiaz=0
... 
... m=turtle.Screen()
... m.setup(600,600)
... m.bgcolor('darkgreen')
... m.title('بازی لاک پشت و توپ')
... 
... divar=turtle.Turtle()
... divar.up()
... divar.goto(-275,275)
... divar.down()
... divar.width(4)
... for i in range(4):
...     divar.fd(550)
...     divar.rt(90)
... divar.ht()
... 
... 
... lakposht=turtle.Turtle()
... lakposht.shape('turtle')
... lakposht.color('white')
... lakposht.shapesize(2)
... lakposht.up()
... 
... 
... toop=turtle.Turtle()
... toop.shape('circle')
... toop.color('blue')
... toop.up()
... toop.goto(random.randint(-260,260),random.randint(-260,260))
... 
... def moveright():
...     lakposht.right(20)
... def moveleft():
    lakposht.left(20)

m.listen()
m.onkey(moveright,'d')
m.onkey(moveleft,'a')
w=turtle.Turtle()
w.up()
w.goto(-270,275)
w.ht()
w.color('black')
w.write('امتیاز:'+str(emtiaz))
while True:

    lakposht.fd(1)

    if lakposht.xcor() > 270 or lakposht.xcor() < -270 or lakposht.ycor() > 270 or lakposht.ycor() < -270:
        lakposht.right(180)
        emtiaz=emtiaz-2
        w.clear()
        w.write('امتیاز :'+str(emtiaz),font=12)

    if lakposht.distance(toop)<15:
        toop.goto(random.randint(-260,260),random.randint(-260,260))
        toop.color(random.choice(['red', 'lightgreen', 'blue', 'yellow', 'purple']))
        emtiaz=emtiaz+4
        w.clear()
        w.write('امتیاز :'+str(emtiaz))

        if emtiaz>=20:
            w.goto(-75,0)
            w.write('شما برنده شدید!!!',font=30)
