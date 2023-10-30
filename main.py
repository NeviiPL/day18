from turtle import *
import random
# import colorgram
#
# colors = colorgram.extract('image.jpg', 30)
#
# colors_list= []
# for color in colors:
#     new_color = (color.rgb.r, color.rgb.b, color.rgb.b)
#     colors_list.append(new_color)
#
# print(colors_list)

color_list = [(241, 245, 245), (226, 230, 230), (237, 218, 218), (142, 208, 208), (25, 48, 48), (24, 159, 159), (208, 113, 113), (143, 63, 63), (237, 234, 234), (230, 92, 92), (4, 197, 197), (218, 82, 82), (228, 43, 43), (54, 115, 115), (28, 117, 117), (194, 167, 167), (170, 96, 96), (107, 86, 86), (109, 87, 87), (240, 2, 2), (193, 46, 46), (2, 119, 119), (18, 20, 20), (49, 109, 109), (174, 172, 172), (116, 36, 36), (224, 186, 186), (58, 64, 64), (24, 24, 24), (153, 219, 219)]
tim = Turtle()
colormode(255)
Screen().setup(height=500, width=500)

x = -230
y = -230
dots_in_row = 0
number_of_dots = 0
tim.speed("fastest")
for _ in range (0,100):
    if dots_in_row < 10:
        tim.penup()
        tim.goto(x,y)
        tim.pendown()
        tim.pencolor(random.choice(color_list))
        tim.dot(20)
        number_of_dots =+ 1
        dots_in_row = dots_in_row + 1
        x = x + 50
    if dots_in_row == 10:
        x = -230
        y = y + 50
        dots_in_row = 0







Screen()
Screen().exitonclick()