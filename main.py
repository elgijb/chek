import random

brands = ["TOY", "BMW", "TES", "KIA", "HYU"]

def generate_lot(rows, cols):
    lot = []
    for r in range(rows):
        row_data = []
        for c in range(cols):
            row_data.append(random.choice([None] + brands))
        lot.append(row_data)
    return lot

def step1(rows, cols):
    parking_lot = generate_lot(rows, cols)
    print("STEP 1: Parking Lot:")
    for row in parking_lot:
        print(row)
    print("Row indexes:", list(range(rows)))
    print("Column indexes:", list(range(cols)))
    return parking_lot

def step2(parking_lot):
    rows = len(parking_lot)
    cols = len(parking_lot[0])
    print("\nSTEP 2: TES count per row:")
    for i, row in enumerate(parking_lot):
        print(f"Row {i}: {row.count('TES')} TES cars")
    print("\nEmpty spots in odd columns:")
    for c in range(cols):
        if c % 2 == 1:
            empty_count = sum(1 for r in range(rows) if parking_lot[r][c] is None)
            print(f"Column {c}: {empty_count} empty spots")

def step3(parking_lot):
    rows = len(parking_lot)
    cols = len(parking_lot[0])
    counts = {b: 0 for b in brands}
    for r in range(rows):
        for c in range(cols):
            car = parking_lot[r][c]
            if car in counts:
                counts[car] += 1
    sorted_counts = sorted(counts.items(), key=lambda x: x[1], reverse=True)
    print("\nSTEP 3: Top 3 Brands in the Parking Lot:")
    for brand, num in sorted_counts[:3]:
        print(f"{brand} {num}")

def step4():
    rows1 = int(input("\nEnter rows for first parking lot: "))
    cols1 = int(input("Enter columns for first parking lot: "))
    parking_lot_1 = generate_lot(rows1, cols1)
    print("First Parking Lot:")
    for row in parking_lot_1:
        print(row)
    rows2 = int(input("\nEnter rows for second parking lot: "))
    cols2 = int(input("Enter columns for second parking lot: "))
    parking_lot_2 = generate_lot(rows2, cols2)
    print("Second Parking Lot:")
    for row in parking_lot_2:
        print(row)
    brands_lot1 = {cell for row in parking_lot_1 for cell in row if cell}
    brands_lot2 = {cell for row in parking_lot_2 for cell in row if cell}
    only_first = brands_lot1 - brands_lot2
    both = brands_lot1 & brands_lot2
    print("\nBrands only in the first parking lot:", only_first)
    print("Brands in both parking lots:", both)

def bonus(rows, cols):
    lot_a = generate_lot(rows, cols)
    lot_b = generate_lot(rows, cols)
    print("\nBONUS: Parking Lot A:")
    for row in lot_a:
        print(row)
    print("\nBONUS: Parking Lot B:")
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
    print("\nNumber of conflicts:", len(conflicts))
    print("Conflict coordinates:", conflicts)

def main():
    rows = int(input("Enter number of rows: "))
    cols = int(input("Enter number of columns: "))
    parking_lot = step1(rows, cols)
    step2(parking_lot)
    step3(parking_lot)
    step4()
    bonus(rows, cols)

if __name__ == "__main__":
    main()
