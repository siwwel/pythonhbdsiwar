import turtle


def dessine_carre(tortue):
    for i in range(4):
        tortue.forward(50)
        tortue.right(90)
        turtle.setup(800, 600)

        wn = turtle.Screen()
        wn.bgcolor("lighthouse")
        wn.title("Python Turtle")

        tess = turtle.Turtle()
        dessine_carre(tess)
        wn.exitonclick()
