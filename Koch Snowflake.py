import turtle

turtle.speed(0)
turtle.shape("turtle")

turtle.penup()
turtle.goto(-150, 100)
turtle.pendown()
# Move forward
# Turn left
# Move forward
# Turn right
# Move forward
# Turn left
# Move forward


def snowflake(lengthSide, levels):
  # Base Case
  if (levels == 0):
    turtle.forward(lengthSide)
    return
  
  lengthSide = lengthSide / 3.0
  
  # Recursive Case
  # Moving forward
  snowflake(lengthSide, levels - 1)
  turtle.left(60)  # turn left
  
  snowflake(lengthSide, levels - 1)
  turtle.right(120)
  
  snowflake(lengthSide, levels - 1)
  turtle.left(60)
  
  snowflake(lengthSide, levels - 1)
  
for i in range(3):
  
  snowflake(200, 4)
  turtle.right(120)
