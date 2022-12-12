import turtle
import random


def player_move(player):
    player_turn = input("Pressione 'Enter' para rolar o dado ")
    die_outcome = random.choice(die)
    print("O resultado da rolagem foi: ")
    print(die_outcome)
    print("O número de passos será: ")
    print(20 * die_outcome)
    player.fd(20 * die_outcome)


player_one = turtle.Turtle()
player_one.color("green")
player_one.shape("turtle")
player_one.penup()
player_one.goto(-200, 100)
player_two = player_one.clone()
player_two.color("blue")
player_two.penup()
player_two.goto(-200, -100)

player_one.goto(300, 60)
player_one.pendown()
player_one.circle(40)
player_one.penup()
player_one.goto(-200, 100)

player_two.goto(300, -140)
player_two.pendown()
player_two.circle(40)
player_two.penup()
player_two.goto(-200, -100)

die = [1, 2, 3, 4, 5, 6]

for i in range(20):
    if player_one.pos() >= (300, 100):
        print("Jogador Nº1 Venceu!")
        break
    elif player_two.pos() >= (300, -100):
        print("Jogador Nº2 Venceu!")
        break
    else:
        player_move(player_one)
        player_move(player_two)
