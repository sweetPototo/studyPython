length = int(input("길이 :"))

import turtle
turtle.shape("turtle")

# turtle.forward(length/(2**0))
# turtle.right(45)
# turtle.forward(length/(2**1))
# turtle.right(45)
# turtle.forward(length/(2**2))
# turtle.right(45)
# turtle.forward(length/(2**3))
# turtle.right(45)
# turtle.forward(length/(2**4))
# turtle.right(45)

for i in range(5):
    turtle.forward(length/(2**i))
    turtle.right(45)

turtle.done()