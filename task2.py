import turtle
import math

def draw_pythagoras_tree(t, branch_length, level):
    if level == 0:
        return

    # Alternate colors between blue and yellow
    if level % 2 == 0:
        t.color("blue")
    else:
        t.color("yellow")

    # Draw the current branch
    t.forward(branch_length)

    # Save the current state of the turtle
    t.left(45)
    draw_pythagoras_tree(t, branch_length * math.sqrt(2) / 2, level - 1)

    t.right(90)
    draw_pythagoras_tree(t, branch_length * math.sqrt(2) / 2, level - 1)

    # Restore the state of the turtle
    t.left(45)
    t.backward(branch_length)

def main():
    # Get user input for the recursion level
    recursion_level = int(input("Введіть рівень рекурсії: "))

    # Create turtle
    t = turtle.Turtle()
    t.speed(0)  # Set speed to the maximum
    t.left(90)  # Point the turtle upwards

    # Initialize the turtle graphics window
    window = turtle.Screen()
    window.bgcolor("white")
    window.title("Дерево Піфагора")

    # Draw the Pythagoras tree
    draw_pythagoras_tree(t, 100, recursion_level)

    # Close the turtle graphics window on click
    window.exitonclick()

if __name__ == "__main__":
    main()
