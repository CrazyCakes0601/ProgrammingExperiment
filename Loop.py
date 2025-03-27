from turtle import *
delay(0)
for steps in range(100):
    for c in ( 'red' , 'orange' , 'yellow'):
        color(c)
        forward(steps)
        right(30)
        # gray + tan + black -  green + purple + blue - cyan + purple + hot pink
        # hot pink + yellow + cyan - navy + blue + cyan
hideturtle()
done()        