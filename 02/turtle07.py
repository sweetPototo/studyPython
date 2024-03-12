import turtle
turtle.shape("turtle")

for i in range(3):
    turtle.goto(0,-50*i)
    turtle.down() #거북이를 내려놔서 그리도록 함
    turtle.forward(100)
    turtle.up()   #거북이를 들어서 그리지 못하게 함
    
    
    

turtle.done()