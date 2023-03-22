import turtle


def draw_squares():

    t = turtle.Turtle()
    t.speed(1)
    t.pensize(2)
    t.color('pink')

    for length in range(20, 100, 20):

        t.penup()
        t.goto(-length/2, length/2)
        t.pendown()

        for _ in range(4):
            t.fd(length)
            t.right(90)

    turtle.exitonclick()


def draw_poly(t, n, sz):
    t.speed(1)
    t.pensize(2)
    t.color('pink')

    for _ in range(n):
        t.fd(sz)
        t.right(360/n)

    turtle.exitonclick()


def sum_to(n):
    return (n+1)*n//2


def draw_spirals():
    t = turtle.Turtle()

    t.penup()
    t.goto(-100, 0)
    t.pendown()

    t.speed(0)
    t.pensize(2)
    t.color('blue')

    for length in range(2, 160, 2):
        t.fd(length)
        t.right(90)

    t.penup()
    t.goto(100, 0)
    t.pendown()

    for length in range(2, 160, 2):
        t.fd(length)
        t.right(91)

    turtle.exitonclick()


if __name__ == "__main__":
    # draw_squares()

    # tess = turtle.Turtle()
    # draw_poly(tess, 8, 50)

    # print(sum_to(10))

    draw_spirals()
