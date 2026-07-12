# Conditional Calculation Pipeline

## Purpose

Perform different calculations depending on a condition.

Selection = choose a path.


## Flow

Input
 ↓
Transform
 ↓
Selection
 ↓
Calculation
 ↓
Output


## Recognition Clues

- "If the value is..."
- "For values above..."
- "Otherwise..."
- "Different rules apply..."




## Reusable Algorithm

Receive data

Convert data type

Check condition

Choose calculation path

Display result


## Sample Code

hours = float(input("Hours: "))
rate = float(input("Rate: "))

if hours > 40:
    pay = (40 * rate) + ((hours - 40) * rate * 1.5)
else:
    pay = hours * rate

print(pay)
