from turtle import *
from math import *
width(1)


def d(n):
    p = 500 / int(n)
    return p


def h(p):
    d1 = p / 2
    s = d1 / (sqrt(3) / 2)
    return s


def figure(s, p, n):
    speed(500)
    x = -350
    y = 300
    n = int(n)
    r = n // 2
    penup()
    goto(x, y)
    pendown()
    pp = 1
    for l in range(r):
        color('black')
        yell = 'yellow'
        gr = 'green'
        nn = 1
        n = int(n)
        if pp % 2 == 0:
            yell = 'yellow'
            gr = 'green'
        else:
            yell = 'green'
            gr = 'yellow'
        for i in range(n):
            if nn % 2 == 0:
                fillcolor(gr)
            else:
                fillcolor(yell)
            begin_fill()
            right(-30)
            forward(s)
            for q in range(5):
                right(60)
                forward(s)
            end_fill()
            right(90)
            penup()
            forward(p)
            pendown()
            nn += 1
            continue
        right(90)
        penup()
        forward(s)
        forward(s)
        left(-60)
        forward(s)
        pendown()
        left(-30)
        nn = 1
        for i in range(n):
            if nn % 2 == 0:
                fillcolor(yell)
            else:
                fillcolor(gr)
            begin_fill()
            right(-30)
            forward(s)
            for q in range(5):
                right(60)
                forward(s)
            end_fill()
            right(90)
            penup()
            forward(p)
            pendown()
            nn += 1
            continue
        pp += 1
        right(90)
        penup()
        forward(s)
        forward(s)
        left(-60)
        forward(s)
        left(-30)
        right(90)
        forward(3 * s)
        right(-90)
        pendown()
    mainloop()



def main():
    n = numinput('n', 'Пожалуйста, введите количество шестиугольников, располагаемых в ряд:', 0, minval=4, maxval=20)
    p = d(n)
    a = h(p)
    figure(a, p, n)



if __name__ == '__main__':
    main()