import turtle
import time
import asyncio

SHOP_ITEMS = {
    'item':'price',
    'sugar':100
}

score = 0

window = turtle.Screen()
window.title('Pattles\' Clicker Game')
window.bgcolor(0.36470588235294116, 0.6627450980392157, 0.9137254901960784)

window.register_shape(name='Assets/cookie.gif')
cookie = turtle.Turtle()
cookie.shape('Assets/cookie.gif')
cookie.speed(0)

window.register_shape(name='Assets/hamburger_menu.gif')
menu = turtle.Turtle()
menu.shape('Assets/hamburger_menu.gif')
menu.speed(0)
menu.penup()
menu.goto(295, 295)

pen = turtle.Turtle()
pen.hideturtle()
pen.pencolor('white')
pen.penup()
pen.goto(0, 200)
pen.write(f'Score: {score}', align='center', font=('Courier New', 32, 'bold'))

def clicked(x, y):
    global score
    score += 1
    pen.clear()
    pen.write(f'Score: {score}', align='center', font=('Courier New', 32, 'bold'))

def display_menu(x, y):
    pen.clear()
    cookie.hideturtle()
    menu.hideturtle()
    window.bgcolor(1, 0.7803921568627451, 0.34901960784313724)

    

cookie.onclick(clicked)
menu.onclick(display_menu)


if __name__ == '__main__':
    window.mainloop()
    

