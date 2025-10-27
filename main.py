import random

brands = ["TOY", "BMW", "TES", "KIA", "HYU"]
rows = 6
cols = 5

parking_lot_1 = []
for r in range(rows):
    row_data = []
    for c in range(cols):
        row_data.append(random.choice([None] + brands))
    parking_lot_1.append(row_data)

print("Parking Lot 1 (6x5):")
for row in parking_lot_1:
    print(row)

rows2 = 8
cols2 = 10
parking_lot_2 = []
for r in range(rows2):
    row_data = []
    for c in range(cols2):
        row_data.append(random.choice([None] + brands))
    parking_lot_2.append(row_data)

print("\nParking Lot 2 (8x10):")
for row in parking_lot_2:
    print(row)

brands_lot1 = {cell for row in parking_lot_1 for cell in row if cell}
brands_lot2 = {cell for row in parking_lot_2 for cell in row if cell}

only_first = brands_lot1 - brands_lot2
both = brands_lot1 & brands_lot2

print("\nBrands only in the first parking lot:", only_first)
print("Brands in both parking lots:", both)
