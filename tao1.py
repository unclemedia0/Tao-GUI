import turtle
import random
ເຕົ່າ = turtle.Turtle()
ເຕົ່າ.shape('turtle')
color = ['red','blue','green','purple','orange','pink']
ເຕົ່າ.speed(2)

for i in range(36):
    i = random.choice(color)
    ເຕົ່າ.color(i)
    ເຕົ່າ.forward(100)
    ເຕົ່າ.backward(100)
    ເຕົ່າ.left(10)
    
for UncleMedia in range(1,30):
    i = random.choice(color)
    ເຕົ່າ.color(i)
    ເຕົ່າ.circle(50)
    ເຕົ່າ.left(35)
    print('ຮອບທີ່:',UncleMedia)


'''
c = random.choice(color)
tao.home()
for i in range(1,11):
    c = random.choice(color)
    w = random.randint(10,100)
    l = random.randint(10,100)
    origin_x = random.randint(-300,300)
    origin_y = random.randint(-300,300)
    tao.goto(origin_x,origin_y)
    tao.pensize(3)
    print("-------")
    tao.color(c)
    tao.pendown()
    tao.fd(w)
    tao.rt(90)
    tao.fd(1)
    tao.rt(90)
    tao.fd(w)
    tao.rt(90)
    tao.fd(1)
    tao.penup()
    
tao.home()

'''
