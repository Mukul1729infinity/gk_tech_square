import turtle
pen=turtle.Turtle()
def hare():
    for i in range(200):
        pen.right(1)
        pen.forward(1)
def krishna():
    pen.fillcolor("red")
    pen.begin_fill()
    pen.left(140)
    pen.forward(113)
    hare()
    pen.left(120)
    hare()
    pen.forward(112)
    pen.end_fill()
def hare_krishna():
    pen.up()
    pen.setpos(-68,95)
    pen.down()
    pen.color('gold')
    pen.write(" HareKrishna",font=("Verdana",12,"bold"))
krishna()
hare_krishna()
pen.ht()
