length = int(input("길이:"))

import turtle
turtle.shape("turtle")

# turtle.forward(length*(2**0))  #2의 0제곱
# turtle.right(45)
# turtle.forward(length*(2**1))  #2의 0제곱
# turtle.right(45)
# turtle.forward(length*(2**2))  #2의 0제곱
# turtle.right(45)
# turtle.forward(length*(2**3))  #2의 0제곱
# turtle.right(45)
# turtle.forward(length*(2**4))  #2의 0제곱



for i in range(5):
    turtle.forward(length*(2**i))
    turtle.right(45)

turtle.done()