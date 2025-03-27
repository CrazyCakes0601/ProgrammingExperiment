# This will be a clock face project that will display the time in an analog format.
from turtle import*
delay(0)

def drawhour(hournumber:int):
    hourangle = 90-(hournumber*30)
    romnums = ["XII","I","II","III","IV","V","VI","VII","VIII","IX","X","XI"]
    setpos(0, 150)
    setheading(hourangle)
    forward(90)
    down()
    color("red")
    circle(1)
    up()
    color("white")
    forward(20)
    write(romnums[hournumber], True, align="center", font=('Arial', 16, 'normal'))

def drawminute(minutenumber:int):
    minuteangle = 90-(minutenumber*6)
    setpos(0, 150)
    setheading(minuteangle)
    forward(140)
    down()
    color("black")
    circle(1)
    up()    

home()
print(position())

print(heading())

fillcolor("light gray")
begin_fill()
circle(150)
print(position())
end_fill()

up()

setpos(0, 140)
fillcolor("black")
begin_fill()
circle(10)
end_fill()


setpos(0, 30)

color("black")

for minute in range(60):
    drawminute(minute)

for hour in range(12):
    drawhour(hour)

setpos (0, 150)

setheading(30*-4.50) # hour hand

down()

color("black")

forward(75)

back(75)

setheading(-90) # minute hand

forward(110)

up()

down()

print(heading())

hideturtle()

done()