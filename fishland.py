mackerel_price = float(input())
sprat_price = float(input())
palamud_price = float(input()) * (mackerel_price + mackerel_price * 0.60)
scad_price = float(input()) * (sprat_price + sprat_price * 0.80)
mussels_price = int(input()) * 7.50

total_price = palamud_price + scad_price + mussels_price
print(f"{total_price:.2f}")
