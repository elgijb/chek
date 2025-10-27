import random

brands = ["TOY", "BMW", "TES", "KIA", "HYU"]
rows = 6
cols = 5

def generate_lot(rows, cols):
    lot = []
    for r in range(rows):
        row_data = []
        for c in range(cols):
            row_data.append(random.choice([None] + brands))
        lot.append(row_data)
    return lot

lot_a = generate_lot(rows, cols)
lot_b = generate_lot(rows, cols)

print("Parking Lot A:")
for row in lot_a:
    print(row)

print("\nParking Lot B:")
for row in lot_b:
    print(row)

merged_lot = []
conflicts = []

for r in range(rows):
    merged_row = []
    for c in range(cols):
        a = lot_a[r][c]
        b = lot_b[r][c]
        if a is None and b is None:
            merged_row.append(None)
        elif a is None:
            merged_row.append(b)
        elif b is None:
            merged_row.append(a)
        elif a == b:
            merged_row.append(a)
        else:
            merged_row.append("X")
            conflicts.append((r, c))
    merged_lot.append(merged_row)

print("\nMerged Parking Lot:")
for row in merged_lot:
    print(row)

print(f"\nNumber of conflicts: {len(conflicts)}")
print("Conflict coordinates:", conflicts)
