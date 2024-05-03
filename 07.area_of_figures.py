from math import pi

type_figure = input()
area = 0

if type_figure == "circle":
    radius = float(input())
    area = pi* pow(radius,2)
elif type_figure == "square":
    a_side = float(input())
    area = pow(a_side,2)
elif type_figure == "rectangle":
    a_side = float(input())
    b_side=float(input())
    area = a_side*b_side
elif type_figure == "triangle":
    a_side = float(input())
    h_side = float(input())
    area = (a_side * h_side)/2
print(area)
