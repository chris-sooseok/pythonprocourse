from canvas import Canvas
from shapes import Rectangle, Square

# Get canvas width and height from the user
canvas_width = int(input("Enter canvas width: "))
canvas_height = int(input("Enter canvas height: "))

# Make a dictionary of color codes and prompt for color
colors = {"white": (255,255,255), "black": (0,0,0)}
canvas_color = input("Enter canvas color (white or black): ")

# Create a canvas with the user data
canvas = Canvas(canvas_height, canvas_width, colors[canvas_color])


while True:
    shape_type = input("rectangle or square? Enter quit to quit. ")

    if shape_type.lower() == "rectangle":
        rec_x = int(input("Enter rect x: "))
        rec_y = int(input("Enter rect y: "))
        rec_width = int(input("Enter rect width: "))
        rec_height = int(input("Enter rect height: "))
        red = int(input("Enter red color: "))
        green = int(input("Enter green color: "))
        blue = int(input("Enter blue color: "))

        # Create the rect
        r1 = Rectangle(rec_x, rec_y, rec_width, rec_height, (red, green, blue))
        r1.draw(canvas)

    if shape_type.lower() == "sqaure":
        sq_x = int(input("Enter square x: "))
        sq_y = int(input("Enter square y: "))
        sq_side = int(input("Enter square side: "))
        red = int(input("Enter red color: "))
        green = int(input("Enter green color: "))
        blue = int(input("Enter blue color: "))
        s1 = Square(sq_x, sq_y, sq_side, (red, green, blue))
        s1.draw(canvas)

    if shape_type.lower() == "quit":
        break

canvas.make("canvas.png")






