# Input → Transform → Process → Output

Purpose

Take user data, prepare it, perform work, and display results.

Flow

Input
↓
Transform
↓
Process
↓
Output

Recognition Clues

- User enters numbers
- Calculation required
- Conversion needed

Examples

- Pay calculator
- Temperature converter
- Area calculator
- Unit conversion

Sample Code:

hours = input("Enter Hours: ")
rate = input("Enter Rate: ")

hours = float(hours)
rate = float(rate)

pay = hours * rate

print("Pay:", pay)
