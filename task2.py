import turtle
import math

def draw_pythagoras_tree(t, branch_length, level):
    if level == 0:
        return

    if level % 2 == 0:
        t.color("blue")
    else:
        t.color("yellow")

    t.forward(branch_length)

    t.left(45)
    draw_pythagoras_tree(t, branch_length * math.sqrt(2) / 2, level - 1)

    t.right(90)
    draw_pythagoras_tree(t, branch_length * math.sqrt(2) / 2, level - 1)

    t.left(45)
    t.backward(branch_length)

def main():
    recursion_level = int(input("Введіть рівень рекурсії: "))

    t = turtle.Turtle()
    t.speed(0)  # Set speed to the maximum
    t.left(90)  # Point the turtle upwards

    window = turtle.Screen()
    window.bgcolor("white")
    window.title("Дерево Піфагора")

    draw_pythagoras_tree(t, 100, recursion_level)

    window.exitonclick()

if __name__ == "__main__":
    main()
