import random

brands = ["TOY", "BMW", "TES", "KIA", "HYU"]
rows = 6
cols = 5

parking_lot = []
for r in range(rows):
    row_data = []
    for c in range(cols):
        row_data.append(random.choice([None] + brands))
    parking_lot.append(row_data)

print("Parking Lot (6x5):")
for row in parking_lot:
    print(row)

print("Row indexes:", list(range(rows)))
print("Column indexes:", list(range(cols)))
