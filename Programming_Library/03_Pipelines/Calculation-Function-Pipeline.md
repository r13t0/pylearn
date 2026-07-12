Great exercise. This one is important because it introduces a **new programming pattern**: **Function Decomposition**.

You already know:

* Variables ✅
* Input/output ✅
* Conditions ✅
* Loops ✅
* Strings ✅
* Files ✅

New concept:

* **Functions returning values** ✅

Let's run it through your framework.

---

# Step 1 — Problem Analysis (Decomposition)

## Purpose

Calculate gross pay while separating the calculation logic into a reusable function.

---

## Inputs

Two user inputs:

```
hours worked
hourly rate
```

Example:

```
45
10.50
```

---

## Outputs

Display:

```
Pay 498.75
```

---

## Constraints

* First 40 hours = normal rate
* Hours above 40 = 1.5 × rate
* Calculation must happen inside:

```python
computepay()
```

* Function must return the result.

---

## Sub-Problems

Break it down:

```
1. Get hours
2. Get rate
3. Convert strings to numbers
4. Send values to function
5. Calculate pay
6. Return result
7. Display result
```

---

# Step 2 — Pattern Recognition

## Pattern 1: Input → Assignment → Output

Already known.

```
Input
 ↓
Store
 ↓
Use
 ↓
Output
```

---

## Pattern 2: Selection

Used for overtime.

Question:

```
Are hours greater than 40?
```

Pattern:

```
Condition
    ↓
True branch
    ↓
False branch
```

---

## Pattern 3: Function Decomposition (NEW)

Purpose:

Separate a task into a reusable unit.

Instead of:

```
Program
 |
 |-- calculate everything
 |-- print everything
```

We create:

```
Main Program
      |
      |
      ↓
 computepay()
      |
      ↓
 return result
```

---

# Step 3 — Pattern Composition

Pipeline:

```
Input
 ↓
Assignment
 ↓
Type Conversion
 ↓
Function Call
 ↓
Selection
 ↓
Calculation
 ↓
Return Value
 ↓
Output
```

The controlling pattern:

```
Function Decomposition
```

because it controls where the calculation lives.

---

# Step 4 — Abstraction

Ignore Python.

The idea:

> Receive information, send it to a calculator, let the calculator produce a result, then display that result.

Mental model:

```
Input
  ↓
Machine
  ↓
Answer
```

A function is like a machine.

Example:

```
Coffee Machine

Input:
coffee beans + water

Process:
make coffee

Output:
coffee
```

Programming function:

```
Input:
hours + rate

Process:
calculate pay

Output:
pay
```

---

# Step 5 — Algorithm Design

No Python:

```
1. Ask user for hours.
2. Ask user for hourly rate.
3. Convert both values into numbers.
4. Send hours and rate to computepay.
5. Check if hours exceed 40.
6. If yes:
       calculate regular pay
       calculate overtime pay
       combine them
7. Otherwise:
       calculate normal pay.
8. Return the pay.
9. Display the returned value.
```

---

# Step 6 — Programming Concepts

## New Concept: Function

Purpose:

Reusable block of instructions.

Example:

```
computepay()
```

---

## Parameters

Function receives data:

```
hours
rate
```

---

## Return Value

Function sends data back:

```
return pay
```

---

## Existing Concepts Used

| Concept     | Purpose                 |
| ----------- | ----------------------- |
| Variables   | Store hours, rate, pay  |
| Input       | Receive user data       |
| float()     | Convert text to numbers |
| if/else     | Handle overtime         |
| Expressions | Calculate pay           |
| print()     | Display answer          |

---

# Step 7 — Python Toolbox

| Pattern        | Concept          | Python Tool |
| -------------- | ---------------- | ----------- |
| Input          | Receive data     | `input()`   |
| Conversion     | Change type      | `float()`   |
| Function       | Reusable logic   | `def`       |
| Function input | Receive values   | parameters  |
| Return         | Send answer back | `return`    |
| Selection      | Decision         | `if/else`   |
| Output         | Display          | `print()`   |

---

# Step 8 — Translation to Python

```python
def computepay(hours, rate):
    # Selection pattern
    if hours > 40:
        overtime_hours = hours - 40
        regular_pay = 40 * rate
        overtime_pay = overtime_hours * rate * 1.5
        pay = regular_pay + overtime_pay
    else:
        pay = hours * rate

    # Return value pattern
    return pay


# Input pattern
hrs = float(input("Enter Hours:"))
rph = float(input("Enter rate per hour:"))

# Function call pattern
pay = computepay(hrs, rph)

# Output pattern
print("Pay", pay)
```

Output:

```
Pay 498.75
```

---

# Step 9 — Generalization

## Problem Type

**Calculation with reusable logic**

---

## Recognition Clues

"When you see:"

* "Put the logic in a function"
* "Create a function called..."
* "Return a value"

Think:

```
Function Decomposition
```

---

## General Algorithm

```
Define function
      ↓
Receive inputs
      ↓
Process data
      ↓
Return result
      ↓
Use result
```

---

# Step 10 — Pattern Library Entry

```text
Pattern Name:
Function Decomposition

Purpose:
Break a large program into smaller reusable pieces.

Recognition Clues:
"When you see..."
- "Create a function"
- "Put logic inside..."
- "Return a value"

Inputs:
Function parameters

Outputs:
Return value

Algorithm:

Create function
↓
Receive data
↓
Process data
↓
Return answer

Programming Concepts:

- Functions
- Parameters
- Return values
- Scope

Python Toolbox:

def function_name():
return value

Common Variations:

1. Function with inputs
2. Function without inputs
3. Function returning values
4. Function performing actions

Often Combined With:

- Selection
- Iteration
- Validation
- Calculation

Common Mistakes:

- Forgetting return
- Printing instead of returning
- Wrong parameters

Example Problems:

- Calculate pay
- Calculate tax
- Convert units
- Calculate averages
```

---

# Step 11 — Pattern Pipeline Library

```text
Pipeline Name:

Calculation Function Pipeline


Purpose:

Receive data, process it, return a calculated result.


Flow:


Input

↓

Assignment

↓

Function Call

↓

Function Processing

↓

Selection

↓

Calculation

↓

Return Value

↓

Output


Recognition Clues:

"When the program needs a reusable calculation."


Reusable Algorithm:

1. Collect inputs.
2. Pass inputs into function.
3. Function processes data.
4. Function returns result.
5. Display result.
```

---

# Step 12 — Knowledge Update

## Already knew:

✅ Variables
✅ Input
✅ Output
✅ float conversion
✅ if/else
✅ arithmetic calculations

## New:

🆕 Functions with parameters
🆕 Return values
🆕 Function decomposition

## Existing patterns strengthened:

Selection:

```
if condition
```

now works inside a function.

---

This exercise is a major step because you moved from:

```
Write a program
```

to:

```
Design a system of reusable components
```

That is the beginning of software engineering thinking.

