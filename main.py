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

print("\nCount of TES cars per row:")
for i, row in enumerate(parking_lot):
    count_tes = row.count("TES")
    print(f"Row {i}: {count_tes} TES cars")

print("\nCount of empty spots in odd columns:")
for c in range(cols):
    if c % 2 == 1:
        empty_count = sum(1 for r in range(rows) if parking_lot[r][c] is None)
        print(f"Column {c}: {empty_count} empty spots")

counts = {b: 0 for b in brands}
for r in range(rows):
    for c in range(cols):
        car = parking_lot[r][c]
        if car in counts:
            counts[car] += 1

sorted_counts = sorted(counts.items(), key=lambda x: x[1], reverse=True)
print("\nTop 3 Brands in the Parking Lot:")
for brand, num in sorted_counts[:3]:
    print(f"{brand} {num}")
