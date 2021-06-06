import turtle
turtle.bgcolor("black")
var1=turtle.Screen()
var1.title("Animated Circles")
turtle=turtle.Turtle()
turtle.color('red')
turtle.speed(0)
turtle.hideturtle()
for i in range(150):
    turtle.circle(i*2)
    turtle._rotate(5)
var1.mainloop()