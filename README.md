
# Parking Lot Project

This Python project simulates parking lots using 2D lists and performs several analytical operations.

## Step 1 — Create Parking Lot
Generate a 6x5 parking lot with random car brands (`TOY`, `BMW`, `TES`, `KIA`, `HYU`) or empty spots.  
Display the parking lot and its row and column indexes.

## Step 2 — Count Cars and Empty Spots
Count how many `TES` cars appear in each row.  
Count how many empty spots exist in each odd-numbered column.

## Step 3 — Top 3 Brands
Count total cars of each brand in the parking lot.  
Sort and display the top 3 brands by frequency.

## Step 4 — Compare Two Parking Lots
Generate a second parking lot (8x10).  
Find brands that exist only in the first lot and brands that appear in both lots.

## Bonus Step — Merge and Detect Conflicts
Create two equal-sized parking lots and merge them into one:
- `None` if both spots are empty  
- The car brand if only one spot is occupied  
- `X` if both spots have different cars  
Display the merged lot, total number of conflicts, and their coordinates.

## Run
```bash
python parking_lot.py
````

## Author

Andrey Elgin
