from turtle import *


def plot_tree(sz, level):
    if level > 0:
        colour = (color[0]//level, color[1]//level, color[2]//level)
        colormode(255)
        pencolor(colour)
        fd(sz)
        rt(angle)
        plot_tree(0.8 * sz, level - 1)
        pencolor(colour)
        lt(2 * angle)
        plot_tree(0.8 * sz, level - 1)
        pencolor(colour)
        rt(angle)
        fd(-sz)


tree_level = int(input("Digite o nível de recursividade da árvore: "))
color_choice = int(input("Escolha a cor da árvore: 1-cinza, 2-vermelha"
                         ", 3-verde, 4-azul, 5-ciano, 6-amarela, 7-magenta:\n"))
color = (0, 0, 0)
if color_choice == 1:
    color = (127, 127, 127)
elif color_choice == 2:
    color = (255, 0, 0)
elif color_choice == 3:
    color = (0, 255, 0)
elif color_choice == 4:
    color = (0, 0, 255)
elif color_choice == 5:
    color = (0, 255, 255)
elif color_choice == 6:
    color = (255, 255, 0)
elif color_choice == 7:
    color = (255, 0, 255)
speed('fastest')
rt(-90)
angle = 30
plot_tree(60, tree_level)
done()
