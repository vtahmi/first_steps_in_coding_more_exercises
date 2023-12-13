green_paint_l = 3.4
red_paint_l = 4.3
door = 2 * 1.2
windows = (1.5 * 1.5) * 2
x = float(input())
y = float(input())
h = float(input())
house_body_front = (x * x) * 2
house_body_sides = (x * y) * 2
house_roof_front = x * h / 2
house_roof_side = (x * y) * 2
house_body = (house_body_front - door) + (house_body_sides - windows)
house_roof = (house_roof_front * 2) + house_roof_side
green_paint = house_body / green_paint_l
red_paint = house_roof / red_paint_l
print(f"{green_paint:.2f}")
print(f"{red_paint:.2f}")
