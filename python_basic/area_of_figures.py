import math

shape = input()
area = 0

if shape == "square":
    side = float(input())
    area = side ** 2
elif shape == "rectangle":
    length = float(input())
    width = float(input())
    area = length * width
elif shape == "circle":
    radius = float(input())
    area = math.pi * radius ** 2
elif shape == "triangle":
    base = float(input())
    height = float(input())
    area = 0.5 * base * height

print(f"{area:.3f}")

