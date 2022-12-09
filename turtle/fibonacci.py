import turtle
import math


def plot_fibo(n):
    a = 0
    b = 1
    side_a = a
    side_b = b
    t.pencolor("blue")
    t.fd(b * factor)
    t.lt(90)
    t.fd(b * factor)
    t.lt(90)
    t.fd(b * factor)
    t.lt(90)
    t.fd(b * factor / 2)
    t.penup()
    t.rt(90)
    t.bk(b * factor / 2)
    if int(b * factor / 5) != 0:
        t.write(str(side_b), font=("Arial", int(b * factor / 5), "normal"))
    t.lt(180)
    t.bk(b * factor / 2)
    t.rt(90)
    t.pendown()
    t.fd(b * factor / 2)
    o = side_b
    side_b = side_b + side_a
    side_a = o
    for i in range(1, n):
        color = i
        while color > len(colors)-1:
            color -= len(colors)
        t.pencolor(colors[color])
        t.bk(side_a * factor)
        t.rt(90)
        t.fd(side_b * factor)
        t.lt(90)
        t.fd(side_b * factor)
        t.lt(90)
        t.fd(side_b * factor / 2)
        t.penup()
        t.rt(90)
        t.bk(side_a * factor / 2)
        if int(side_a*factor/5) != 0:
            t.write(str(side_b), font=("Arial", int(side_a * factor / 5), "normal"))
        t.lt(180)
        t.bk(side_a * factor / 2)
        t.rt(90)
        t.pendown()
        t.fd(side_b * factor / 2)
        o = side_b
        side_b = side_b + side_a
        side_a = o

    t.penup()
    t.setposition(factor, 0)
    t.seth(0)
    t.pendown()
    t.pencolor("red")
    t.lt(90)
    for i in range(n):
        print(b)
        fdwd = math.pi * b * factor / 2
        fdwd /= 90
        for j in range(90):
            t.fd(fdwd)
            t.lt(1)
        o = a
        a = b
        b = o + b


colors = ["black", "green", "blue", "magenta"]
n = 0
while n <= 1:
    n = int(input('Digite o número de iterações: '))
    if n <= 1:
        print("Por favor digite um valor acima de 1")
# calculo para adequar o fator de distância do turtle em relação ao tamanho do gráfico final
n1, n2 = 1, 1
count = 0
while count < n-2:
    nth = n1 + n2
    n1 = n2
    n2 = nth
    count += 1
# isso garante que o retângulo inteiro vai sempre caber na tela independentemente do valor de n
factor = 400/(n1+n2)
print("Números de fibonacci até", n, "elementos :")
t = turtle.Turtle()
t.speed(100)
plot_fibo(n)
turtle.done()
