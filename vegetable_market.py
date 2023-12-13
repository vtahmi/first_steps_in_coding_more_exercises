euro = 1.94
veg_price_per_kg = float(input())
fruit_price_per_kg = float(input())
veg_total_kg = int(input())
fruit_total_kg = int(input())
total = veg_total_kg * veg_price_per_kg + fruit_total_kg * fruit_price_per_kg
total_euro = total / euro
print(f"{total_euro:.2f}")
