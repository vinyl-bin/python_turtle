import turtle

turtle.setup(width=1000, height=300)
t=turtle.Turtle()

t.penup()
t.goto(-300,0)
t.color("red")
t.pendown()
t.circle(50, steps=3)
t.penup()
t.goto(-300,-50)
t.write("삼각형",front=(15))
t.pendown()