forecast = float(input())
if 26.00 <= forecast <= 35.00:
    print("Hot")
elif 20.1 <= forecast <= 25.9:
    print("Warm")
elif 15.00 <= forecast <= 20.00:
    print("Mild")
elif 12.00 <= forecast <= 14.9:
    print("Cool")
elif 5.00 <= forecast <= 11.9:
    print("Cold")
else:
    print("unknown")



